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
        object_hash = encode_hash(_object.get('objectHash'))

        # if objectContainer be present
        objectContainer = _object.get('objectContainer')
        if not objectContainer is None:
            container_object = _object.get('objectContainer')
            container_hash = _object.get('containerHash')
            # Validate container hash
            verify_sha256(_object.get('objectContainer'),
                        _object.get('containerHash'))

            # Validate container signature
            validate_timestamped_signature(
                sender_pubkey, container_hash, _object.get('containerSig'))
        else:
            if not Reader.get_object_existance(object_hash):
                raise Exception('Object %s not exist.' % object_hash)