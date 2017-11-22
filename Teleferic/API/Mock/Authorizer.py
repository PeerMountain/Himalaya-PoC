import base64
import json
from Crypto.Hash import SHA256, HMAC

from libs.tools import Identity, AES
from . import Reader, Teleferic_Identity, Writer

from collections import OrderedDict
import msgpack


def validate_timestamped_signature(sender_pubkey, message_hash, signature):
  identity = Identity(sender_pubkey)
  
  sign = signature[b'signature']
  timestamp = signature[b'timestamp']
  
  validator_map = OrderedDict()
  validator_map['messageHash'] = message_hash
  validator_map['timestamp'] = timestamp
  
  validator = msgpack.packb(validator_map)

  if not identity.verify(validator,sign):
    raise Exception("Invalid sign")

def authorize_message(envelope):
    check_sender = True
    '''
    If message type is REGISTRATION
    and bodyType is REGISTRATION
    the sender should be new and his
    pubkey should not be present
  '''
    if envelope.get('messageType') is '1':
        try:
            public_cipher = AES('Peer Mountain')
            message = envelope.get('message').encode()
            message_content_raw = public_cipher.decrypt(message)
            # Parse message
            message_content = json.loads(message_content_raw.decode())
            if message_content.get('bodyType') == 1:
                check_sender = False
                message_body = json.loads(message_content.get('messageBody'))
                sender_pubkey = message_body.get('publicKey')
        except:
            pass

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

    # Validate ACL readers
    ACL = envelope.get('ACL')
    if ACL:
        for ACL_rule in ACL:
            # Rise an exception if some address be not registred
            Reader.get_pubkey(ACL_rule.get('reader'))
    else:
        # Validate Pulic Message
        # Decrypt
        public_cipher = AES('Peer Mountain')
        try:
            message_content_raw = public_cipher.decrypt(message)
            # Parse message
            message_content = json.loads(message_content_raw.decode())
        except Exception as e:
            raise Exception('Invalid public message content.')

        # Validate Body
        body_hash = envelope.get('bodyHash')
        message_body_raw = message_content.get('messageBody').encode()
        current_body_hash = SHA256.new(message_body_raw).hexdigest()
        if body_hash != current_body_hash:
            raise Exception('Invalid bodyHash.')

        # Validate dossierSalt
        dossier_salt = message_content.get('dossierSalt').encode()
        if len(dossier_salt) != 40:
            raise Exception('Invalid dossierSalt.')

        # Validate dossierHash
        dossier_hash = envelope.get('dossierHash')
        if dossier_hash != HMAC.new(dossier_salt, message_body_raw, SHA256).hexdigest():
            raise Exception('Invalid dossierHash.')

        # Parse message body
        try:
            message_body = json.loads(message_body_raw.decode())
        except Exception as e:
            raise Exception('Invalid messageBody.')

        {
            0: validate_invite,
            1: validate_registration
        }.get(message_content.get('bodyType'))(message_body)

    return True


def validate_registration(message_body):
    # Validate bootstrap node
    invite_message_hash = message_body.get('inviteMsgID')
    if invite_message_hash in (None, ''):
        raise Exception('Invalid invite message hash.')

    nickname = message_body.get('publicNickname')
    if nickname in (None, ''):
        raise Exception('Invalid nickname.')

    invite_message = Reader.get_message_content(invite_message_hash)
    public_cipher = AES('Peer Mountain')
    try:
        invite_message_content_raw = public_cipher.decrypt(invite_message)
        # Parse message
        invite_message_content = json.loads(
            invite_message_content_raw.decode())
        invite_message_body_content = json.loads(
            invite_message_content.get('messageBody'))
    except Exception as e:
        raise Exception('Invalid invite message content.')

    key_proof_raw = message_body.get('keyProof')
    print(key_proof_raw)
    try:
        key_proof = Teleferic_Identity.decrypt_content(key_proof_raw.encode())
    except Exception as e:
        raise Exception('Invalid keyProof1.')
    if key_proof == None:
        raise Exception('Invalid keyProof.2')

    decoder = AES(key_proof.decode())

    original_invite_name_raw = invite_message_body_content.get('inviteName')
    original_invite_name = decoder.decrypt(original_invite_name_raw)

    given_invitite_name_raw = message_body.get('inviteName')
    given_invitite_name = Teleferic_Identity.decrypt_content(
        given_invitite_name_raw)

    if original_invite_name != given_invitite_name:
        raise Exception('Invalid inviteKey.')

    public_key = message_body.get('publicKey')

    Reader.check_persona_not_registred(public_key, nickname)

    new_identity = Identity(public_key)

    Writer.add_persona(
        pubkey=new_identity.pubkey,
        nickname=nickname
    )


def validate_invite(message_body):
    # Validate bootstrap node
    bootstrap_node = message_body.get('bootstrapNode')
    if bootstrap_node in (None, ''):
        raise Exception('Invalid bootstrapNode.')

    # Validate bootstrap address
    bootstrap_address = message_body.get('bootstrapAddr')
    if bootstrap_address in (None, ''):
        raise Exception('Invalid bootstrapAddr.')

    # Validate offering address
    offering_address = message_body.get('offeringAddr')
    if offering_address in (None, ''):
        raise Exception('Invalid offeringAddr.')

    # Validate service announcement message
    service_announcement_message = message_body.get(
        'serviceAnnouncementMessage')
    if service_announcement_message in (None, ''):
        raise Exception('Invalid serviceAnnouncementMessage.')

    # Validate service offering id
    service_offering_id = message_body.get('serviceOfferingID')
    if service_offering_id in (None, ''):
        raise Exception('Invalid serviceOfferingID.')

    # Validate invite name
    invite_name_raw = message_body.get('inviteName')
    if invite_name_raw in (None, ''):
        raise Exception('Invalid inviteName.')
