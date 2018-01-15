from libs.tools import Identity
from .. import Teleferic_Identity
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

        # Validate container hash
        verify_sha256(container.get('objectContainer'),
                      container.get('containerHash'))

        # Validate container signature
        validate_timestamped_signature(
            sender_pubkey, container_hash, container.get('containerSig'))

        # Validate date limits
        now = datetime.datetime.now(datetime.timezone.utc)

        # Validate validUntil
        _validUntil = Teleferic_Identity.decrypt_content(
            container.get('validUntil'))
        validUntil = dateutil.parser.parse(_validUntil)
        if validUntil <= now:
            raise Exception('Invalid validUntil, is on the past. %s' % validUntil)

        # Validate retainUntil
        _retainUntil = Teleferic_Identity.decrypt_content(
            container.get('retainUntil'))
        retainUntil = dateutil.parser.parse(_retainUntil)
        if retainUntil < validUntil:
            raise Exception('Invalid retainUntil, is before validUntil. %s' % retainUntil)
