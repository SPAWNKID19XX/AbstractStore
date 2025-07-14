import './App.css'
import NavBar from './components/NavBar/NavBar';
import Footer from './components/Footer/Footer';
import Login from './components/login/Login';
import SignUp from './components/signup/SignUp';
import { Route, Routes } from 'react-router-dom';

import './i18n.js';

function App() {
  return (
    <div className="MainPaig">
      <NavBar />

      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
      </Routes>

      <Footer />
    </div>
  );
}

export default App;
