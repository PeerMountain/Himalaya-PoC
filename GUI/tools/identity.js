let JSEncrypt = false
let key

class Identity{
  constructor(){
    this.load = false
  }
  remember(){
    const aux_key = localStorage.getItem('key')
    if(aux_key){
      this.importKey(aux_key)
    }
  }
  importKey(privkey,remember = false){
    if(JSEncrypt == false){
      JSEncrypt = require('jsencrypt').JSEncrypt
      key = new JSEncrypt()
    }
    try {
      key.setKey(privkey)
      if(remember){
        localStorage.setItem('key',privkey)
      }
      this.load = true
      return true
    } catch (error) {
      this.load = false
      return false
    }
  }
}

const identity = new Identity()

export default identity