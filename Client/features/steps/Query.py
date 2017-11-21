# -- FILE: features/steps/Teleferic.py
import os
from behave import given, when, then, step

import requests
import base64

@given('following query')
def step_impl(context):
    context.query = context.text.strip()

@given('bootstap url {bootstrapNode}')
def step_impl(context, bootstrapNode):
    context.bootstrap_node = bootstrapNode.strip().encode()

@when('I send query to bootstrap node')
def step_impl(context):
    r = requests.post(context.bootstrap_node, data = {
        'query': context.query
    })
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
    context.b64decode_property_value = base64.b64decode(context.property_value)

@then('property value should be {wanted_value}')
def step_impl(context, wanted_value):
    assert context.property_value == wanted_value.strip().encode()

@then('decoded property should be')
def step_impl(context):
    assert context.text.strip().encode() == context.b64decode_property_value
