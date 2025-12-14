import { Link } from "react-router-dom";
import { useAuth } from "../auth/AuthContext";

function Navbar() {
  const { user, logout } = useAuth();

  return (
    <nav style={{ padding: "1rem", borderBottom: "1px solid #ddd" }}>
      <Link to="/" style={{ marginRight: "1rem", fontWeight: "bold" }}>
        FitPlanHub
      </Link>

      {!user ? (
        <>
          <Link to="/login" style={{ marginRight: "1rem" }}>
            Login
          </Link>
          <Link to="/signup">Signup</Link>
        </>
      ) : (
        <>
          <span style={{ marginRight: "1rem" }}>
            {user.email}
          </span>

          <Link to="/feed" style={{ marginRight: "1rem" }}>
            Feed
          </Link>

          {user.role === "trainer" && (
            <Link to="/trainer/dashboard" style={{ marginRight: "1rem" }}>
              Dashboard
            </Link>
          )}

          <button onClick={logout}>Logout</button>
        </>
      )}
    </nav>
  );
}

export default Navbar;
