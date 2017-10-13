# -- FILE: features/steps/example_steps.py
import os
from behave import given, when, then, step

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signer
from Crypto.Hash import RIPEMD
import base64
import time

@given('Teleferic has pubkey')
def step_impl(context):
    context.pubkey = RSA.importKey(context.text)

@when('I query the pubkey of Teleferic')
def step_impl(context):
    context.query = '''
        query{
            teleferic{
                persona{
                    pubkey
                }
            }
        }
    '''
    context.executed = context.client.execute(context.query)

@then('the pubkey should match')
def step_impl(context):
    response_pubkey = RSA.importKey(context.executed['data']['teleferic']['persona']['pubkey'])
    assert context.pubkey.exportKey() == response_pubkey.exportKey()

@given('Teleferic nickname is "{nickname}"')
def step_impl(context,nickname):
    context.nickname = nickname

@when('I query the nickname of Teleferic')
def step_impl(context):
    context.query = '''
        query{
            teleferic{
                persona{
                    nickname
                }
            }
        }
    '''
    context.executed = context.client.execute(context.query)

@then('the nickname should match')
def step_impl(context):
    assert context.executed == {
        'data': {
            'teleferic': {
                'persona': {
                    'nickname': context.nickname
                }
            }
        }
    }

@given('Teleferic address is "{address}"')
def step_impl(context,address):
    context.address = address
    

@when('I query the address of Teleferic')
def step_impl(context):
    context.query = '''
        query{
            teleferic{
                persona{
                    address
                }
            }
        }
    '''
    context.executed = context.client.execute(context.query)

@then('the addresses should match')
def step_impl(context):
    assert context.executed == {
        'data': {
            'teleferic': {
                'persona':{
                    'address': context.address
                }
            }
        }
    }

@given('Teleferic has pubkey <pubKey>')
def step_impl(context):
    context.execute_steps('''
        When I query the pubkey of Teleferic
    ''')
    context.pubkey = RSA.importKey(context.executed['data']['teleferic']['persona']['pubkey'])

@given('the current timestamp is <initial_timestamp>')
def step_impl(context):
    context.initial_timestamp = time.time()

@when('I query a signed timestap of Teleferic')
def step_impl(context):
    context.query = '''
        query{
            teleferic{
                signedTimestamp{
                    timestamp
                    signature
                }
            }
        }
    '''
    context.executed = context.client.execute(context.query)

@then('the timestamp will be between <initial_timestamp> and current timestamp')
def step_impl(context):
    response_time = context.executed['data']['teleferic']['signedTimestamp']['timestamp']
    assert context.initial_timestamp < response_time and time.time() > response_time

@then('the message should have a valid signature according to Teleferic pubkey')
def step_impl(context):
    signer = Signer.new(context.pubkey)
    signature_raw = context.executed['data']['teleferic']['signedTimestamp']['signature']
    signature = base64.b64decode(signature_raw)
    timestamp = str(context.executed['data']['teleferic']['signedTimestamp']['timestamp'])
    timestamp_hash = RIPEMD.new(timestamp)
    assert signer.verify(timestamp_hash,signature)