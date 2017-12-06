class GetIdentity():
    filters = ['address', 'nickname', 'pubkey']
    attributes = ['address', 'nickname', 'pubkey']

    @staticmethod
    def by_nickname(nickname, attributes=attributes):
        query = '''
      query{
        persona(
          nickname: "%s"
        ){
          %s
        }
      }
    ''' % (nickname, ','.join(attributes))
        return {
            'query': query
        }

    @staticmethod
    def by_address(address, attributes=attributes):
        query = '''
      query{
        persona(
          address: "%s"
        ){
          %s
        }
      }
    ''' % (address, ','.join(attributes))
        return {
            'query': query
        }
