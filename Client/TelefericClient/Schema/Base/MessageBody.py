import msgpack
import base64

from collections import OrderedDict

from .Base import Base
from Crypto.Hash import SHA256


class MessageBody(Base):
    content = OrderedDict()

    def __init__(self, body_type, **kwargs):
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
        return msgpack.packb(self.content)

    @classmethod
    def decode(b64PackMessageBody):
        packMessageBody = base64.b64decode(b64PackMessageBody)
        content = msgpack.unpackb(packMessageBody)
        return MessageBody(**content)

    def build(self):
        build = base64.b64encode(self.pack())
        self.hash = base64.b64encode(SHA256.new(build).digest()).decode()
        return build.decode()
