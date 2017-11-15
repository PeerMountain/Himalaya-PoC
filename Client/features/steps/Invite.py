# -- FILE: features/steps/Invite.py
import os
from behave import given, when, then, step

from TelefericClient.Cryptography import AES

@given('secret passphrase {passphrase}')
def step_impl(context,passphrase):
  context.passphrase = passphrase.strip().encode()
  print(len(context.passphrase))
  assert len(context.passphrase) == 32

@given('secret invite name {inviteName}')
def step_impl(context, inviteName):
  context.inviteName = inviteName.strip().encode()

@when('I encrypt using AES module and given passphrase')
def step_impl(context):
  cipher = AES(context.passphrase)
  context.encryptedInviteName = cipher.encrypt(context.inviteName)

@then('the resulting encrypted invite name should be {result}')
def step_impl(context, result):
  print(context.encryptedInviteName)
  assert context.encryptedInviteName == result.strip().encode()  