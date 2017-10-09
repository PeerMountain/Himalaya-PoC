from __future__ import print_function

from Crypto.Hash import RIPEMD
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5

import random

import base58
import json

import os

from identity_tools import Identity
import requests

from settings import IDENTITY_FOLDER, ENDPOINT

identity_filepath = 'identity'

privkey_file = open(identity_filepath, 'rb')
privkey = RSA.importKey(privkey_file.read())
identity = Identity(privkey)

print('Pubkey:', identity.pubkey)
print('Address:', identity.address)