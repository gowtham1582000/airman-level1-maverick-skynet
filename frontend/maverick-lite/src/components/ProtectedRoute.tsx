import type { JSX } from "react";
import { Navigate } from "react-router-dom";

interface Props {
  allowedRole: string;
  children: JSX.Element;
}

export default function ProtectedRoute({ allowedRole, children }: Props){

  const user = JSON.parse(localStorage.getItem("user") || "null");

  if(!user) return <Navigate to="/login" />;

  if(user.role !== allowedRole)
    return <Navigate to="/" />;

  return children;
}