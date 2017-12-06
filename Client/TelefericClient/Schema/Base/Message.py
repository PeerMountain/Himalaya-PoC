import msgpack
import base64

from collections import OrderedDict

from TelefericClient.Cryptography import RSA


class Message():

    def __init__(self, message_content, passphrase='Peer Mountain', readers=None):
        self.message_content = message_content
        self.passphrase = passphrase
        self.readers = readers

    def build(self, identity, bootstrap_node):
        build_content = self.message_content.build(self.passphrase)
        content = {
            'sender': identity.address,
            'messageSig': identity.sign_message(self.message_content.hash,bootstrap_node),
            'messageType': self.message_content.type,
            'messageHash': self.message_content.hash,
            'dossierHash': self.message_content.hmac,
            'bodyHash': self.message_content.body.hash,
            'message': build_content
        }
        return content
