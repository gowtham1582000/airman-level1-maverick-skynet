import { useContext } from "react";
import { AuthContext } from "../auth/AuthContext";
import { Link } from "react-router-dom";

export default function Navbar() {

  const authContext = useContext(AuthContext);

  if (!authContext) return null;

  const { user, logout } = authContext;

  return (
    <nav style={styles.nav}>

      <div>
        <Link to="/">Home</Link>

        {!user && (
          <Link to="/login"> Login</Link>
        )}

        {user?.role === "admin" && (
          <Link to="/admin"> Admin Dashboard</Link>
        )}

        {user?.role === "instructor" && (
          <Link to="/instructor"> Instructor Dashboard</Link>
        )}

        {user?.role === "student" && (
          <Link to="/student"> Student Dashboard</Link>
        )}

      </div>

      {user && (
        <button onClick={logout}>
          Logout ({user.role})
        </button>
      )}

    </nav>
  );
}

const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    padding: "10px",
    background: "#111",
    color: "white"
  }
};