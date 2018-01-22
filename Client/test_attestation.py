#!/usr/bin/env python3
from collections import OrderedDict
import datetime

from TelefericClient.Identity import Identity
from TelefericClient.Client import Client
from TelefericClient.Schema.Attestation import Attestation, ASSERTION_TYPE

idn_sender = Identity(open("keys/4096_a.private").read())
idn_reader = Identity(open("keys/4096_b.public").read())

assertion = 'EKgLvSTTA3EGMEsPr/9hj+snAo5y/62y9V0Al+JB3+k='

readers = [idn_reader]
client = Client("http://127.0.0.1:8000/teleferic/", debug=True)
att = OrderedDict(**{
    'subject': assertion,
    'attestations': [{
        'type': ASSERTION_TYPE.Message_Analysis,
        'detail': {
            'containerHash': b'LS66jsaQHcN0Z9X/nM/WD8JNdqXQA5YrnadRLnHNh1E=',
            'objectHash': b'bEUOA355t28jGnGiL/QEA/fZt0sV4BTlL+EVbTZmw+Y=',
            'metaType': 2,
            'metaValue': b'Pepe Sarasa',
            'metaSalt': b'xG\xb8\xf5jbx\xbd3x\xbf\xb9\x14\x1a\xb65\xd2\xdb\xd4\x96\\\xda\xba"K\xe0\xba\\\\\x9a\x01t=\x19\xa1c\xea\x0fu\x80',
            'attest': 'Test'
        }
    }]
})

attestation = Attestation(idn_sender, client, att, readers)
# agarra la asercion recien creada 
result = attestation.send(debug=True)
print('Result', result)