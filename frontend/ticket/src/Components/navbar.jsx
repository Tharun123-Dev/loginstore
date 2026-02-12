import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="navbar">
      <h2>My Website</h2>
      <div className="nav-links">
        <Link to="/profile">Profile</Link>
        <Link to="/login">Login</Link>
      </div>
    </div>
  );
};

export default Navbar;
