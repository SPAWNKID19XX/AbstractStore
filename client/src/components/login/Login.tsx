import styles from './Login.module.css'
import {useNavigate} from 'react-router-dom';
import {useState} from "react";
import {login} from "../../utils/auth.ts";


const LoginForm = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');


    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');
        try {
            const tokens = await login({email, password});
            localStorage.setItem('access', tokens.access);
            localStorage.setItem('refresh', tokens.refresh);
            navigate('/');
        } catch (err) {
            console.error(err);
            setError("Email and Password not match");
        }
    }



    return (
        <div className={styles.formContainer}>
            <form className={styles.form} onSubmit={handleLogin}>
                <h1>Login Form</h1>
                <input
                    name="email"
                    type="email"
                    placeholder="Email"
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input
                    name="password"
                    type="password"
                    placeholder="Password"
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default LoginForm;
