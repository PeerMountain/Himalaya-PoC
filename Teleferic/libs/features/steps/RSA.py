# -- FILE: features/steps/RSA.py
import os
from behave import given, when, then, step

from Crypto.PublicKey import RSA as Key
from libs.RSA import RSA

@given('<privkey>')
def step_imp(context):
  context.privkey = Key.importKey(context.text)

@given('message as {message}')
def step_imp(context, message):
  context.message = message

@given('signature as {signature}')
def step_imp(context, signature):
  context.signature = signature

@when('I sign <message_hash> with <privkey> and store it on <current_sign>')
def step_imp(context):
  context.current_sign = RSA.sign(context.message, context.privkey)

@when('I compare <current_sign> with {given_sign}')
def step_imp(context, given_sign):
  context.result = context.current_sign == given_sign

@then('sign should be {result}')
def step_imp(context, result):
  assertion = result == 'valid'
  assert context.result == assertion