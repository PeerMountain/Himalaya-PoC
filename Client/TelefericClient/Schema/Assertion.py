from .MessageBody import MessageBody

class Assertion(MessageBody):
  subject_address = None
  assertions = None

  def __init__(self, subject_address, assertions):
    