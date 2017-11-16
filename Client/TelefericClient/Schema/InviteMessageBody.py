from .MessageBody import MessageBody
from collections import OrderedDict

class InviteMessageBody(MessageBody):
  messageBody = OrderedDict()

  def __init__(self, *args, **kargs):
    self.messageBody['bootstrapAddr'] = kargs['bootstrapAddr']
    self.messageBody['bootstrapNode'] = kargs['bootstrapNode']
    self.messageBody['inviteName'] = kargs['encryptedInviteName']
    self.messageBody['offeringAddr'] = kargs['offeringAddr']
    self.messageBody['serviceAnnouncementMessage'] = kargs['serviceAnnouncementMessage']
    self.messageBody['serviceOfferingID'] = kargs['serviceOfferingID']
  
  