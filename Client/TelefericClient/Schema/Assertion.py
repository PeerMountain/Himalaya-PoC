import base64
import msgpack
from collections import OrderedDict
from Crypto.Hash import SHA256, HMAC

from Cryptography import AES, RSA
from .MessageBody import MessageBody
from .MessageEnvelope import MessageEnvelope
from .MessageContent import MessageContent

class Assertion(MessageEnvelope):
    subject_address = None
    assertions = None

    def __init__(self, subject_address, assertions, container_key=None):
        assertions = list(
            self.build_assertion_list(assertions, container_key)
        )
        containers = list(
            self.build_container_list(assertions)
        )
        metahashes = list(
            self.build_meta_hash_list(assertions)
        )

        message_body = MessageBody(
            subjectAddr=subject_address,
            assertions=assertions
        )

        message_content = MessageContent(
            message_type=0, # BodyTypes.Assertion.ANY,
            message_body=message_body,
        )

    def build_assertion_list(self, assertions, container_key):
        for assertion in assertions:
            if not container_key:
                container_key = self.generate_random_bytes()
            cipher = AES(container_key)
            container = cipher.encrypt(assertion.object)

            object_hash = base64.b64encode(
                SHA256.new(assertion.object).digest()
            )
            container_hash = base64.b64encode(
                SHA256.new(container).digest()
            )

            object_signature = self.identity.sign_message(
                object_hash, self.client
            )

            container_signature = self.identity.sign_message(
                container_hash, self.client
            )

            yield {
                'validUntil': assertion.valid_until,
                'retainUntil': assertion.retain_until,
                'containerHash': container_hash,
                'containerKey': container_key,
                'objectHash': object_hash,
                'objectSign': object_signature, 
                'metas': assertion.metas,
                'container': container,
                'containerSignature': container_signature,
            }

    def build_meta_hash_list(self, assertions):
        for assertion in assertions:
            metahashes = []
            for meta in assertion.metas:
                salt = self.generate_random_bytes()
                pack = msgpack.pack(meta)
                salted_meta_hash = base64.b64encode(
                    HMAC.new(
                        salt, pack, "SHA256"
                    ).digest()
                )

                # FIXME I hope this updates the dicts living inside the assertions
                meta.update({
                    'metaSalt': salt,
                })

                metahashes.append(salted_meta_hash)
            yield metahashes
 
    def build_container_list(self, assertions, meta_hashes):
        teleferic_pubkey = self.client.get_node_pubkey()
        for i, assertion in enumerate(assertions):
            yield {
                'containerHash': assertion.get('containerHash'),
                'objectHash': assertion.get('objectHash'),
                'containerSig': assertion.pop('containerSignature'),
                'metaHashes': meta_hashes[i],
                'retainUntil': RSA(teleferic_pubkey).encrypt(
                    assertion.get('retainUntil'), None
                ),
                'validUntil': RSA(teleferic_pubkey).encrypt(
                    assertion.get('validUntil'), None
                ),
                'objectContainer': assertion.pop('container')
            }