import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/v1/users';

interface LoginData {
    email: string;
    password: string;
}

interface SignupData {
    email: string;
    password: string;
    first_name: string;
    last_name: string;
    phone: string;
    address: string;
    gender: string;
    date_of_birth: Date | string;
    tax_id: string;
}

export const refreshAccessToken = async () => {
    const refreshToken = localStorage.getItem('refresh');
    if (!refreshToken) return null;

    try {
        const response = await axios.post(`${BASE_URL}/token/refresh/`, {
            refresh: refreshToken,
        });

        localStorage.setItem('access', response.data.access);

        // Выводим токены в консоль
        console.log('Access token:', response.data.access);
        console.log('Refresh token:', refreshToken);

        return response.data.access;
    } catch (error) {
        console.error('Refresh token error:', error);
        return null;
    }
};


export const getCurrentUser = async () => {
    const accessToken = localStorage.getItem('access');
    if (!accessToken) return null;

    try {
        const response = await axios.get(`${BASE_URL}/me/`, {
            headers: {
                Authorization: `Bearer ${accessToken}`,
            },
        });
        console.log(response.data)
        return response.data;
    } catch (error) {
        console.error('Error fetching current user:', error);
        return null;
    }
};

export const login = (data: LoginData) => {
  return axios.post(`${BASE_URL}/token/`, data);
};

export const signup = (data: SignupData) => {
    return axios.post(`${BASE_URL}/signup/`, data);
};

export const logout = () => {
  localStorage.removeItem('access');
  localStorage.removeItem('refresh');
};