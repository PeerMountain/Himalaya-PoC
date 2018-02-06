import base64
import msgpack
from collections import OrderedDict
from Crypto.Hash import SHA256, HMAC

from ..Cryptography import AES, RSA
from .Base.MessageBody import MessageBody
from .Base.MessageEnvelope import MessageEnvelope
from .Base.MessageContent import MessageContent
from .Base.Message import Message

class Assertion(MessageEnvelope):
    subject_address = None
    assertions = None

    def __init__(self, identity, client, assertions, readers, container_key=None):
        self.identity = identity
        self.client = client

        assertions = list(
            self.build_assertion_list(assertions, container_key)
        )
        meta_hashes = list(
            self.build_salted_meta_hash_list(assertions)
        )
        objects = list(
            self.build_object_list(assertions, meta_hashes)
        )

        message_body = MessageBody(
            subjectAddr=self.identity.address,
            assertions=assertions,
            # TODO(felipe) check this body type constant
            # is it always 0 for assertions?
            body_type=0
        )


        message_content = MessageContent(
            message_type="ASSERTION", # Assertion
            message_body=message_body,
        )

        passphrase = self.generate_random_bytes(length=32)

        self.message = Message(
            message_content,
            passphrase,
            readers,
            objects,
        )

    def build_assertion_list(self, assertions, container_key):
        for assertion in assertions:
            if not container_key:
                container_key = self.generate_random_bytes(length=32)
            cipher = AES(container_key)
            container = cipher.encrypt(assertion.get('object')).decode()

            object_hash = base64.b64encode(
                SHA256.new(assertion.get('object')).digest()
            ).decode()
            container_hash = base64.b64encode(
                SHA256.new(container.encode()).digest()
            )

            object_signature = self.identity.sign_message(
                object_hash, self.client
            )

            container_signature = self.identity.sign_message(
                container_hash, self.client
            )

            yield {
                'validUntil': assertion.get('valid_until'),
                'retainUntil': assertion.get('retain_until'),
                'containerHash': container_hash.decode(),
                'containerKey': container_key,
                'objectHash': object_hash,
                'objectSign': object_signature, 
                'metas': assertion.get('metas'),
                'container': container,
                'containerSignature': container_signature,
            }

    def build_salted_meta_hash_list(self, assertions):
        for assertion in assertions:
            salted_meta_hashes = []
            for meta in assertion.get('metas'):
                salt = self.generate_random_bytes()
                meta_base = OrderedDict()
                meta_base['metaType'] = meta.get('metaType')
                meta_base['metaValue'] = meta.get('metaValue')
                pack = msgpack.packb(meta_base)
                salted_meta_hash = base64.b64encode(
                    HMAC.new(
                        salt, pack, SHA256
                    ).digest()
                )

                # FIXME I hope this updates the dicts living inside the assertions
                meta.update({
                    'metaSalt': salt,
                })

                salted_meta_hashes.append(salted_meta_hash.decode())
            yield salted_meta_hashes
 
    def build_object_list(self, assertions, salted_meta_hashes):
        teleferic_pubkey = self.client.get_node_pubkey()
        for i, assertion in enumerate(assertions):
            container = {
                'containerHash': assertion.get('containerHash'),
                'containerSign': assertion.get('containerSignature'),
                'objectContainer': assertion.get('container'),
            }

            yield {
                'objectHash': assertion.get('objectHash'),
                'metaHashes': salted_meta_hashes[i],
                'container': container,
            }
