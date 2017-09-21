# -- FILE: features/steps/example_steps.py
import os
from behave import given, when, then, step

from graphene.test import Client
from API.schema import schema
from settings import VERSION_NAME, VERSION_CODE, BUILD_NUMBER

@given('we have version query')
def step_impl(context):
    context.client = Client(schema)
    pass

@when('we require current version')
def step_impl(context):  # -- NOTE: number is converted into integer
    context.executed = context.client.execute('''
        query {
            version{
                name
                code
                buildNumber
            }
        }
    ''')

@then('response data is equal to current version')
def step_impl(context):
    assert context.executed == {
        'data': {
            'version': {
                'name': VERSION_NAME,
                'code': VERSION_CODE,
                'buildNumber': BUILD_NUMBER
            }
        }
    }