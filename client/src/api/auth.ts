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

export const login = (data: LoginData) => {
    return axios.post(`${BASE_URL}/token/`, data);
};

export const signup = (data: SignupData) => {
    return axios.post(`${BASE_URL}/signup/`, data);
};