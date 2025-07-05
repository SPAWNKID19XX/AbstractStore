import React, { createContext, useState} from 'react';
import type { ReactNode } from 'react';
interface AuthData {
  accessToken: string | null;
  refreshToken: string | null;
  user: any | null;  // можно типизировать под твою структуру пользователя
}

interface AuthContextProps {
  authData: AuthData;
  setAuthData: (data: AuthData) => void;
  logout: () => void;
}

export const AuthContext = createContext<AuthContextProps>({
  authData: { accessToken: null, refreshToken: null, user: null },
  setAuthData: () => {},
  logout: () => {}
});

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [authData, setAuthDataState] = useState<AuthData>(() => {
    // Попытка достать токены из localStorage при инициализации
    const accessToken = localStorage.getItem('accessToken');
    const refreshToken = localStorage.getItem('refreshToken');
    const user = localStorage.getItem('user');
    return {
      accessToken,
      refreshToken,
      user: user ? JSON.parse(user) : null
    };
  });

  const setAuthData = (data: AuthData) => {
    setAuthDataState(data);
    if (data.accessToken) {
      localStorage.setItem('accessToken', data.accessToken);
    } else {
      localStorage.removeItem('accessToken');
    }
    if (data.refreshToken) {
      localStorage.setItem('refreshToken', data.refreshToken);
    } else {
      localStorage.removeItem('refreshToken');
    }
    if (data.user) {
      localStorage.setItem('user', JSON.stringify(data.user));
    } else {
      localStorage.removeItem('user');
    }
  };

  const logout = () => {
    setAuthData({ accessToken: null, refreshToken: null, user: null });
  };

  return (
    <AuthContext.Provider value={{ authData, setAuthData, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
