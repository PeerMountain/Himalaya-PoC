# -- FILE: features/steps/example_steps.py
import os
from behave import given, when, then, step

from graphene.test import Client
from API.schema import schema
from settings import VERSION_NAME, VERSION_CODE, BUILD_NUMBER

@given('Teleferic current version is <current_version>')
def step_impl(context):
    context.current_version = {
        'data': {
            'teleferic': {
                'version': {
                    'name': VERSION_NAME,
                    'code': VERSION_CODE,
                    'buildNumber': BUILD_NUMBER
                }
            }
        }
    }

@when('I query the current version of Teleferic')
def step_impl(context):
    context.executed = context.client.execute('''
        query {
            teleferic{
                version{
                    name
                    code
                    buildNumber
                }
            }
        }
    ''')

@then('the current version should match')
def step_impl(context):
    assert context.executed == context.current_version