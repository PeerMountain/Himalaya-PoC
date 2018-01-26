import msgpack
import base64

from collections import OrderedDict

from TelefericClient.Cryptography import RSA

from Crypto.Hash import SHA256

class Message():
    """Message

    A Teleferic Message.
    """

    def __init__(self, message_content, passphrase='Peer Mountain', readers=None, objects=tuple()):
        """__init__

        Create a message envelope.

        :param message_content: MessageContent: message content data.
        :param passphrase: string: Passphrase used to encrypt message_content.
        :param readers: array: Identities allowed to read the message.
        """
        self.message_content = message_content
        self.passphrase = passphrase
        self.readers = readers
        self.objects = objects

    def build(self, identity, client):
        """build

        Generate a dictionary containing the data to be sent to Teleferic

        :param identity: Identity: identity of the sender.
        :param client: Teleferic API client.
        """
        if not isinstance(self.passphrase, bytes):
            self.passphrase = self.passphrase.encode()
        build_content = self.message_content.build(self.passphrase)
        content = {
            'sender': identity.address,
            'messageSig': identity.sign_message(self.message_content.hash,client),
            'messageType': self.message_content.type,
            'messageHash': self.message_content.hash,
            'dossierHash': self.message_content.hmac,
            'bodyHash': self.message_content.body.hash,
            'message': build_content,
            'objects': self.objects,
        }
        if not self.readers is None:
            content['ACL'] = [
                {
                    'reader': reader.address,
                    'key': RSA(reader.pubkey).encrypt(self.passphrase).decode()
                } for reader in self.readers
            ]
        return content
