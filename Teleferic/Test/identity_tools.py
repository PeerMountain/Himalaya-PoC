from Crypto.Hash import RIPEMD, SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import base58
import six

from settings import ADDRESS_PREFIX

class Identity():
  def __init__(self):
    rng = Random.new().read
    self.key = RSA.generate(4096, rng)

  @property
  def address(self):
    #The public key of the pair is hashed SHA-256.
    step_1 = SHA256.new(self.key.exportKey()).digest()
    #The resulting Hash is further hashed with RIPEMD-160.
    step_2 = RIPEMD.new(step_1).digest()
    #Two bytes are prefixed to the resulting RIPEMD-160 hash in order to identify the deployment system.
    step_3 = bytes(ADDRESS_PREFIX)+step_2
    #A checksum is calculated by SHA-256 hashing the extended RIPEMD-160 hash, then hashing
    #the resulting hash once more.
    step_4_checksum = SHA256.new(SHA256.new(step_3).digest()).digest()
    #The last 4 bytes of the final hash are added as the 
    #trailing 4 bytes of the extended RIPEMD-160 hash. This is the checksum
    step_4 = step_3 + step_4_checksum[4:]
    #The resulting object is Base58 encoded
    return base58.b58encode(step_4)

  @property
  def pubkey(self):
    return base58.b58encode(self.key.publickey().exportKey("DER"))

  def export_private(self,passphrase):
    return self.key.exportKey(passphrase=passphrase, pkcs=8)

  def sign(self, content):
    hash_message = RIPEMD.new(content).digest()
    rng = Random.new().read
    signature = self.key.sign(hash_message, rng)
    return base58.b58encode_int(signature[0])

  def verify(self, content, signature):
    hash_message = RIPEMD.new(content).digest()
    result = self.key.verify(hash_message, (base58.b58encode_int(signature),))
    return result == 1

  def generate_invitation(self,passphrase):
    rng = Random.new().read
    invite_keypair = RSA.generate(4096, rng)
    invitation_content = invite_keypair.encrypt(self._to_format_for_encrypt(passphrase),32)
    invitation_key = invite_keypair.exportKey('PEM',passphrase=passphrase)
    return {
      'content': base58.b58encode(invitation_content[0]),
      'key': base58.b58encode(invitation_key)
    }
    '''
      {
        'content': '2bSv8NMmkmJB9PeiAAVSnbwaQTvifiuwr6cXHZbJog8zyz9qJ2ZeAQKafYkVsc5vBp4dcHvy9vNFNM2YEzQvY4j4BxizeuXhvnnWw9ydBcXxwQF6H1xBjNvc9fjYW3Pj9o3CEaEGsTHEZWBpruv8Bx9hBcJDJvuaDJLuvDFNe4A9LQMMr1MKANDML271VLpKh6tBQq9MLkLVumNRv4wUKNpW9jyecgLv961gPYGcnLRmiDcTvm9yDhrTyg6v7RRbLXb7VnkDHBabAmw4hnUeKLAuuJ9FCb9yH3PGJD3BGdd6We2oiYymtHYKaVG28FzLmJr31HYkGjiPnN27RCHyWtjKBaSpyCutLhYEuaqcs97Zzp5i78dXo5grSxSGxiFS2U68NgHwAZzgenJ9FRu2c5wwpT8xN9BTmCHArZ1NvFcLLdN3xMsPhkViqnC7oJgmMk54hDSK62m4HABGPxYzoiKP91p9M1qq5gUubrWnadFApC9mBcQhjZu1pXkBhZ37USppkScNbYJNMXv1ZZJ4dw2US53dQYyNvitDe9DcCpmAY8Tbfe299hLuErFkPWsR6QvNGett66S1XZ77k6Ba8en4q7wEECKCuDHicbLV5K23tYhSpdxGS6jPQSs6tKb67zChCuipcfLQK7SRNspMs7Ejjj8RE97vttCw5fp8UbuVVrvXD6Ebb5q9Z5ev',
        'key': '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',
        'token': 'Z7TNmCqMrzkWwvkrE7x7Lm51KMmypHaxbgNxziJCv3qK3hb2QB7dz'
      }
    '''

  def _to_format_for_encrypt(self, value):
    if isinstance(value, int):
      return six.binary_type(value)
    for str_type in six.string_types:
      if isinstance(value, str_type):
        return value.encode('utf8')
    if isinstance(value, six.binary_type):
      return value