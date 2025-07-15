import api from '../api/api'
import axios from "axios";

export interface TokenResponse {
    access: string;
    refresh: string;
}

export interface LoginData {
    email: string;
    password: string;
}

export interface UserData {
    email: string;
    password: string;
    first_name: string;
    last_name: string;
    is_admin: boolean;
    phone: string;
    address: string;
    gender: string;
    date_of_birth: string;
    is_active: boolean;
    is_staff: boolean;
    is_superuser: boolean;
    tax_id: string;
}

export const isAuthenticated = (): boolean => {
    const token = localStorage.getItem("access");
    return !!token;
};

export const login = async (data: LoginData) => {
    const response = await api.post<TokenResponse>('users/token/', data);
    localStorage.setItem("access", response.data.access);
    localStorage.setItem("refresh", response.data.refresh);
    return response.data;
}

export const logout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
}

export const myData = async (): Promise<UserData> => {
  const token = localStorage.getItem("access");

  const response = await api.get<UserData>('users/me/', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
};





