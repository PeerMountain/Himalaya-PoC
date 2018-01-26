from Crypto.Hash import RIPEMD, SHA256
from Crypto.PublicKey import RSA as Key
from Crypto.PublicKey.RSA import _RSAobj
from Crypto import Random
import base58
import base64
import msgpack

from collections import OrderedDict

from .Cryptography import RSA
ADDRESS_PREFIX = [1, 0]


class Identity():
    """Identity

    Helper class for encrypting and signing messages.
    """

    def __init__(self, key=None, prefix=ADDRESS_PREFIX):
        """__init__

        Create a new Identity using a given key,
        or generate a key in the spot.

        :param key: RSA key.
        :param prefix:
        """
        if key is None:
            rng = Random.new().read
            self.key = Key.generate(4096, rng)
        else:
            key_type = type(key)
            if key_type in (str, bytes):
                self.key = Key.importKey(key.strip())
            elif key_type == _RSAobj:
                self.key = key
            else:
                raise Exception('Invalid key format.')
        
        if self.key.size() < 4095:
            raise Exception('4096 is the minimun key size')
        
        if not len(prefix) is len(ADDRESS_PREFIX):
            raise Exception('Invalid address prefix')

        for index, value in enumerate(prefix):
            if not value is ADDRESS_PREFIX[index]:
                raise Exception('Invalid address prefix')

        self.prefix = prefix
        self.rsa = RSA(self.key)

    @property
    def address(self):
        """address
        
        Property which returns this Identity's platform address.
        """
        # The public key of the pair is hashed SHA-256.
        step_1 = SHA256.new(self.key.publickey().exportKey()).digest()
        # The resulting Hash is further hashed with RIPEMD-160.
        step_2 = RIPEMD.new(step_1).digest()
        # Two bytes are prefixed to the resulting RIPEMD-160 hash in order to
        # identify the deployment system.
        step_3 = bytes(self.prefix) + step_2
        # A checksum is calculated by SHA-256 hashing the extended RIPEMD-160 hash, then hashing
        # the resulting hash once more.
        step_4_checksum = SHA256.new(SHA256.new(step_3).digest()).digest()
        # The last 4 bytes of the final hash are added as the
        # trailing 4 bytes of the extended RIPEMD-160 hash. This is the
        # checksum
        step_4 = step_3 + step_4_checksum[4:]
        # The resulting object is Base58 encoded
        return base58.b58encode(step_4)

    @property
    def pubkey(self):
        return self.key.publickey().exportKey("PEM")

    @property
    def privkey(self):
        if self.key.has_private:
            return self.key.exportKey("PEM")
        else:
            return False

    def export_private(self, passphrase):
        if self.key.has_private:
            return self.key.exportKey(passphrase=passphrase, pkcs=8)
        else:
            return False

    def sign(self, content):
        if self.key.has_private:
            return self.rsa.sign(content)
        else:
            return False

    def verify(self, content, signature):
        return self.rsa.verify(content, signature)

    def encrypt(self, content):
        return self.rsa.encrypt(content)

    def decrypt(self, content):
        if self.key.has_private:
            return self.rsa.decrypt(content)
        else:
            return False
    
    def sign_dict(self, content, client):
        """sign_dict

        Sign bytes to be sent to Teleferic.

        This requires using a timestamp signed by Teleferic, so the API is called.

        :param content: Dict content.
        :param client: Teleferic API client.
        """
        content = msgpack.packb(content)
        return self.sign_bytes(content,client)

    def sign_bytes(self, content, client):
        """sign_bytes

        Sign bytes to be sent to Teleferic.

        This requires using a timestamp signed by Teleferic, so the API is called.

        :param content: Bytes content.
        :param client: Teleferic API client.
        """
        content_hash = base64.b64encode(
            SHA256.new(content).digest()
        ).decode()
        
        node_signed_timestamp = client.get_node_signedtimestamp()

        signable_object = OrderedDict()
        signable_object['messageHash'] = content_hash
        signable_object['timestamp'] = node_signed_timestamp
        
        signable_object = msgpack.packb(signable_object)

        return base64.b64encode(msgpack.packb({
            'signature': self.sign(signable_object),
            'timestamp': node_signed_timestamp
        })).decode()

    def sign_message(self, message_hash, client):
        """sign_message

        Sign a message to be sent to Teleferic.

        This requires using a timestamp signed by Teleferic, so the API is called.

        :param message_hash: Hash of the message content.
        :param client: Teleferic API client.
        """
        if type(message_hash) is str:
            message_hash = message_hash.encode()

        node_signed_timestamp = client.get_node_signedtimestamp()

        signable_object = OrderedDict()
        signable_object['messageHash'] = message_hash
        signable_object['timestamp'] = node_signed_timestamp
        
        signable_object = msgpack.packb(signable_object)

        return base64.b64encode(msgpack.packb({
            'signature': self.sign(signable_object),
            'timestamp': node_signed_timestamp
        })).decode()
