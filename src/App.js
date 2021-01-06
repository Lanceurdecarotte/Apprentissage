import React from "react";
import logo from './logo.svg';
import './App.css';

class App extends React.Component
 {
  constructor(props) {
    super(props);
    this.state= {
      counter: 0,
    };
 } 
 render() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>{this.state.counter}</p>

        <button
        className="miel-pops"
          onClick={() => this.setState({counter: this.state.counter + 1})}
          >
            Count
          </button>

          <a
          className="App-link"
          href="https://www.instagram.com/rudy.fakhoury/"
          target="_blank"
          rel="noopener noreferrer"
        >
          <button className="App-link">My Insta</button>
        </a>
        
      </header>
    </div>
  );
 }
}

export default App;
