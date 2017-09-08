from django.test import TestCase
from graphene.test import Client

from API.models import Invitation
from API.schema import schema

import base58
import json

from Test.identity_tools import Identity

class RegisterTestCase(TestCase):
  passphrase = "PeerMountain"
  identity = Identity()
  
  def setUp(self):
    self.client = Client(schema)
    invitation_context = self.identity.generate_invitation(self.passphrase)
    invitation = Invitation(
      content=invitation_context['content'],
      key=invitation_context['key']
    )
    invitation.save()
    self.token =  base58.b58encode(bytes(invitation.__str__().encode('utf8'))+b'.'+bytes(base58.b58encode(bytes(self.passphrase.encode('utf8'))).encode('utf8')))

  def test_valid_registration(self):
    message_content = {
      'token': self.token
    }

    message_envelope = {
      'sender': self.identity.address,
      'sender_pubkey': self.identity.pubkey,
      'sign': self.identity.sign(json.dumps(message_content, ensure_ascii=False))
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

  def test_invalid_sign(self):
    message_content = {
      'token': self.token
    }

    message_envelope = {
      'sender': self.identity.address,
      'sender_pubkey': self.identity.pubkey,
      'sign': self.identity.sign(json.dumps(message_content, ensure_ascii=False))+'.'
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
              'ok': False
            }
        }
    }

  def test_invalid_token(self):
    message_content = {
      'token': self.token+'1'
    }

    message_envelope = {
      'sender': self.identity.address,
      'sender_pubkey': self.identity.pubkey,
      'sign': self.identity.sign(json.dumps(message_content, ensure_ascii=False))
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
              'ok': False
            }
        }
    }

  def test_invalid_pubkey(self):
    message_content = {
      'token': self.token
    }

    message_envelope = {
      'sender': self.identity.address,
      'sender_pubkey': self.identity.pubkey+'.',
      'sign': self.identity.sign(json.dumps(message_content, ensure_ascii=False))
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
              'ok': False
            }
        }
    }

  def test_invalid_reuse_invitation(self):
    message_content = {
      'token': self.token
    }

    message_envelope = {
      'sender': self.identity.address,
      'sender_pubkey': self.identity.pubkey,
      'sign': self.identity.sign(json.dumps(message_content, ensure_ascii=False))
    }

    self.client.execute('''
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
              'ok': False
            }
        }
    }
