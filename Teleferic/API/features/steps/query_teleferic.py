# -- FILE: features/steps/example_steps.py
import os
from behave import given, when, then, step

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signer
from Crypto.Hash import RIPEMD
import base64
import time

@given('pubkey of Teleferic')
def step_impl(context):
    context.pubkey = RSA.importKey(context.text)

@when('send pubkey query of teleferic')
def step_impl(context):
    context.query = '''
        query{
            teleferic{
                pubkey
            }
        }
    '''
    context.executed = context.client.execute(context.query)

@then('we will have equal pubkey')
def step_impl(context):
    response_pubkey = RSA.importKey(context.executed['data']['teleferic']['pubkey'])
    assert context.pubkey.exportKey() == response_pubkey.exportKey()

@given('nickname is "{nickname}"')
def step_impl(context,nickname):
    context.nickname = nickname

@when('send nickname query of teleferic')
def step_impl(context):
    context.query = '''
        query{
            teleferic{
                nickname
            }
        }
    '''
    context.executed = context.client.execute(context.query)

@then('we will have equal nickname')
def step_impl(context):
    assert context.executed == {
        'data': {
            'teleferic': {
                'nickname': context.nickname
            }
        }
    }

@given('address is "{address}"')
def step_impl(context,address):
    context.address = address
    

@when('send address query of teleferic')
def step_impl(context):
    context.query = '''
        query{
            teleferic{
                address
            }
        }
    '''
    context.executed = context.client.execute(context.query)

@then('we will have equal address')
def step_impl(context):
    assert context.executed == {
        'data': {
            'teleferic': {
                'address': context.address
            }
        }
    }

@given('current timestamp as initial_timestamp')
def step_impl(context):
    context.initial_timestamp = time.time()

@when('we send signed timestap query of teleferic')
def step_impl(context):
    context.query = '''
        query{
            teleferic{
                timestamp{
                    timestamp
                    signature
                }
            }
        }
    '''
    context.executed = context.client.execute(context.query)

@then('we will have timestamp between initial_timestamp and current timestamp')
def step_impl(context):
    response_time = context.executed['data']['teleferic']['timestamp']['timestamp']
    assert context.initial_timestamp < response_time and time.time() > response_time

@then('we will have valid signature according Teleferic pubkey')
def step_impl(context):
    signer = Signer.new(context.pubkey)
    signature_raw = context.executed['data']['teleferic']['timestamp']['signature']
    signature = base64.b64decode(signature_raw)
    timestamp = str(context.executed['data']['teleferic']['timestamp']['timestamp'])
    timestamp_hash = RIPEMD.new(timestamp)
    assert signer.verify(timestamp_hash,signature)