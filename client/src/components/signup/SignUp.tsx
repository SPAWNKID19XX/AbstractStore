import React, {useState} from 'react';
import {signup} from '../../api/auth.ts';
import {useAuth} from '../../auth/authContext.ts';
import {AxiosError} from 'axios';

const SignUp: React.FC = () => {

    interface SignUpGenderField {
        id: number;
        value: string;
        label: string;
    }

    const genderFields: SignUpGenderField[] = [
        {id: 1, value: 'select', label: 'Select'},
        {id: 2, value: 'male', label: 'Male'},
        {id: 3, value: 'female', label: 'Female'},
    ];

    const {updateUser} = useAuth();

    const [formData, setFormData] = useState({
        email: '',
        password: '',
        first_name: '',
        last_name: '',
        phone: '',
        address: '',
        gender: '',
        date_of_birth: '',
        tax_id: ''
    });

    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        setFormData(prev => ({...prev, [e.target.name]: e.target.value}));
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);
        setLoading(true);
        try {
            const response = await signup(formData);
            const {access, refresh, user} = response.data;

            localStorage.setItem('access', access);
            localStorage.setItem('refresh', refresh);
            updateUser(user);

            alert('Регистрация прошла успешно!');
        } catch (err: unknown) {
            const error = err as AxiosError;

            if (error.response) {
                setError(error.response.data as string);
            } else {
                setError('Неизвестная ошибка');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input name="email" type="email" placeholder="Email" required value={formData.email}
                   onChange={handleChange}/>
            <input name="password" type="password" placeholder="Пароль" required value={formData.password}
                   onChange={handleChange}/>
            <input name="first_name" placeholder="Имя" value={formData.first_name} onChange={handleChange}/>
            <input name="last_name" placeholder="Фамилия" value={formData.last_name} onChange={handleChange}/>
            <input name="phone" placeholder="Телефон" value={formData.phone} onChange={handleChange}/>
            <input name="address" placeholder="Адрес" value={formData.address} onChange={handleChange}/>
            <select name="gender" value={formData.gender} onChange={handleChange}>
                {genderFields.map(g => (
                    <option key={g.value} value={g.value}>
                        {g.label}
                    </option>
                ))}
            </select>
            <input name="date_of_birth" type="date" value={formData.date_of_birth} onChange={handleChange}/>
            <input name="tax_id" placeholder="ИНН" value={formData.tax_id} onChange={handleChange}/>

            {error && <p style={{color: 'red'}}>{error}</p>}
            <button type="submit" disabled={loading}>{loading ? 'Загрузка...' : 'Зарегистрироваться'}</button>
        </form>
    );
};

export default SignUp;
