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


class ASSERTION_TYPE(Enum):
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
            1: self.build_message_analysis
        }

        attestations = list(
            self.build_attestations_list(_attestations.get('attestations'))
        )

        containers = next(self.build_container_list(attestations))

        message_body = MessageBody(
            subjectAddr=self.identity.address,
            z=attestations,
            body_type=0
        )

        message_content = MessageContent(
            message_type="ASSERTION",  # Assertion
            message_body=message_body,
        )

        passphrase = self.generate_random_bytes(length=32)

        self.message = Message(
            message_content,
            passphrase,
            readers,
            containers,
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
            'containerHash': attestation.get('containerHash'),
            'objectHash':  attestation.get('objectHash'),
            'metaType': attestation.get('metaType'),
            'metaValue': attestation.get('metaValue'),
            'metaSalt': attestation.get('metaSalt'),
            'attest': attestation.get('attest'),
            'container': {
                'containerHash': attestation.get('containerHash'),
                'objectHash':  attestation.get('objectHash'),
                'saltedMetaHashes': salted_meta_hash,
            }
        }

    def build_attestations_list(self, attestations):
        for attestation in attestations:
            
            attestation_type = attestation.get('type').value

            details = next(self.builders_map.get(attestation_type)(attestation.get('detail')))
            container = details.pop('container')

            datails_pack = msgpack.packb(details)

            attestation_signature = self.identity.sign_bytes(datails_pack,self.client)

            yield {
                'attestType': attestation_type,
                'attestSign': attestation_signature,
                'detail': datails_pack,
                'container': container
            }

    def build_container_list(self, attestations):
        containers =  []
        for attestation in attestations:
            container = attestation.pop('container')
            aux = [x for x in containers if x.get('containerHash')]
            if aux.__len__() is 0:
                aux = {
                    'containerHash': container.get('containerHash'),
                    'objectHash':  container.get('objectHash'),
                    'saltedMetaHashes': [container.get('saltedMetaHashes')],
                }
                containers.append(aux)
            else:
                aux.get('saltedMetaHashes').append(container.get('saltedMetaHashes'))
        yield containers
            