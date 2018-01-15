import base58
import base64
from Crypto.Hash import RIPEMD, SHA256
from Crypto.PublicKey import RSA
from API.models import Persona, Message, Container
from libs.tools import Identity
import os
from API.Mock.utils import get_container_path, get_message_path, encode_hash 


def get_persona(address=None, nickname=None, pubkey=None):

    if address != None:
        persona = Persona.objects.get(pk=address)
    elif nickname != None:
        persona = Persona.objects.get(nickname=nickname)
    elif pubkey != None:
        persona = Persona.objects.get(pubkey=pubkey)
    else:
        raise Exception('Define one filter')

    if not persona:
        raise Exception('Invalid filter')

    return persona


def check_persona_not_registred(pubkey, nickname):
    persona = Identity(pubkey)

    existent_identity = Persona.objects.filter(address=persona.address).first()
    if existent_identity is not None:
        raise Exception('Address already registred.')

    existent_identity = Persona.objects.filter(pubkey=persona.pubkey).first()
    if existent_identity is not None:
        raise Exception('Pubkey already registred.')

    existent_identity = Persona.objects.filter(nickname=nickname).first()
    if existent_identity is not None:
        raise Exception('Nickname already registred.')

    return True


def get_message_content(message_hash):
    message_path = get_message_path(message_hash)
    message = open(message_path, 'r')
    content = message.read()
    return content

def get_container_content(container_hash):
    container_path = get_message_path(container_hash)
    container = open(container_path, 'r')
    content = container.read()
    return content

def get_message(_hash):
    return Message.objects.get(messageHash=_hash)

def get_message_by_date(_date):
    return Message.objects.filter(createdAt=_date)

def get_message_by_reader(_reader):
    return Message.objects.filter(acl__reader=_reader)

def get_container(_hash):
    return Container.objects.get(containerHash=_hash)

def get_message_existance(message_hash):
    message_path = get_message_path(message_hash)
    return os.path.isfile(message_path)
