from django.test import TestCase
from graphene.test import Client

from API.schema import schema

from settings import VERSION_NAME, VERSION_CODE, BUILD_NUMBER


class VersionTestCase(TestCase):
  def setUp(self):
    self.client = Client(schema)

  def test_valid_result(self):
    executed = self.client.execute('''
      query {
        version{
          name
          code
          buildNumber
        }
      }
    ''')

    assert executed == {
      'data': {
        'version': {
          'name': VERSION_NAME,
          'code': VERSION_CODE,
          'buildNumber': BUILD_NUMBER
        }
      }
    }