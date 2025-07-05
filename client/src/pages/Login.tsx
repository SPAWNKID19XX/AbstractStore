import React, { useState, useContext } from 'react';
//import { login } from '../api/auth';
//import { AuthContext } from '../context/AuthContext';

const Login: React.FC = () => {
  //const { setAuthData } = useContext(AuthContext);

  const [formData, setFormData] = useState({
    email: '',
    password: '',
   
  });

  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      await Login(formData);
      //setAuthData?.({ /* можно сразу залогинить или показать сообщение */ });
      alert('Регистрация прошла успешно!');
    } catch (err: any) {
      setError(err.response?.data || 'Ошибка регистрации');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="email" type="email" placeholder="Email" required value={formData.email} onChange={handleChange} />
      <input name="password" type="password" placeholder="Пароль" required value={formData.password} onChange={handleChange} />
      
      {error && <p style={{ color: 'red' }}>{JSON.stringify(error)}</p>}
      <button type="submit" disabled={loading}>{loading ? 'Загрузка...' : 'Зарегистрироваться'}</button>
    </form>
  );
};

export default Login;