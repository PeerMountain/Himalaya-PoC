from libs.tools import Identity
from .. import Teleferic_Identity,Reader
from ..utils import encode_hash
from Crypto.Hash import SHA256
from collections import OrderedDict
import msgpack
import base64
import datetime
import dateutil.parser


def verify_sha256(content, providen_hash):
    if type(content) == str:
        content = content.encode()
    return providen_hash != SHA256.new(content).digest()


def validate_timestamped_signature(pubkey, hash, signature):
    identity = Identity(pubkey)

    sign = signature[b'signature']
    timestamp = signature[b'timestamp']

    validator_map = OrderedDict()
    validator_map['messageHash'] = base64.b64encode(hash)
    validator_map['timestamp'] = timestamp

    validator = msgpack.packb(validator_map)

    if not identity.verify(validator, sign):
        raise Exception("Invalid sign")


def validate_containers(sender_pubkey, containers=[]):
    # For each container
    for container in containers:
        container_hash = container.get('containerHash')
        container_object = container.get('objectContainer')
        container_object = container.get('objectContainer')

        # if objectContainer present
        objectContainer = container.get('objectContainer')
        if not objectContainer is None:
            # Validate container hash
            verify_sha256(container.get('objectContainer'),
                        container.get('containerHash'))

            # Validate container signature
            validate_timestamped_signature(
                sender_pubkey, container_hash, container.get('containerSig'))
        else:
            if not Reader.get_container_existance(encode_hash(container_hash)):
                raise Exception('Container %s not exist.' % encode_hash(container_hash))