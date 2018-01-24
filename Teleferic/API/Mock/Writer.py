import base58
from Crypto.Hash import RIPEMD, SHA256
from Crypto.PublicKey import RSA
from API.models import Message, Persona, ACLRule, SaltedMetaHash
from . import Reader
from libs.tools import Identity
import time
import os
import base64
import base58

from .utils import get_container_path, get_message_path, encode_hash, encode_dict


def add_persona(pubkey, nickname):
    identity = Identity(pubkey)

    persona = Persona(
        address=identity.address,
        pubkey=identity.pubkey,
        nickname=nickname
    )

    persona.save()

    return persona


def write_message(envelope):
    message = Message(
        messageSig=encode_dict(envelope.get('messageSig')),
        messageHash=encode_hash(envelope.get('messageHash')),
        messageType=envelope.get('messageType'),
        dossierHash=encode_hash(envelope.get('dossierHash')),
        bodyHash=encode_hash(envelope.get('bodyHash')),
        sender=Persona.objects.get(pk=envelope.get('sender')),
        messagePath=store_message(envelope.get(
            'message'), envelope.get('messageHash'))
    )
    message.save()

    acls = envelope.get('ACL')
    if not acls is None:
        for acl in acls:
            acl_rule = ACLRule.objects.create(**{
                'reader': Reader.get_persona(address=acl.get('reader')),
                'key': acl.get('key'),
                'message': message
            })
            acl_rule.save()
 
    containers = envelope.get('containers')
    if not containers is None:
        for _container in containers:
            object_hash = encode_hash(_container.get('objectHash'))
            salted_meta_hashes = _container.pop('saltedMetaHashes')
            _object = message._objects.create(objectHash= object_hash)

            import pdb; pdb.set_trace()
            if not _container.get('objectContainer') is None:
                object_container = _container.pop('objectContainer')
                container_hash = encode_hash(_container.get('containerHash'))
                _container['containerHash'] = container_hash
                
                object_container_path = store_container(object_container, container_hash)

                _container['objectContainerPath'] = object_container_path
                
                container_signature = encode_dict(_container.get('containerSig'))
                _container['containerSig'] = container_signature
                
                _object.container.create(
                    containerHash= container_hash,
                    containerSig= container_signature,
                    objectContainerPath= object_container_path
                )

            for salted_meta_hash in salted_meta_hashes:
                salted_meta_hash = encode_hash(salted_meta_hash)
                
                _object.saltedMetaHashes.create(**{
                    'saltedMetaHash': salted_meta_hash
                })

    return {
        "envelopeID": message.pk.decode('utf-8'),
        "cacheTXID": message.pk.decode('utf-8'),
        "cacheTimestamp": time.time(),
        "messageHash": SHA256.new(envelope.get('message').encode()).digest()
    }


def store(content, path):
    _file = open(path, 'w+')
    _file.write(content)
    _file.close()
    return path


def store_message(message, messageHash):
    return store(message, get_message_path(messageHash))


def store_container(container, containerHash):
    import pdb; pdb.set_trace()
    return store(container, get_container_path(containerHash))
