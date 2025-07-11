import styles from './Login.module.css'
import React, {useState} from "react";
import {AxiosError} from "axios";
import {login} from "../../api/auth.ts";


const Login = () => {

    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        setFormData(prev => ({...prev, [e.target.name]: e.target.value}));
    };

    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);
        setLoading(true);
        try {
            await login(formData);
            alert('User Logged');
        } catch (err: unknown) {
            const error = err as AxiosError;

            if (error.response) {
                setError(error.response.data as string);
            } else {
                setError('Unknown error. Please try again later. If the problem persists, contact the administrator.');
            }
        } finally {
            setLoading(false);
        }
    };


    return (
        <>
            <div className={styles.formContainer}>
                <form className={styles.form} onSubmit={handleSubmit}>
                    <h1>Login Form</h1>
                    <input name="email" type="email" placeholder="Email" required value={formData.email}
                           onChange={handleChange}/>
                    <input name="password" type="password" placeholder="Password" required value={formData.password}
                           onChange={handleChange}/>
                    {error && <p style={{color: 'red'}}>{JSON.stringify(error)}</p>}
                    <button type="submit" disabled={loading}>{loading ? 'Submiting...' : 'Login'}</button>
                </form>
            </div>

        </>
    );
};

export default Login;