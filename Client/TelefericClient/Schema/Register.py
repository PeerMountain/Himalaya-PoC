import msgpack

from .Base import Message, MessageContent, MessageBody, MessageEnvelope

from TelefericClient.Cryptography import AES, RSA
from TelefericClient import Client

import base64
from Crypto.Hash import SHA256

class Register(MessageEnvelope):
    """Register
    
    Message sent by invitees, responding to a registered user's invitation
    """

    MESSAGE_TYPE = 'REGISTRATION'
    MESSAGE_BODY_TYPE = 1

    def compose(self, inviteMsgID, inviteKey, inviteNonce, inviteName, nickname):
        """compose

        Compose the registration message.

        :param inviteMsgID: ID of the Invite message the client received.
        :param inviteKey: string: Key of the invite. Shared secret between inviter and invitee.
        :param inviteNonce: string: Nonce of the invite. Shared secret between inviter and invitee.
        :param inviteName: string: Name of the invite. Shared secret between inviter and invitee.
        :param nickname: Undocumented parameter.
        """

        node_pubkey = self.client.get_node_pubkey()
        node_cipher = RSA(node_pubkey)

        message_body = MessageBody(
            self.MESSAGE_BODY_TYPE,
            inviteMsgID=inviteMsgID,
            keyProof=node_cipher.encrypt(msgpack.packb({
                'key': inviteKey,
                'nonce': inviteNonce
            })),
            inviteName=node_cipher.encrypt(inviteName.encode()),
            publicKey=self.identity.pubkey,
            publicNickname=nickname,
        )

        message_content = MessageContent(
            'REGISTRATION',
            message_body,
            encrypt=False
        )

        self.message = Message(message_content)
