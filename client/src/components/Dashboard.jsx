import React, { useEffect, useState } from "react";
import axios from "../utils/api";
import "../styles/Dashboard.css"; 

const Dashboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("/api/data").then((response) => setData(response.data));
  }, []);

  return (
    <div className="dashboard-container">
      <div className="dashboard-header">
        <h2>Real-Time Data</h2>
      </div>
      <div className="dashboard-content">
        <pre className="data-display">{JSON.stringify(data, null, 2)}</pre>
      </div>
    </div>
  );
};

export default Dashboard;
