import React, {Component} from 'react'
import fetch from 'isomorphic-fetch'

import dynamic from 'next/dynamic'
const GraphiQL = dynamic(import('graphiql'), {
  ssr: false
})

import Router from 'next/router'

import Mayre from 'mayre'

import {ENDPOINT} from '../settings'


class Index extends Component {
  constructor (props, context) {
    super(props, context)
    this.state = {
      ready: false
    }
  }

  componentWillMount() {
    this.setState({
      ready: true
    })
  }

  graphQLFetcher = graphQLParams => {
    const request = {
      ...graphQLParams,
      'sign': this.refs.sign.value
    }
    return fetch(ENDPOINT, {
      method: 'post',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(request),
    }).then(response => response.json());
  }

  render () {
    const { ready } = this.state
    return (
      <div className="root">
        <div className="header">
          <h1 className="logo">Himalaya</h1>
          <div className="actions">
            <input ref="sign" value="" placeholder="Request Sign"/>
          </div>    
        </div>
        <div className="explorer">
          <Mayre
            of={
              <GraphiQL fetcher={this.graphQLFetcher} />
            }
            when={ready}
          />
        </div>
        <style jsx>{`
          .root{
            height: 100vh;
            display: flex;
            flex-direction: column;
          }
          .header{
            display: flex;
            justify-content: flex-end;
            align-items: center;
          }
          .header .actions{
            flex: 1;
            display: flex;
            justify-content: flex-end;
          }
          .explorer{
            flex: 1;
          }
        `}</style>
      </div>
    )
  }
}

export default Index
