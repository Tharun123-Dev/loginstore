import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api/"
});

// ✅ Add access token
api.interceptors.request.use(config => {
  const token = localStorage.getItem("access"); // 🔥 FIXED

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});


// 🔥 HANDLE TOKEN EXPIRY
api.interceptors.response.use(
  response => response,

  error => {
    if (error.response && error.response.status === 401) {

      // Remove tokens
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");

      alert("Session expired. Please login again.");

      window.location.href = "/login";
    }

    return Promise.reject(error);
  }
);

export default api;