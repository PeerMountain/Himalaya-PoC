import React from 'react'
import Identity from '../tools/identity'
import Router from 'next/router'

export default class extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      loading: true
    }
  }

  componentWillUpdate(nextProps, nextState) {
    if('privkey' in nextProps){
      let result = Identity.importKey(nextProps.privkey())
      if('onLoad' in nextProps){
        nextProps.onLoad(Identity)
      }
    }
  }
  

  componentDidMount() {
    Identity.remember()
    /*
    if(!Identity.load && this.props.validate){
      return Router.push('/')
    }
    */
    this.setState({
      loading: false
    })
  }
  
  render(){
    const { loading } = this.state
    const { validate } = this.props
    if(!loading){
      if(Identity.load || !validate ){
        return this.props.children
      }else{
        return <div>No access.</div>  
      }
    }else{
      return <div>Loading...</div>
    }
  }
}