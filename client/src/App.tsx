import './App.css'
import NavBar from './components/NavBar/NavBar';
import Footer from './components/Footer/Footer';
import Login from './pages/login/Login';
import SignUp from './pages/signup/SignUp';
import {Route, Routes} from "react-router-dom";

import './i18n.js'

function App() {

    return (
        <div className="MainPaig">
            <NavBar />

            <Routes>
                <Route path="/login" element={
                    <>
                        <Login/>
                    </>
                }/>
            </Routes>



            <Routes>
                <Route path="/signup" element={
                    <>
                        <SignUp/>
                    </>
                }/>
            </Routes>

            <Footer />
        </div>
    )
}

export default App
