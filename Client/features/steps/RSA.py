# -- FILE: features/steps/RSA.py
import os
from behave import given, when, then, step

from TelefericClient.Cryptography import RSA

@given('the following privkey')
def step_imp(context):
  context.key = RSA(context.text.strip())

@given('the following pubkey')
def step_imp(context):
  context.key = RSA(context.text.strip())

@given('a content {content}')
def step_imp(context, content):
  context.content = content.strip().encode()

@when('I sign the content hash with RSA')
def step_imp(context):
  context.current_sign = context.key.sign(context.content)


@when('convert the signature from long to bytes')
def step_imp(context):
  pass

@when('I encode the signature from bytes on base64')
def step_imp(context):
  pass

@when('I calculate SHA256 of the content')
def step_imp(context):
  pass

@when('I decode signature {given_sign} with base64')
def step_imp(context, given_sign):
  context.given_sign = given_sign.strip().encode()

@when('I convert the signature from bytes to long')
def step_imp(context):
  pass

@when('I convert the signature from long to bytes')
def step_imp(context):
  pass

@when('I encrypt the content with RSA')
def step_imp(context):
  context.encrypted_content = context.key.encrypt(context.content)

@when('I encode the result with base64')
def step_imp(context):
  pass

@when('I decode the content with base64')
def step_imp(context):
  pass

@when('I decrypt the result with RSA')
def step_imp(context):
  pass

@then('the decryped content should be equal to {given_decrypted_content}')
def step_imp(context, given_decrypted_content):
  assert context.key.decrypt(context.content) == given_decrypted_content.strip().encode()

@then('the encoded content should be equal to {encrypted_content}')
def step_imp(context,encrypted_content):
  assert encrypted_content.strip().encode() == context.encrypted_content

@then('the signature and {given_sign} should be equal')
def step_imp(context, given_sign):
  assert context.current_sign == given_sign.strip().encode()

@then('verify the signature with calculate hash should be valid')
def step_imp(context):
  assert context.key.verify(context.content, context.given_sign)
