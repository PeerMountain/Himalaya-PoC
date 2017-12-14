from .Base import Message, MessageContent, MessageBody, MessageEnvelope

from TelefericClient.Cryptography import AES, RSA
from TelefericClient import Client

import base64
from Crypto.Hash import SHA256

class Register(MessageEnvelope):

    MESSAGE_TYPE = 'REGISTRATION'
    MESSAGE_BODY_TYPE = 1

    def compose(self, inviteMsgID, inviteKey, inviteName, nickname):

        node_pubkey = self.client.get_node_pubkey()
        node_cipher = RSA(node_pubkey)
    
        message_body = MessageBody(
            self.MESSAGE_BODY_TYPE,
            inviteMsgID=inviteMsgID,
            keyProof=node_cipher.encrypt(inviteKey.encode()),
            inviteName=node_cipher.encrypt(inviteName.encode()),
            publicKey=self.identity.pubkey,
            publicNickname=nickname
        )

        message_content = MessageContent(
            'REGISTRATION',
            message_body
        )

        self.message = Message(message_content)