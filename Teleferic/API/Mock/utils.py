import os
import base58
import base64
import msgpack

MESSAGES_STORAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),'messages')
CONTAINER_STORAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),'containers')

def get_message_path(message_hash):
  file_name = base58.b58encode(message_hash)
  return os.path.join(MESSAGES_STORAGE,file_name)

def get_container_path(message_hash):
  file_name = base58.b58encode(message_hash)
  return os.path.join(MESSAGES_STORAGE,file_name)

def encode_hash(_hash):
  if not type(_hash) is bytes:
    raise Exception('Hash needs to be bytes. %s' % _hash)
  return base64.b64encode(_hash)

def decode_hash(_hash_encoded):
  return base64.b64decode(_hash_encoded)

def encode_dict(_object):
  return base64.b64encode(msgpack.packb(_object))

def decode_dict(_string):
  return msgpack.unpackb(base64.b64decode(_string))