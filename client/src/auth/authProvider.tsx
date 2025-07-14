import React, { useEffect, useState, type ReactNode } from 'react';
import { AuthContext } from './authContext';
import type { AuthContextType, User } from './authContext';
import { login as apiLogin, getCurrentUser, refreshAccessToken } from '../api/auth';

interface Props {
  children: ReactNode;
}

export const AuthProvider: React.FC<Props> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const initializeAuth = async () => {
      const token = await refreshAccessToken();
      if (token) {
        const currentUser = await getCurrentUser();
        setUser(currentUser);
      }
    };
    initializeAuth();
  }, []);

 const login = async (email: string, password: string) => {
  const response = await apiLogin({ email, password });
  localStorage.setItem('access', response.data.access);
  localStorage.setItem('refresh', response.data.refresh);

  const currentUser = await getCurrentUser();
  setUser(currentUser);
};

  const logout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    setUser(null);
  };

  const updateUser = (newUser: User) => {
    setUser(newUser);
  };

  const contextValue: AuthContextType = {
    user,
    login,
    logout,
    updateUser,
  };

  return <AuthContext.Provider value={contextValue}>{children}</AuthContext.Provider>;
};
