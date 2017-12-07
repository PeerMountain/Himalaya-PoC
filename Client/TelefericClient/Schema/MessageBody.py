import msgpack
import base64
from collections import OrderedDict

class MessageBody():
  
  def decode(self,b64PackMessageBody):
    packMessageBody = base64.b64decode(b64PackMessageBody)
    messageBody = msgpack.unpackb(packMessageBody)
    return messageBody

  def encode(self,messageBody):
    packMessageBody = msgpack.packb(messageBody)
    b64PackMessageBody = base64.b64encode(packMessageBody)
    return b64PackMessageBody