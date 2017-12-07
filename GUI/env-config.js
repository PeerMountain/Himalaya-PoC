var vars

switch (process.env.NODE_ENV) {
  case 'production':
    vars = {
      'process.env.BACKEND_URL': 'https://api.centraldefondos.com.ar',
      'process.env.DISABLE_ANALYTICS': '0',
      'process.env.DISABLE_INTERCOM': '0'
    }
    break
  case 'staging':
    vars = {
      'process.env.BACKEND_URL': 'https://api.dev.centraldefondos.com.ar',
      'process.env.DISABLE_ANALYTICS': '1',
      'process.env.DISABLE_INTERCOM': '1'
    }
    break
  default:
    vars = {
      'process.env.BACKEND_URL': 'http://localhost:8000',
      'process.env.DISABLE_ANALYTICS': '1',
      'process.env.DISABLE_INTERCOM': '1'
    }
}

module.exports = vars