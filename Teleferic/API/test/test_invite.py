from django.test import TestCase
from django.test import Client

from API.models import Invitation
from API.schema import schema

import base58
import json

from Playground.identity_tools import Identity

class InviteTestCase(TestCase):
  passphrase = "PeerMountain"

  def setUp(self):
    '''
    Genesis Invite
    '''
    self.client = Client()
    self.main_identity = Identity()
    identity = Identity()
    invitation_context = identity.generate_invitation(self.passphrase)
    invitation = Invitation(
      content=invitation_context['content'],
      key=invitation_context['key']
    )
    invitation.save()
    token = base58.b58encode(bytes(invitation.__str__().encode('utf8'))+b'.'+bytes(base58.b58encode(bytes(self.passphrase.encode('utf8'))).encode('utf8')))
    self.register(token)

  def register(self,token):
    message_content = {
      'token': token
    }

    message_envelope = {
      'sender': self.main_identity.address,
      'sender_pubkey': self.main_identity.pubkey,
    }
    
    message_raw = {}
    message_raw.update(message_content)
    message_raw.update(message_envelope)
    message = json.dumps(message_raw)

    query = '''
        mutation register(
          $token: String!
          $sender: String!
          $sender_pubkey: String! 
        ){
          register(
            envelope: {
              sender: $sender
              pubkey: $sender_pubkey
            }
            message: {
              token: $token
            }
          ) {
            ok
          }
        }
      '''
    response_raw = self.client.post('/teleferic', {
      'query': query, 
      'variables': message,
      'sign': self.main_identity.sign(query+message)
    })

  def test_create_invite(self):
    invite = self.main_identity.generate_invitation(self.passphrase)

    message_content = {
      'content': invite.get('content'),
      'key': invite.get('key')
    }

    message_envelope = {
      'sender': self.main_identity.address,
    }

    message_raw = {}
    message_raw.update(message_content)
    message_raw.update(message_envelope)
    message = json.dumps(message_raw)

    query = '''
        mutation invite(
          $content: String!
          $key: String!
          $sender: String!
        ){
          invite(
            envelope: {
              sender: $sender
            }
            message: {
              content: $content
              key: $key
            }
          ) {
            ok
          }
        }
      '''
    
    response_raw = self.client.post('/teleferic', {
      'query': query, 
      'variables': message,
      'sign': self.main_identity.sign(query+message)
    })

    assert response_raw.status_code == 200

    response = response_raw.json()

    assert response == {
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
    }

    message_raw = {}
    message_raw.update(message_content)
    message_raw.update(message_envelope)
    message = json.dumps(message_raw)

    query = '''
        mutation invite(
          $content: String!
          $key: String!
          $sender: String!
        ){
          invite(
            envelope: {
              sender: $sender
            }
            message: {
              content: $content
              key: $key
            }
          ) {
            ok
          }
        }
      '''

    response_raw = self.client.post('/teleferic', {
      'query': query, 
      'variables': message,
      'sign': self.main_identity.sign(query+message)
    })

    assert response_raw.status_code == 200

    response = response_raw.json()

    assert response == {
        'data': {
            'invite': {'ok':False}
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
    }

    message_raw = {}
    message_raw.update(message_content)
    message_raw.update(message_envelope)
    message = json.dumps(message_raw)

    query = '''
        mutation invite(
          $content: String!
          $key: String!
          $sender: String!
        ){
          invite(
            envelope: {
              sender: $sender
            }
            message: {
              content: $content
              key: $key
            }
          ) {
            ok
          }
        }
      '''

    response_raw = self.client.post('/teleferic', {
      'query': query, 
      'variables': message,
      'sign': self.main_identity.sign(query+message+'a')
    })
    assert response_raw.status_code == 200

    response = response_raw.json()

    assert response == {
        'data': {
            'invite': {'ok':False}
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
    }

    message_raw = {}
    message_raw.update(message_content)
    message_raw.update(message_envelope)
    message = json.dumps(message_raw)

    query = '''
        mutation invite(
          $content: String!
          $key: String!
          $sender: String!
        ){
          invite(
            envelope: {
              sender: $sender
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
      '''

    response_raw = self.client.post('/teleferic', {
      'query': query, 
      'variables': message,
      'sign': self.main_identity.sign(query+message)
    })
    assert response_raw.status_code == 200

    response = response_raw.json()

    token =  base58.b58encode(bytes(response.get('data').get('invite').get('id').encode('utf8'))+b'.'+bytes(base58.b58encode(bytes(self.passphrase.encode('utf8'))).encode('utf8')))
    
    message_content = {
      'token': token
    }

    identity = Identity()

    message_envelope = {
      'sender': identity.address,
      'sender_pubkey': identity.pubkey
    }

    message_raw = {}
    message_raw.update(message_content)
    message_raw.update(message_envelope)
    message = json.dumps(message_raw)

    query = '''
        mutation register(
          $token: String!
          $sender: String!
          $sender_pubkey: String!
        ){
          register(
            envelope: {
              sender: $sender
              pubkey: $sender_pubkey
            }
            message: {
              token: $token
            }
          ) {
            ok
          }
        }
      '''

    response_raw = self.client.post('/teleferic', {
      'query': query, 
      'variables': message,
      'sign': identity.sign(query+message)
    })
    assert response_raw.status_code == 200

    response = response_raw.json()

    assert response == {
        'data': {
            'register': {
              'ok': True
            }
        }
    }