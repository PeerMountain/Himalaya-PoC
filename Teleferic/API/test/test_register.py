from django.test import TestCase
from django.test import Client

from API.models import Invitation
from API.schema import schema

import base58
import json

from Playground.identity_tools import Identity

class RegisterTestCase(TestCase):
  passphrase = "PeerMountain"
  identity = Identity()
  
  def setUp(self):
    self.client = Client()
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

    response_raw = self.client.post('/graphql', {
      'query': query, 
      'variables': message,
      'sign': self.identity.sign(query+message)
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

  def test_invalid_sign(self):
    message_content = {
      'token': self.token
    }

    message_envelope = {
      'sender': self.identity.address,
      'sender_pubkey': self.identity.pubkey,
    }

    message_raw = {}
    message_raw.update(message_content)
    message_raw.update(message_envelope)
    message = json.dumps(message_raw)
    message_raw['token'] = message_raw['token'] + 'a'
    message_modified = json.dumps(message_raw)

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
    response_raw = self.client.post('/graphql', {
      'query': query, 
      'variables': message_modified,
      'sign': self.identity.sign(query+message)
    })
    assert response_raw.status_code == 200

    response = response_raw.json()

    assert response == {
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

    response_raw = self.client.post('/graphql', {
      'query': query, 
      'variables': message,
      'sign': self.identity.sign(query+message)
    })
    assert response_raw.status_code == 200

    response = response_raw.json()
    
    assert response == {
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
      'sender_pubkey': self.identity.pubkey+'.'
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
    
    response_raw = self.client.post('/graphql', {
      'query': query, 
      'variables': message,
      'sign': self.identity.sign(query+message)
    })
    assert response_raw.status_code == 200

    response = response_raw.json()

    assert response == {
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

    self.client.post('/graphql', {
      'query': query, 
      'variables': message,
      'sign': self.identity.sign(query+message)
    })

    response_raw = self.client.post('/graphql', {
      'query': query, 
      'variables': message,
      'sign': self.identity.sign(query+message)
    })
    assert response_raw.status_code == 200

    response = response_raw.json()

    assert response == {
        'data': {
            'register': {
              'ok': False
            }
        }
    }
