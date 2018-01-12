#!/usr/bin/env python3
from TelefericClient.Identity import Identity
from collections import OrderedDict
from TelefericClient.Client import Client
from TelefericClient.Schema.Assertion import Assertion

idn = Identity(open("/home/mori/dev_sk").read())
readers = [idn]
client = Client("http://192.168.252.14:8000/teleferic/")
ass = [{'valid_until': 0, 'retain_until': 0, 'object': b'\x12\x34\x56\x78\x90', 'metas': [OrderedDict(**{'metaKey': 2, 'metaValue': 'Pepe Sarasa'})]}]

assertion = Assertion(idn, client, ass, readers)
# agarra la asercion recien creada 
assertion.send()