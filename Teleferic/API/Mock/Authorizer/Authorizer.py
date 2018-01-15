import base64
import logging
from Crypto.Hash import SHA256, HMAC

from libs.tools import Identity, AES
from .. import Reader, Teleferic_Identity, Writer
from .constants import (
    MessageTypes,
    BodyTypes,
    PUBLIC_AES_KEY,
    Parameters
)

from .validators import validate_containers

from collections import OrderedDict
import msgpack
from API.Mock.utils import decode_hash
import time

def validate_timestamped_signature(sender_pubkey, message_hash, signature):
    identity = Identity(sender_pubkey)

    sign = signature[b'signature']
    timestamp = signature[b'timestamp']

    teleferic_signature = msgpack.unpackb(base64.b64decode(timestamp))
    
    #Validate if timestamp is signed by Teleferic
    if not Teleferic_Identity.verify_signature(teleferic_signature[b'timestamp'],teleferic_signature[b'signature']):
        raise Exception("Invalid sign")

    #Validate tolerance
    message_timestap = float(teleferic_signature[b'timestamp'])
    if time.time() - message_timestap > Parameters.TOLERABLE_TIME_DIFFERENCE_IN_SECONDS:
        raise Exception("Invalid sign")

    validator_map = OrderedDict()
    validator_map['messageHash'] = base64.b64encode(message_hash)
    validator_map['timestamp'] = timestamp

    validator = msgpack.packb(validator_map)

    if not identity.verify(validator, sign):
        raise Exception("Invalid sign")


def authorize_message(envelope):
    check_sender = True
    '''
        If message type is REGISTRATION
        and bodyType is REGISTRATION
        the sender should be new and his
        pubkey should not be present
    '''
    if False and Reader.get_message_existance(envelope.get('messageHash')):
        raise Exception('Message already registred')
    if envelope.get('messageType') == MessageTypes.REGISTRATION:
        try:
            public_cipher = AES(PUBLIC_AES_KEY)
            message = envelope.get('message')
            message_content_raw = public_cipher.decrypt(message)
            
            # Parse message
            message_content = msgpack.unpackb(message_content_raw)
            logging.warning(repr(message_content.get(b'bodyType')))
            if message_content.get(b'bodyType') == BodyTypes.Registration.REGISTRATION:
                check_sender = False
                message_body = msgpack.unpackb(
                    base64.b64decode(message_content.get(b'messageBody')))
                sender_pubkey = message_body.get(b'publicKey').decode()
        except Exception as e:
            raise Exception(
                'Invalid public message content passphrase, should be {}'.format(PUBLIC_AES_KEY)
            )

    if check_sender:
        # Validate Sender
        sender = envelope.get('sender')
        sender_pubkey = Reader.get_persona(address=sender).pubkey
    
    # Validate MessageHash
    message = envelope.get('message').encode()
    message_hash = envelope.get('messageHash')
    if message_hash != SHA256.new(message).digest():
        raise Exception("Invalid messageHash")
    
    # Validate Sign
    signature = envelope.get('messageSig')
    validate_timestamped_signature(sender_pubkey, message_hash, signature)

    if envelope.get('messageType') != MessageTypes.REGISTRATION:
        # Validate ACL readers
        ACL = envelope.get('ACL')
        if ACL:
            for ACL_rule in ACL:
                reader = ACL_rule.get('reader')
                # Rise an exception if some address be not registred
                Reader.get_persona(address=reader)
        else:
            raise Exception('Invalid ACL')
        
        validate_containers(sender_pubkey,envelope.get('containers'))
    else:
        
        # Validate Pulic Message
        # Decrypt
        public_cipher = AES(PUBLIC_AES_KEY)
        try:
            # Parse message
            message_content_raw = public_cipher.decrypt(message)
            message_content = msgpack.unpackb(message_content_raw)
        except Exception as e:
            raise Exception('Invalid public message content.')

        # Validate Body
        body_hash = envelope.get('bodyHash')
        message_body_raw = message_content.get(b'messageBody')
        current_body_hash = SHA256.new(message_body_raw).digest()
        if body_hash != current_body_hash:
            raise Exception('Invalid bodyHash.')

        # Validate dossierSalt
        dossier_salt = message_content.get(b'dossierSalt')
        if len(dossier_salt) != 40:
            raise Exception('Invalid dossierSalt.')

        # Validate dossierHash
        dossier_hash = envelope.get('dossierHash')
        if dossier_hash != HMAC.new(dossier_salt, message_body_raw, SHA256).digest():
            raise Exception('Invalid dossierHash.')

        # Parse message body
        try:
            decoded_message_body = base64.b64decode(message_body_raw)
            message_body = msgpack.unpackb(decoded_message_body)
        except Exception as e:
            raise Exception('Invalid messageBody.')

        {
            0: validate_invite,
            1: validate_registration
        }.get(message_content.get(b'bodyType'))(message_body)

    return True


def validate_registration(message_body):
    # Validate bootstrap node
    invite_message_hash = message_body.get(b'inviteMsgID')
    if invite_message_hash in (None, ''):
        raise Exception('Invalid invite message hash.')

    nickname = message_body.get(b'publicNickname')
    if nickname in (None, ''):
        raise Exception('Invalid nickname.')

    logging.info("AES KEY: %s", PUBLIC_AES_KEY)

    # Try deciphering the message using the public aes key.
    invite_message = Reader.get_message_content(decode_hash(invite_message_hash))
    public_cipher = AES(PUBLIC_AES_KEY)
    try:
        invite_message_content_raw = public_cipher.decrypt(invite_message)
        # Parse message
        invite_message_content = msgpack.unpackb(
            invite_message_content_raw)
        invite_message_body_content = msgpack.unpackb(base64.b64decode(
            invite_message_content.get(b'messageBody')))
    except Exception as e:
        raise Exception('Invalid invite message content.')

    # Extract the keyProof from the registration message
    key_proof_raw = message_body.get(b'keyProof')
    try:
        key_proof = Teleferic_Identity.decrypt_content(key_proof_raw)
    except Exception as e:
        raise Exception('Invalid keyProof1.')
    if key_proof == None:
        raise Exception('Invalid keyProof.2')

    # Try decoding the original inviteName from the invite message.
    decoder = AES(key_proof)

    original_invite_name_raw = invite_message_body_content.get(b'inviteName')
    original_invite_name = decoder.decrypt(original_invite_name_raw)

    given_invitite_name_raw = message_body.get(b'inviteName')
    given_invitite_name = Teleferic_Identity.decrypt_content(
        given_invitite_name_raw)

    # Check the registration invite name against the original invite name.
    if original_invite_name != given_invitite_name:
        raise Exception('Invalid inviteKey.')

    # If these validations pass, register the persona into our database.
    public_key = message_body.get(b'publicKey')

    Reader.check_persona_not_registred(public_key, nickname)

    new_identity = Identity(public_key)

    Writer.add_persona(
        pubkey=new_identity.pubkey,
        nickname=nickname
    )


def validate_invite(message_body):
    # Validate bootstrap node
    bootstrap_node = message_body.get(b'bootstrapNode')
    if bootstrap_node in (None, ''):
        raise Exception('Invalid bootstrapNode.')

    # Validate bootstrap address
    bootstrap_address = message_body.get(b'bootstrapAddr')
    if bootstrap_address in (None, ''):
        raise Exception('Invalid bootstrapAddr.')

    # Validate offering address
    offering_address = message_body.get(b'offeringAddr')
    if offering_address in (None, ''):
        raise Exception('Invalid offeringAddr.')

    # Validate service announcement message
    service_announcement_message = message_body.get(
        b'serviceAnnouncementMessage')
    if False and service_announcement_message in (None, ''):
        raise Exception('Invalid serviceAnnouncementMessage.')

    # Validate service offering id
    service_offering_id = message_body.get(b'serviceOfferingID')
    if service_offering_id in (None, ''):
        raise Exception('Invalid serviceOfferingID.')

    # Validate invite name
    invite_name_raw = message_body.get(b'inviteName')
    if invite_name_raw in (None, ''):
        raise Exception('Invalid inviteName.')
