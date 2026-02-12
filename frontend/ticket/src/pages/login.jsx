import { useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

const Login = () => {

  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: "",
    password: ""
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleLogin = async () => {
    try {
      const response = await api.post("login/", formData);
      if (response.data.message === "Login successful") {
        navigate("/profile");
      }
    } catch {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h2>Login</h2>

        <input name="username" placeholder="Username" onChange={handleChange} />
        <input type="password" name="password" placeholder="Password" onChange={handleChange} />

        <button onClick={handleLogin}>Login</button>
      </div>
    </div>
  );
};

export default Login;
