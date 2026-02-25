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
      const res = await api.post("jwt-login/", formData);

      console.log("Login response 👉", res.data); // 🔍 Debug

      // ✅ Handle both response formats
      const accessToken = res.data.access || res.data.access_token;
      const refreshToken = res.data.refresh || res.data.refresh_token;

      if (!accessToken) {
        alert("❌ Token not received from server");
        return;
      }

      // ✅ Save tokens
      localStorage.setItem("access", accessToken);
      localStorage.setItem("refresh", refreshToken);

      alert("Login successful ✅");

      navigate("/profile");

    } catch (error) {
      console.log(error);
      alert("Invalid credentials ❌");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h2>Login</h2>

        <input
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          style={styles.input}
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          style={styles.input}
        />

        <button onClick={handleLogin} style={styles.button}>
          Login
        </button>
      </div>
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh"
  },
  card: {
    padding: 30,
    borderRadius: 10,
    boxShadow: "0 0 10px rgba(0,0,0,0.1)",
    width: 300,
    textAlign: "center"
  },
  input: {
    width: "100%",
    padding: 10,
    margin: "10px 0",
    borderRadius: 5,
    border: "1px solid #ccc"
  },
  button: {
    padding: 10,
    width: "100%",
    background: "#007bff",
    color: "#fff",
    border: "none",
    borderRadius: 5,
    cursor: "pointer"
  }
};

export default Login;