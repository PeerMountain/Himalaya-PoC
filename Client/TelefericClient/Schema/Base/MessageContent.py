import msgpack
import base64
import random

from Crypto.Hash import HMAC, SHA256

from collections import OrderedDict

from TelefericClient.Cryptography import AES

AVAILABLE_TYPES = [
    'REGISTRATION'
]


class MessageContent():

    content = OrderedDict()

    def __init__(self, message_type, message_body, service_id=None, consumer_id=None, signature=None):

        if not message_type in AVAILABLE_TYPES:
            raise Exception(
                'Message type should be [%s].' % '|'.join(AVAILABLE_TYPES))

        self.type = message_type
        self.body = message_body

        self.content['bodyType'] = message_body.type

        # Optionals
        if not service_id is None:
            self.content['serviceID'] = service_id
        if not consumer_id is None:
            self.content['consumerID'] = consumer_id
        if not signature is None:
            self.content['signature'] = signature

        self.content['dossierSalt'] = self.generate_dossier_salt()
        self.content['messageBody'] = self.body.build()

    def generate_dossier_salt(self):
        salt = bytes(bytearray(random.getrandbits(8) for _ in range(40)))
        return salt

    def pack(self):
        return msgpack.packb(self.content)

    def build(self, passphrase):
        cipher = AES(passphrase)
        build = cipher.encrypt(self.pack())
        self.hash = base64.b64encode(SHA256.new(build).digest()).decode()
        self.hmac = base64.b64encode(HMAC.new(
            self.content['dossierSalt'], self.content['messageBody'].encode(), SHA256).digest()).decode()
        return build.decode()
