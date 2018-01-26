#!/usr/bin/env python3
from collections import OrderedDict

import msgpack
import base64

from TelefericClient.Identity import Identity
from TelefericClient.Client import Client
from TelefericClient.Cryptography import AES

from pprint import pprint

idn_reader = Identity(open("keys/4096_a.private").read())
#message_hash = b'd0+J5K0myPITO2/alAcnTokv3rugorCeBguNqJ4aSx4='
message_hash = b'Gs4N80OC1FE53Uwi4xbCPgeq08zVpDyadieVPwKOeGU='
#Retrive assertion
client = Client("http://127.0.0.1:8000/teleferic/", debug=False)

query = '''
  query(
    $messageHash: SHA256!
  ){
    messageByHash(messageHash:$messageHash){
      sender{
        address
        nickname
      }
      messageHash
      messageType
      messageSig
      dossierHash
      bodyHash
      ACL{
        reader{
          address
        }
        key
      }
      containers{
        objectHash
        saltedMetaHashes
        containerHash
        objectContainer
      }
      createdAt
      message
      
    }
  }
'''

variables = {
    'messageHash': message_hash
}

envelope = client.request(query,variables).get('data').get('messageByHash')
key_raw = [x for x in envelope.get('ACL') if x.get('reader').get('address') == idn_reader.address][0]
key = idn_reader.decrypt(key_raw.get('key'))

message_raw = AES(key).decrypt(envelope.get('message'))
message = msgpack.unpackb(message_raw)
message_body = msgpack.unpackb(base64.b64decode(message.get(b'messageBody')))



pprint('Envelope')
pprint(envelope)
pprint('Message')
pprint(message)
pprint('Message Body')
pprint(message_body)