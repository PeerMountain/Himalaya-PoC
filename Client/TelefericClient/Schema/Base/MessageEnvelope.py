from TelefericClient import Client


class MessageEnvelope():
    """MessageEnvelope

    Helper class for Teleferic API connection.
    """

    def __init__(self, identity, node):
        self.identity = identity
        self.client = Client(node)

    def send(self):
        """send

        Send the message to Teleferic's API.
        """
        return self.client.request(
            query='''
            mutation (
                $sender: Address!
                $messageType: MessageType!
                $messageHash: SHA256!
                $bodyHash: SHA256!
                $messageSig: Sign!
                $message: AESEncryptedBlob!
                $dossierHash: HMACSHA256!
                ){
                sendMessage(
                    envelope: {
                    sender: $sender
                    messageType: $messageType
                    messageHash: $messageHash
                    bodyHash: $bodyHash
                    messageSig: $messageSig
                    message: $message
                    dossierHash: $dossierHash
                    }
                ) {
                    messageHash
                }
            }
            ''',
            variables=self.message.build(self.identity, self.client)
        )
