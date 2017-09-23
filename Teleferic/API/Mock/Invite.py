import base58
from Crypto.PublicKey import RSA
from API.models import Invitation

from .Register import execute_get_pubkey


def execute_invite(message_content,message_key,sender):
  invitation = Invitation(
    content=message_content,
    key=message_key,
    sender=sender
  )
  invitation.save()
  return invitation.__str__()