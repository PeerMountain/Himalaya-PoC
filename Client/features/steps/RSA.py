# -- FILE: features/steps/RSA.py
import os
from behave import given, when, then, step

from HimalayaClient.Crypto import RSA

@given('the following <privkey>')
def step_imp(context):
  context.key = RSA(context.text.strip())

@given('the following <pubkey>')
def step_imp(context):
  context.key = RSA(context.text.strip())

@given('a {message}')
def step_imp(context, message):
  context.message = message.strip().encode()

@when('I sign the message hash with RSA')
def step_imp(context):
  context.current_sign = context.key.sign(context.message)

@when('verify the signature with message hash')
def step_imp(context):
  context.current_verification = context.key.verify(context.message, context.given_sign)

@when('convert the signature from long to bytes')
def step_imp(context):
  pass

@when('I encode the signature bytes on base64')
def step_imp(context):
  pass

@when('I calculate SHA256 of the message')
def step_imp(context):
  pass

@when('I decode {given_sign} with base64')
def step_imp(context, given_sign):
  context.given_sign = given_sign.strip().encode()

@when('convert the signature from byte to long')
def step_imp(context):
  pass

@when('I encrypt the message with RSA')
def step_imp(context):
  context.encrypted_message = context.key.encrypt(context.message)

@when('encode the result with base64')
def step_imp(context):
  pass

@when('decode the message with base64')
def step_imp(context):
  pass

@when('decrypt the result with RSA')
def step_imp(context):
  pass

@then('the decryped message should be equal to {given_decrypted_message}')
def step_imp(context, given_decrypted_message):
  print ('esto', context.key.decrypt(context.message))
  assert context.key.decrypt(context.message) == given_decrypted_message.strip().encode()

@then('the encoded message should be equal to {encrypted_message}')
def step_imp(context,encrypted_message):
  print('aca',context.encrypted_message)
  assert encrypted_message.strip().encode() == context.encrypted_message

@then('the signature and {given_sign} should be equal')
def step_imp(context, given_sign):
  print(context.current_sign)
  assert context.current_sign == given_sign.strip().encode()

@then('the resulted verification should be valid')
def step_imp(context):
  assert context.current_verification