# -- FILE: features/steps/Teleferic.py
import os
from behave import given, when, then, step

import requests
import base64
import msgpack

from TelefericClient.Cryptography import RSA

@given('following query')
def step_impl(context):
    context.query = context.text.strip()

@given('bootstrap node url {bootstrapNode}')
def step_impl(context, bootstrapNode):
    context.bootstrap_node = bootstrapNode.strip().encode()

@when('I send query to bootstrap node')
def step_impl(context):
    r = requests.post(context.bootstrap_node, data = {
        'query': context.query
    })
    context.query_response = r.json()

@when(u'send mutation with variables to bootstrap node <bootstrapNode>')
def step_impl(context):
    r = requests.post(context.bootstrap_node, data = {
        'query': context.mutation,
        'variables': context.variables
    })
    print(r.json())
    context.query_response = r.json()

@when('get property {property_path} from query response')
def step_impl(context, property_path):
    parts = property_path.split('.')
    data = context.query_response
    for part in parts:
        data = data.get(part)    
    context.property_value = data.encode()

@when('decode property with Base64')
def step_impl(context):
    context.property = base64.b64decode(context.property_value)

@then('property value should be {wanted_value}')
def step_impl(context, wanted_value):
    assert context.property_value == wanted_value.strip().encode()

@then('decoded property should be')
def step_impl(context):
    assert context.text.strip().encode() == context.property


@given('bootstrap node pubkey <bootstrapNodePubkey>')
def step_impl(context):
    context.execute_steps("""
        Given following query
        '''
        query{
            teleferic{
                persona{
                pubkey
                }
            }
        }
        '''
        And bootstrap node url """+context.bootstrap_node.decode('utf-8')+"""
        When I send query to bootstrap node
        And get property data.teleferic.persona.pubkey from query response
        And decode property with Base64
    """)
    context.bootstrapNodePubkey = RSA(context.property.decode('utf-8'))

@when(u'unpack property with Message Pack')
def step_impl(context):
    context.property = msgpack.unpackb(context.property)

@then(u'result should have {property_key} property')
def step_impl(context, property_key):
    assert property_key.strip().encode() in context.property

@then(u'signature should be valid for timestamp')
def step_impl(context):
    assert context.bootstrapNodePubkey.verify(context.property[b'timestamp'],context.property[b'signature'])
