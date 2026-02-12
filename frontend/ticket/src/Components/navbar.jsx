import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="navbar">
      <h2>My Website</h2>
      <div className="nav-links">
        <Link to="/profile">Profile</Link>
        <Link to="/login">Login</Link>
        <button 
      onClick={() => window.location.href = "http://localhost:8000/admin/"} 
      style={styles.navBtn}
    >
      Admin Panel
    </button>
      </div>
    </div>
  );
};

export default Navbar;
