import base64
import msgpack
from Crypto.Hash import SHA256, HMAC
from collections import OrderedDict
from enum import Enum

from ..Cryptography import AES, RSA
from .Base.MessageBody import MessageBody
from .Base.MessageEnvelope import MessageEnvelope
from .Base.MessageContent import MessageContent
from .Base.Message import Message


class ATTESTATION_TYPE(Enum):
    Message_Analysis     = 1
    Message_Comparison   = 2
    Research_Analysis    = 3
    Retraction_Rejection = 4

class Attestation(MessageEnvelope):
    subject_address = None
    attestations = None

    def __init__(self, identity, client, _attestations, readers):
        self.identity = identity
        self.client = client

        self.builders_map = {
            ATTESTATION_TYPE.Message_Analysis: self.build_message_analysis
        }

        attestations = list(
            self.build_attestations_list(_attestations.get('attestations'))
        )

        objects = next(self.build_object_list(attestations))

        message_body = MessageBody(
            subjectAddr=self.identity.address,
            attestations=attestations,
            body_type=0
        )

        message_content = MessageContent(
            message_type="ATTESTATION",
            message_body=message_body,
        )

        passphrase = self.generate_random_bytes(length=32)

        self.message = Message(
            message_content,
            passphrase,
            readers,
            objects,
        )

    def build_message_analysis(self, attestation):
        salt = attestation.get('metaSalt')
        metas = OrderedDict()
        metas['metaType'] = attestation.get('metaType')
        metas['metaValue'] = attestation.get('metaValue')
        pack = msgpack.packb(metas)
        salted_meta_hash = base64.b64encode(
            HMAC.new(
                salt, pack, SHA256
            ).digest()
        )
        yield {
            'bodyHash': attestation.get('bodyHash'),
            'objectHash':  attestation.get('objectHash'),
            'metaType': attestation.get('metaType'),
            'metaValue': attestation.get('metaValue'),
            'metaSalt': attestation.get('metaSalt'),
            'attest': attestation.get('attest'),
            'object': {
                'objectHash':  attestation.get('objectHash'),
                'metaHashes': salted_meta_hash,
            }
        }

    def build_attestations_list(self, attestations):
        for attestation in attestations:
            
            attestation_type = attestation.get('type')

            details = next(self.builders_map.get(attestation_type)(attestation.get('detail')))
            _object = details.pop('object')

            datails_pack = msgpack.packb(details)

            attestation_signature = self.identity.sign_bytes(datails_pack,self.client)
            yield {
                'attestType': attestation_type.value,
                'attestSign': attestation_signature,
                'detail': datails_pack,
                'object': _object
            }

    def build_object_list(self, attestations):
        objects =  []
        for attestation in attestations:
            _object = attestation.pop('object')
            aux = [x for x in objects if x.get('objectHash') == _object.get('objectHash')]
            if aux.__len__() is 0:
                aux = {
                    'objectHash':  _object.get('objectHash'),
                    'metaHashes': [_object.get('metaHashes')],
                }
                objects.append(aux)
            else:
                aux[0].get('metaHashes').append(_object.get('metaHashes'))
        yield objects
            