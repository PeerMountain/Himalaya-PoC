#!/usr/bin/env python3
from collections import OrderedDict

import msgpack
import base64
from Crypto.Hash import HMAC, SHA256


from TelefericClient.Identity import Identity
from TelefericClient.Client import Client
from TelefericClient.Cryptography import AES
from TelefericClient.Schema.Attestation import Attestation, ATTESTATION_TYPE

idn_sender = Identity(open("keys/4096_b.private").read())
idn_reader = Identity(open("keys/4096_a.public").read())

assertion_hash = b'guq7X42Eb/MJhkSLXr5B0+qr3HzEzDHO0UaX4bKqZTY='

#Retrive assertion
client = Client("http://127.0.0.1:8000/teleferic/", debug=False)
query = '''
    query(
        $messageHash: SHA256!
    ){
        messageByHash(messageHash: $messageHash){
            ACL{
                reader{
                    address
                }
                key
            }
            objects{
                objectHash
                containerHash
                objectContainer
                metaHashes
            }
            bodyHash
            message
        }
    }'''
variables = {
    'messageHash': assertion_hash
}

assertion_raw = client.request(query,variables).get('data').get('messageByHash')
key_raw = [x for x in assertion_raw.get('ACL') if x.get('reader').get('address') == idn_sender.address][0]
key = idn_sender.decrypt(key_raw.get('key'))

message_raw = AES(key).decrypt(assertion_raw.get('message'))
message = msgpack.unpackb(message_raw)
message_body = msgpack.unpackb(base64.b64decode(message.get(b'messageBody')))

assertions = message_body.get(b'assertions')
attetations = []
for assertion in message_body.get(b'assertions'):
    container = [x for x in assertion_raw.get('objects') if x.get('containerHash').encode() == assertion.get(b'containerHash')][0]
    metas = assertion.get(b'metas')
    for index,meta in enumerate(metas):
        meta_validation = OrderedDict()
        meta_validation['metaType'] = meta.get(b'metaType')
        meta_validation['metaValue'] = meta.get(b'metaValue')
        pack = msgpack.packb(meta_validation)
        salt = meta.get(b'metaSalt')
        salted_meta_hash = base64.b64encode(
            HMAC.new(
                salt, pack, SHA256
            ).digest()
        )

        print(salted_meta_hash,container.get('metaHashes')[index].encode())
        assert salted_meta_hash == container.get('metaHashes')[index].encode()

        print(container.get('containerHash'),meta.get(b'metaType'),meta.get(b'metaValue'))

        attetations.append({
            'type': ATTESTATION_TYPE.Message_Analysis,
            'detail': {
                'bodyHash': assertion_raw.get('bodyHash'),
                'objectHash': container.get('objectHash'),
                'metaType': meta.get(b'metaType'),
                'metaValue':  meta.get(b'metaValue'),
                'metaSalt':  meta.get(b'metaSalt'),
                'attest': 'Test'
            }
        })
readers = [idn_reader]
att = OrderedDict(**{
    'subject': assertion_hash,
    'attestations': attetations
})

attestation = Attestation(idn_sender, client, att, readers)
result = attestation.send()
print('Result', result)