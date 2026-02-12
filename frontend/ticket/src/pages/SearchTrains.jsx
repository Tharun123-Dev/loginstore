import { useState } from "react";
import api from "../services/api";
import { Link } from "react-router-dom";

const SearchTrains = () => {

  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");
  const [trains, setTrains] = useState([]);

  const handleSearch = async () => {
    try {
      const res = await api.get(
        `search-trains/?source=${source}&destination=${destination}`
      );
      setTrains(res.data);
    } catch (error) {
      console.log("Search failed");
    }
  };

  return (
    <div style={styles.page}>

      <div style={styles.navbar}>
        <h2>IRCTC Booking Portal</h2>
        <Link to="/profile" style={styles.link}>Dashboard</Link>
      </div>

      <div style={styles.container}>
        <div style={styles.card}>
          <h2>Search Trains 🚆</h2>

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

        </div>
      </div>

    </div>
  );
};

const styles = {

  page: {
    minHeight: "100vh",
    background: "linear-gradient(135deg, #4e73df, #1cc88a)",
    fontFamily: "Arial"
  },

  navbar: {
    display: "flex",
    justifyContent: "space-between",
    padding: "15px 40px",
    backgroundColor: "#222",
    color: "white"
  },

  link: {
    color: "white",
    textDecoration: "none",
    fontWeight: "bold"
  },

  container: {
    display: "flex",
    justifyContent: "center",
    marginTop: "40px"
  },

  card: {
    background: "white",
    padding: "30px",
    width: "450px",
    borderRadius: "10px",
    textAlign: "center"
  },

  resultCard: {
    background: "#f8f9fc",
    padding: "15px",
    marginTop: "10px",
    borderRadius: "6px",
    textAlign: "left"
  }
};

export default SearchTrains;
