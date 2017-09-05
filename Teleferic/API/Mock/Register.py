import base58
from Crypto.PublicKey import RSA
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
    if(key_pair.decrypt(invitation_content).decode() == invitation_passphrase):
      invitation.used = True
      invitation.save()
      registration = Registration(
        invitation=invitation,
        address=address,
        pubkey= pubkey,
      )
      registration.save()
      return registration.__str__()
  except:
    pass
    return False