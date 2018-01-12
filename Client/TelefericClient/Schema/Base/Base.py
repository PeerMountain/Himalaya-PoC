import msgpack
import base64

class Base():
    
    content = {}

    def __init__(self, **kargs):
        self.content = kargs

    def get(self, key):
      if key in self.content:
        return self.content.get(key)
      else:
        raise Exception('Key "%s" not exist.' % key)

    def generate_random_bytes(self, length=40):
        key_accumulator = b''
        for i in range(length):
            key_accumulator += chr(random.randint(0, 255))
        return key_accumulator