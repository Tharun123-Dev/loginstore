import { useEffect, useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

const Profile = () => {

  const [user, setUser] = useState(null);
  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");
  const [trains, setTrains] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const res = await api.get("profile/");
        setUser(res.data);
      } catch {
        navigate("/login");
      }
    };

    fetchProfile();
  }, []);

  const handleSearch = async () => {
    try {
      const res = await api.get(
        `search-trains/?source=${source}&destination=${destination}`
      );
      setTrains(res.data);
    } catch {
      alert("Search failed");
    }
  };

  return (
    <div style={styles.page}>
      <div style={styles.container}>
        <div style={styles.card}>

          {user ? (
            <>
              <h2>Welcome, {user.username} 👋</h2>
              <h2>Here, This is for u Isrtc Booking:</h2>
              <p><b>Email:</b> {user.email}</p>

              <hr style={{ margin: "20px 0" }} />

              <h3>Search Trains 🚆</h3>

              <input
                placeholder="From"
                value={source}
                onChange={(e) => setSource(e.target.value)}
              />

              <input
                placeholder="To"
                value={destination}
                onChange={(e) => setDestination(e.target.value)}
              />

              <button onClick={handleSearch}>Search</button>

              <div style={{ marginTop: "20px" }}>
                {trains.length > 0 ? (
                  trains.map((train, index) => (
                    <div key={index} style={styles.resultCard}>
                      <h4>{train.train_number} - {train.train_name}</h4>
                      <p>{train.source} ➝ {train.destination}</p>
                      <p>Departure: {train.departure_time}</p>
                      <p>Arrival: {train.arrival_time}</p>
                    </div>
                  ))
                ) : (
                  <p>No trains found</p>
                )}
              </div>
            </>
          ) : (
            <p>Loading...</p>
          )}

        </div>
      </div>
    </div>
  );
};

const styles = {
  page: {
    minHeight: "100vh",
    background: "linear-gradient(135deg, #4e73df, #1cc88a)",
    display: "flex",
    justifyContent: "center",
    alignItems: "center"
  },
  card: {
    background: "white",
    padding: "40px",
    width: "450px",
    borderRadius: "10px",
    textAlign: "center"
  },
  resultCard: {
    background: "#f8f9fc",
    padding: "10px",
    marginTop: "10px",
    borderRadius: "6px",
    textAlign: "left"
  }
};

export default Profile;
