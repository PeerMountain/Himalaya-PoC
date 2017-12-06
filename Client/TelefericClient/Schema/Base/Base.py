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