import { useState } from 'react'
import './App.css'
import logo from "./assets/logo.png";

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <img className='logo' src={logo} alt="Logo" width="150" /> 
      </div>
      <h1>Education Order</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button> 
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
