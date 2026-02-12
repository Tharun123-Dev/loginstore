import { useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

const Signup = () => {

  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: ""
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSignup = async () => {
    try {
      const response = await api.post("signup/", formData);
      alert(response.data.message);
      navigate("/login");
    } catch {
      alert("Signup failed");
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h2>Create Account</h2>

        <input name="username" placeholder="Username" onChange={handleChange} />
        <input name="email" placeholder="Email" onChange={handleChange} />
        <input type="password" name="password" placeholder="Password" onChange={handleChange} />

        <button onClick={handleSignup}>Signup</button>
      </div>
    </div>
  );
};

export default Signup;
