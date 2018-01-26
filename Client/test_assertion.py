#!/usr/bin/env python3
from collections import OrderedDict
import datetime

from TelefericClient.Identity import Identity
from TelefericClient.Client import Client
from TelefericClient.Schema.Assertion import Assertion

now = datetime.datetime.now(datetime.timezone.utc)
tomorrow = now + datetime.timedelta(days=1)

idn_sender = Identity(open("keys/4096_registred.private").read())
idn_reader = Identity(open("keys/4096_registred.public").read())

readers = [idn_reader]
client = Client("http://localhost:8000/teleferic/")
ass = [
    {
        'valid_until': now.isoformat(),
        'retain_until': tomorrow.isoformat(),
        'object': b'\x12\x34\x56\x78\x90',
        'metas': [
            OrderedDict(**{
                'metaKey': 2, 
                'metaValue': 'Pepe Sarasa'
            })
        ]
    }
]

assertion = Assertion(idn_sender, client, ass, readers)
# agarra la asercion recien creada 
result = assertion.send(debug=True)
print('Result', result)
