from .Base import Message, MessageContent, MessageBody, MessageEnvelope
from collections import OrderedDict
import random

from TelefericClient.Cryptography import AES
from TelefericClient import Client


class Invite(MessageEnvelope):

    MESSAGE_TYPE = 'REGISTRATION'
    MESSAGE_BODY_TYPE = 0

    def compose(self, bootstrapAddr, bootstrapNode, inviteName, offeringAddr, serviceAnnouncementMessage, serviceOfferingID, inviteKey=None):
        if inviteKey is None:
            self.inviteKey = self.generate_random_passphrase()
        else:
            self.inviteKey = inviteKey

        cipher = AES(self.inviteKey)
        encryptedInviteName = cipher.encrypt(inviteName.encode())

        message_body = MessageBody(
            self.MESSAGE_BODY_TYPE,
            bootstrapAddr=bootstrapAddr,
            bootstrapNode=bootstrapNode,
            inviteName=encryptedInviteName,
            offeringAddr=offeringAddr,
            serviceAnnouncementMessage=serviceAnnouncementMessage,
            serviceOfferingID=serviceOfferingID
        )

        message_content = MessageContent(
            'REGISTRATION',
            message_body
        )

        self.message = Message(message_content)

    def generate_random_passphrase(self):
        key_accumulator = b''
        for i in range(40):
            key_accumulator += chr(random.randint(0, 255))
        return key_accumulator
