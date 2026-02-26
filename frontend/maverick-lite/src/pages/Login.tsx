import api from "../api/axios";
import { useContext } from "react";
import { AuthContext } from "../auth/AuthContext";
import type { User } from "../auth/AuthContext";
import { useForm } from "react-hook-form";

// 👇 form data type
interface LoginForm {
  email: string;
  password: string;
}

export default function Login() {

  const { register, handleSubmit, formState: { errors } } = useForm<LoginForm>();

  const authContext = useContext(AuthContext);

  if (!authContext) {
    throw new Error("AuthContext not found");
  }

  const { login } = authContext;


  const onSubmit = async (data: LoginForm) => {

    const res = await api.post("/auth/login", data);

    const user: User = res.data.user;
    const token: string = res.data.access_token;

    login(user, token);
  };

  return (

    <form onSubmit={handleSubmit(onSubmit)}>

      <input
        {...register("email", { required: true })}
        placeholder="Email"
      />

      {errors.email && <p>Email required</p>}

      <input
        type="password"
        {...register("password", { required: true, minLength: 6 })}
        placeholder="Password"
      />

      {errors.password && <p>Password min 6</p>}

      <button type="submit">Login</button>

    </form>

  );
}