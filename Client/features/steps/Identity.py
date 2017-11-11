# -- FILE: features/steps/Identity.py
import os
from behave import given, when, then, step

from HimalayaClient import Identity

@when('compute SHA256 hash of pubkey')
def step_imp(context):
  pass

@when('compute RIPEMD160 of resulting SHA256')
def step_imp(context):
  pass

@when('prefix resulting RIPEMD160 with [1, 0] bytes to generate the base address')
def step_imp(context):
  pass

@when('apply SHA256 two times over resulting RIPEMD160 to generate the checksum')
def step_imp(context):
  pass

@when('append last 4 bytes of resulting checksum at the end of base address to generate the address')
def step_imp(context):
  pass

@then('the address should be {address}')
def step_imp(context, address):
  identity = Identity(context.key.key)
  assert identity.address == address.strip()