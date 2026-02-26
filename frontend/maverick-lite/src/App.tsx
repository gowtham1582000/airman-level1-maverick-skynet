import Admin from "./pages/admin";
import Instructor from "./pages/Instructor";
import Student from "./pages/student";
import Login from "./pages/Login";
import ProtectedRoute from "./components/ProtectedRoute";
import { AuthProvider } from "./auth/AuthContext";
import Navbar from "./components/Navbar";
import { BrowserRouter, Link, Routes, Route } from "react-router-dom";

function App() {

  return (
    <AuthProvider>
      <BrowserRouter>
        <Navbar />
        <nav style={{ padding: 10 }}>
          <Link to="/">Home</Link> |{" "}
          <Link to="/login">Login</Link> |{" "}
          <Link to="/admin">Admin</Link> |{" "}
          <Link to="/instructor">Instructor</Link> |{" "}
          <Link to="/student">Student</Link>
        </nav>

        <Routes>

          <Route path="/" element={<h2>Welcome to AIRMAN Core</h2>} />
          <Route path="/login" element={<Login />} />

          <Route
            path="/admin"
            element={
              <ProtectedRoute allowedRole="admin">
                <Admin />
              </ProtectedRoute>
            }
          />

          <Route
            path="/instructor"
            element={
              <ProtectedRoute allowedRole="instructor">
                <Instructor />
              </ProtectedRoute>
            }
          />

          <Route
            path="/student"
            element={
              <ProtectedRoute allowedRole="student">
                <Student />
              </ProtectedRoute>
            }
          />

        </Routes>

      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;