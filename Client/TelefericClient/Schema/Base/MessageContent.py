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
    """MessageContent
    
    Helper class for message encryption.
    """

    content = OrderedDict()

    def __init__(self, message_type, message_body, service_id=None, consumer_id=None, signature=None, encrypt=True):
        """__init__

        Create a MessageContent object and prepare the content for encryption.

        :param message_type: string: Type of the message, see AVAILABLE_TYPES
        :param message_body: MessageBody: Instance containing the message body data.
        :param service_id:
        :param consumer_id:
        :param signature:
        :param encrypt:
        """

        # if not message_type in AVAILABLE_TYPES:
        #     raise Exception(
        #         'Message type should be [%s].' % '|'.join(AVAILABLE_TYPES))

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
        self.passphrase = self.nonce = None
        if encrypt:
            self.nonce = bytes(random.randint(0, 255) for _ in range(16))

        self.encrypt = encrypt

    def generate_dossier_salt(self):
        """generate_dossier_salt

        Generates a salt to be used for hashing and eventually verificating
        the message.
        """
        salt = bytes(bytearray(random.getrandbits(8) for _ in range(40)))
        return base64.b64encode(salt)

    def pack(self):
        """pack
        
        Returns the message content as a MessagePack byte array.
        """
        return msgpack.packb(self.content)

    def build(self, passphrase):
        """build

        Encrypts the message's contents (if needed) and generates the various hashes
        that will be used for verification.

        :param passphrase: string: Key to be used in the message's AES encryption.
        :param nonce: Nonce to be used when encrypting the data.
        """
        self.passphrase = passphrase
        self.content['messageBody'] = self.body.build()
        cipher = AES(passphrase)
        pack = self.pack()
        build = cipher.encrypt(pack) if self.encrypt else base64.b64encode(pack)
        # Calculate hashes
        self.hash = base64.b64encode(SHA256.new(build).digest()).decode()
        salt = base64.b64decode(self.content['dossierSalt'])
        self.hmac = base64.b64encode(HMAC.new(
            salt, pack, SHA256).digest()).decode()
        return build.decode()
