import base64
import msgpack
from collections import OrderedDict
from Crypto.Hash import SHA256, HMAC

from Cryptography import AES
from .MessageBody import MessageBody
from .MessageEnvelope import MessageEnvelope

class Assertion(MessageEnvelope):
    subject_address = None
    assertions = None

    def __init__(self, subject_address, assertions, container_key=None):
        assertions = frozenset(assertions)
        assertions = list(
            self.build_assertion_list(assertions, container_key)
        ),

        message_body = MessageBody(
            subjectAddr=subject_address,
            assertions=assertions
        )

        def build_meta_hashes(assertions):
            for assertion in assertions:
                for meta in assertion.metas:
                    if meta.get('metaSalt'): continue
                    salt = self.generate_random_bytes()
                    pack = msgpack.pack(meta)
                    salted_meta_hash = base64.b64encode(
                        HMAC.new(
                            salt, pack, "SHA256"
                        ).digest()
                    )

                    meta.update({
                        'metaSalt': salt,
                    })

                    yield meta, salted_meta_hash

        metas = tuple(
            x[0] for x in build_meta_hashes(assertions)
        )
        meta_hashes = tuple(
            x[1] for x in build_meta_hashes(assertions)
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

            yield {
                'validUntil': assertion.valid_until,
                'retainUntil': assertion.retain_until,
                'containerHash': container_hash,
                'containerKey': container_key,
                'objectHash': object_hash,
                'objectSign': object_signature,
                'metas': assertion.metas
            }