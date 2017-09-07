from django.test import TestCase
from graphene.test import Client

from API.models import Invitation
from API.schema import schema

import base58
import json

from Test.identity_tools import Identity

class InviteTestCase(TestCase):
  passphrase = "PeerMountain"

  def setUp(self):
    '''
    Genesis Invite
    '''
    self.client = Client(schema)
    self.main_identity = Identity()
    identity = Identity()
    invitation_context = identity.generate_invitation(self.passphrase)
    invitation = Invitation(
      content=invitation_context['content'],
      key=invitation_context['key']
    )
    invitation.save()
    token =  base58.b58encode(bytes(invitation.__str__().encode('utf8'))+b'.'+bytes(base58.b58encode(bytes(self.passphrase.encode('utf8'))).encode('utf8')))
    self.register(token)

  def register(self,token):
    message_content = {
      'token': token
    }

    message_envelope = {
      'sender': self.main_identity.address,
      'sender_pubkey': self.main_identity.pubkey,
      'sign': self.main_identity.sign(json.dumps(message_content))
    }
    
    executed = self.client.execute('''
        mutation register(
          $token: String!
          $sender: String!
          $sender_pubkey: String!
          $sign: String! 
        ){
          register(
            envelope: {
              sender: $sender
              pubkey: $sender_pubkey
              sign: $sign
            }
            message: {
              token: $token
            }
          ) {
            ok
          }
        }
      ''',
      variable_values={**message_content, **message_envelope}
    )

  def test_create_invite(self):
    invite = self.main_identity.generate_invitation(self.passphrase)

    message_content = {
      'content': invite.get('content'),
      'key': invite.get('key')
    }

    message_envelope = {
      'sender': self.main_identity.address,
      'sign': self.main_identity.sign(json.dumps(message_content))
    }

    executed = self.client.execute('''
        mutation invite(
          $content: String!
          $key: String!
          $sender: String!
          $sign: String! 
        ){
          invite(
            envelope: {
              sender: $sender
              sign: $sign
            }
            message: {
              content: $content
              key: $key
            }
          ) {
            ok
          }
        }
      ''',
      variable_values={**message_content, **message_envelope}
    )

    assert executed == {
        'data': {
            'invite': {
              'ok': True
            }
        }
    }

  def test_create_invite_invalid_sender(self):
    invite = self.main_identity.generate_invitation(self.passphrase)

    message_content = {
      'content': invite.get('content'),
      'key': invite.get('key')
    }

    message_envelope = {
      'sender': self.main_identity.address+'1',
      'sign': self.main_identity.sign(json.dumps(message_content))
    }

    executed = self.client.execute('''
        mutation invite(
          $content: String!
          $key: String!
          $sender: String!
          $sign: String! 
        ){
          invite(
            envelope: {
              sender: $sender
              sign: $sign
            }
            message: {
              content: $content
              key: $key
            }
          ) {
            ok
          }
        }
      ''',
      variable_values={**message_content, **message_envelope}
    )

    assert executed == {
        'data': {
            'invite': {
              'ok': False
            }
        }
    }

  def test_create_invite_invalid_sign(self):
    invite = self.main_identity.generate_invitation(self.passphrase)

    message_content = {
      'content': invite.get('content'),
      'key': invite.get('key')
    }

    message_envelope = {
      'sender': self.main_identity.address,
      'sign': self.main_identity.sign(json.dumps(message_content))[3:]
    }

    executed = self.client.execute('''
        mutation invite(
          $content: String!
          $key: String!
          $sender: String!
          $sign: String! 
        ){
          invite(
            envelope: {
              sender: $sender
              sign: $sign
            }
            message: {
              content: $content
              key: $key
            }
          ) {
            ok
          }
        }
      ''',
      variable_values={**message_content, **message_envelope}
    )

    assert executed == {
        'data': {
            'invite': {
              'ok': False
            }
        }
    }

  def test_valid_registration(self):
    invite = self.main_identity.generate_invitation(self.passphrase)

    message_content = {
      'content': invite.get('content'),
      'key': invite.get('key')
    }

    message_envelope = {
      'sender': self.main_identity.address,
      'sign': self.main_identity.sign(json.dumps(message_content))
    }

    invite_executed = self.client.execute('''
        mutation invite(
          $content: String!
          $key: String!
          $sender: String!
          $sign: String! 
        ){
          invite(
            envelope: {
              sender: $sender
              sign: $sign
            }
            message: {
              content: $content
              key: $key
            }
          ) {
            ok
            id
          }
        }
      ''',
      variable_values={**message_content, **message_envelope}
    )

    token =  base58.b58encode(bytes(invite_executed.get('data').get('invite').get('id').encode('utf8'))+b'.'+bytes(base58.b58encode(bytes(self.passphrase.encode('utf8'))).encode('utf8')))
    
    message_content = {
      'token': token
    }

    identity = Identity()

    message_envelope = {
      'sender': identity.address,
      'sender_pubkey': identity.pubkey,
      'sign': identity.sign(json.dumps(message_content, ensure_ascii=False))
    }

    executed = self.client.execute('''
        mutation register(
          $token: String!
          $sender: String!
          $sender_pubkey: String!
          $sign: String! 
        ){
          register(
            envelope: {
              sender: $sender
              pubkey: $sender_pubkey
              sign: $sign
            }
            message: {
              token: $token
            }
          ) {
            ok
          }
        }
      ''',
      variable_values={**message_content, **message_envelope}
    )

    assert executed == {
        'data': {
            'register': {
              'ok': True
            }
        }
    }