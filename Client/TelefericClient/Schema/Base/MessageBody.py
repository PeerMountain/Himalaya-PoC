import msgpack
import base64

from collections import OrderedDict

from .Base import Base
from Cryptodome.Hash import SHA256


class MessageBody(Base):
    content = OrderedDict()

    def __init__(self, body_type, **kwargs):
        """__init__

        Create a message body, using the parameters passed.

        :param body_type: int: Body type.
        :param **kwargs: dict: Data to be stored.
        """
        if not type(body_type) is type(1):
            raise Exception('Body type should be integer.')
        self.type = body_type
        for key, value in kwargs.items():
            if type(value) == bytes:
                value = value.decode()
            self.content[key] = value

    def get(self, key):
        if key in self.content:
            return self.content.get(key)
        else:
            raise Exception('Key "%s" not exist.' % key)

    def pack(self):
        """pack
        Return a MessagePack representation of the message's content.
        """
        return msgpack.packb(self.content)

    @classmethod
    def decode(b64PackMessageBody):
        """decode

        Decode a base64 encoded MessagePack byte array into a MessageBody instance.

        :param b64PackMessageBody: string: Base64 encoded MessagePack.
        """
        packMessageBody = base64.b64decode(b64PackMessageBody)
        content = msgpack.unpackb(packMessageBody)
        return MessageBody(**content)

    def build(self):
        """build
        
        Build the base64 encoded MessagePack string corresponding
        to the message body, and calculate its hash.
        """
        build = base64.b64encode(self.pack())
        self.hash = base64.b64encode(SHA256.new(build).digest()).decode()
        return build.decode()
