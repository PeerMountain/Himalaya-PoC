class Query_Abstract():
  query = None
  variables = None

  def build(self):
    return {
      'query': str(self.query),
      'variables': self.variables
    }