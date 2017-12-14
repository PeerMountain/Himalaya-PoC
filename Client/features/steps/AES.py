# -- FILE: features/steps/AES.py
import os
from behave import given, when, then

import base64

from TelefericClient.Cryptography import AES

@given('a passphrase {key}')
def step_imp(context, key):
  context.passphrase = key.strip().encode()

@given('secret 32 bytes passphrase {key}')
def step_imp(context, key):
  context.passphrase = key.strip().encode()
  assert len(context.passphrase) == 32

@when('I encrypt the resulted content with the resulted passphrase using AES')
def step_imp(context):
  context.result = AES(context.passphrase).encrypt(context.content)

@when('I decrypt the content with the resulted passphrase using AES')
def step_imp(context):
  context.result = AES(context.passphrase).decrypt(context.content)

@when('I encode encrypted content with Base64')
def step_imp(context):
  pass

@when('I made PKCS7 padding of passphrase to 32 bytes')
def step_imp(context):
  pass

@when('I made PKCS7 padding of content to 16 bytes block size')
def step_imp(context):
  pass

@when('I made PKCS7 unpadding of decoded content for 16 bytes block size')
def step_imp(context):
  pass

@when('I decode encrypted content with Base64')
def step_imp(context):
  pass

@given('result shoud be {result}')
def step_imp(context, result):
  assert result.strip().encode() == context.result 

@given(u'a text{input}')
def step_impl(context,input):
    context.input = input.strip().encode()

@when(u'I made PKCS7 padding of the text to {size} bytes')
def step_impl(context, size):
    try:
      context.padded = AES.pad(context.input,int(size))
      context.error = False
    except Exception as e:
      context.error = e

@then(u'the hexa result should be{result}')
def step_impl(context, result):
    wanted = bytes.fromhex(result.strip())
    if not context.error is False:  
      if wanted == b'Exception':
        assert True
        return
      else:
        raise context.error
    assert wanted == context.padded

@when(u'I encode it with Base64')
def step_impl(context):
    context.input = base64.b64encode(context.input)

@then(u'the result should be{result}')
def step_impl(context,result):
    wanted = result.strip().encode()
    assert wanted == context.input

@given(u'a base64 encoded text{input}')
def step_impl(context,input):
    context.input = input.strip().encode()
    if context.input == None:
      context.input = b''

@when(u'I dencode it')
def step_impl(context):
    context.input = base64.b64decode(context.input)

@when(u'I AES encrypt the content with the key')
def step_impl(context):
    pass

@then(u'I have to call PKCS7 padding of passphrase to {size} bytes')
def step_impl(context, size):
    context.passphrase = AES.pad(context.passphrase,int(size))

@then(u'I have to call PKCS7 padding of content to {size} bytes block size')
def step_impl(context, size):
    context.content = AES.pad(context.content)

@then(u'I have to encrypt the resulted content with the resulted passphrase using AES')
def step_impl(context):
    context.input = AES(context.passphrase).encrypt(context.content)

@then(u'I have to encode encrypted content with Base64')
def step_impl(context):
    context.result = context.input

