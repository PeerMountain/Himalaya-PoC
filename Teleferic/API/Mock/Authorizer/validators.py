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


def validate_objects(sender_pubkey, objects=[]):
    # For each container
    for _object in objects:
        # if objectContainer be present
        container = _object.get('container')
        if not container is None:
            container_object = container.get('objectContainer')
            container_hash = container.get('containerHash')
        
            # Validate container hash
            verify_sha256(container_object, container_hash)

            # Validate container signature
            validate_timestamped_signature(
                sender_pubkey, container_hash, container.get('containerSign'))
        else:
            object_hash = encode_hash(_object.get('objectHash'))
            if not Reader.get_object_existance(object_hash):
                raise Exception('Object %s not exist.' % object_hash)