import { createContext, useState } from "react";
import type { ReactNode } from "react";


// 👇 Define User type (match backend JWT payload)
export interface User {
  email: string;
  role: "admin" | "instructor" | "student";
}


// 👇 Context type
interface AuthContextType {
  user: User | null;
  login: (userData: User, token: string) => void;
  logout: () => void;
}


// 👇 Create context with default undefined
export const AuthContext = createContext<AuthContextType | undefined>(undefined);


// 👇 Provider props type
interface Props {
  children: ReactNode;
}


export function AuthProvider({ children }: Props) {

  const [user, setUser] = useState<User | null>(() => {
    const storedUser = localStorage.getItem("user");
    return storedUser ? JSON.parse(storedUser) : null;
  });


  const login = (userData: User, token: string) => {
    localStorage.setItem("token", token);
    localStorage.setItem("user", JSON.stringify(userData));
    setUser(userData);
  };


  const logout = () => {
    localStorage.clear();
    setUser(null);
  };


  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}