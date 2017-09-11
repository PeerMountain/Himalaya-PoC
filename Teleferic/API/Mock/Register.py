import base58
from Crypto.Hash import RIPEMD
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from API.models import Invitation, Registration
def execute_register(token, address, pubkey):
  try:
    invitation_context = base58.b58decode(token).decode().split('.')
    invitation_hash = invitation_context[0]
    invitation_passphrase = base58.b58decode(invitation_context[1]).decode() 
    invitation = Invitation.objects.get(pk=invitation_hash)
    if(invitation.used == True):
      return False
    invitation_key = base58.b58decode(invitation.key)
    invitation_content = base58.b58decode(invitation.content)
    invitation_key = base58.b58decode(invitation.key)
    key_pair = RSA.importKey(invitation_key,passphrase=invitation_passphrase)

    dsize = RIPEMD.digest_size
    sentinel = str(Random.new().read(15+dsize))
    cipher = PKCS1_v1_5.new(key_pair)
    message = cipher.decrypt(invitation_content, sentinel)
    digest = RIPEMD.new(message[:-dsize]).digest()
    
    if digest==message[-dsize:]:
      invitation.used = True
      invitation.save()
      registration = Registration(
        invitation=invitation,
        address=address,
        pubkey= pubkey
      )
      registration.save()
      return registration.__str__()
  except:
    return False

def execute_get_pubkey(address):
  registration = Registration.objects.filter(address=address).first()

  if registration == None:
    return False

  return registration.pubkey
