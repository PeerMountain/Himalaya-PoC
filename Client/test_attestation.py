from collections import OrderedDict

import base64
import msgpack
from Crypto.Hash import HMAC, SHA256

from TelefericClient.Identity import Identity
from TelefericClient.Client import Client
from TelefericClient.Cryptography import AES
from TelefericClient.Schema.Attestation import Attestation, ATTESTATION_TYPE

# Defines reader and sender
idn_sender = Identity(open('keys/4096_a.private').read())
idn_reader = Identity(open('keys/4096_c.public').read())

# Define assertion message hash
assertion_hash = b'zep8e4dV0Jex0dpt4fCZed6YT7TW5ySXtHszCqB7bnE='

# Retrive assertion
client = Client('http://127.0.0.1:8000/teleferic/', debug=False)
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
                metaHashes
                container {
                    containerHash
                    containerSign
                    objectContainer
                }
            }
            bodyHash
            message
        }
    }'''

variables = {
    'messageHash': assertion_hash,
}

assertion_raw = client.request(query, variables).get('data').get('messageByHash')

# Get key
sender_acl = [
    acl for acl in assertion_raw.get('ACL') if acl.get('reader').get('address') == idn_sender.address
][0]
key = idn_sender.decrypt(sender_acl.get('key'))

# Get message and message_body
message_raw = AES(key).decrypt(assertion_raw.get('message'))
message = msgpack.unpackb(message_raw)
message_body = msgpack.unpackb(message.get(b'messageBody'))

assertions = message_body.get(b'assertions')
attestations = []

# Build attestations for each assertion
for assertion in assertions:
    objects = assertion_raw.get('objects')
    container_hash = assertion.get(b'containerHash')

    container = [
        obj for obj in objects if obj.get('container').get('containerHash').encode() == container_hash
    ][0]

    metas = assertion.get(b'metas')
    # Validates metaHash and constructs list of attestations
    for index, meta in enumerate(metas):
        unpacked_meta = msgpack.unpackb(meta)

        meta_type = unpacked_meta.get(b'metaType')
        meta_value = unpacked_meta.get(b'metaValue')
        meta_salt = unpacked_meta.get(b'metaSalt')

        meta_validation = OrderedDict()
        meta_validation['metaType'] = meta_type
        meta_validation['metaValue'] = meta_value
        meta_validation['metaSalt'] = meta_salt

        packed_meta_validation = msgpack.packb(meta_validation)
        salted_meta_hash = base64.b64encode(
            HMAC.new( meta_salt, packed_meta_validation, SHA256).digest()
        )

        assert salted_meta_hash == container.get('metaHashes')[index].encode()

        attestations.append({
            'type': ATTESTATION_TYPE.Message_Analysis,
            'detail': {
                'bodyHash': assertion_raw.get('bodyHash'),
                'objectHash': container.get('objectHash'),
                'metaType': meta_type,
                'metaValue': meta_value, 
                'metaSalt': meta_salt,
                'attest': 'Test',
            }
        })

# Build attestation objects
readers = [idn_reader]
attributes = OrderedDict(**{
    'subject': assertion_hash,
    'attestations': attestations,
})

# Send attestation
attestation = Attestation(idn_sender, client, attributes, readers)
result = attestation.send()
print('Result', result)
