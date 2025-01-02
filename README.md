# 🌐 **Real-Time Digital Twin Dashboard with Omniverse USD Integration**

Welcome to the **Real-Time Digital Twin Dashboard** project! This repository is designed to provide a comprehensive solution for creating and integrating digital twins using **NVIDIA Omniverse USD**, **real-time data visualization**, and **state-of-the-art web technologies**. The documentation showcases what I learned from the video explanation and how to effectively build this project step-by-step.

---

## 📖 **What I Understood from the Video**

A digital twin is a **virtual replica** of a real-world system or environment, offering enhanced monitoring, optimization, and management capabilities. 

### **Core Examples from the Video**
1. **Manufacturing Industry**: 
   - Real-time alerts for 64 mapped assets.
   - Data integration for process optimization and feedback loop improvements.

2. **Smart Building Management**: 
   - Energy monitoring with 3D building models.
   - Predictive maintenance with ticketing and downtime analysis.
   - Environmental compliance and occupancy tracking.

### **Key Features of Digital Twin**
- **Monitor**: Real-time asset tracking and alerts.
- **Analyze**: Data-driven planning for optimization.
- **Optimize**: Energy, maintenance, and resource management.
- **Feedback Loop**: Continuous improvement with integrated analytics.

---

## 🛠️ **Tech Stack**

### **Chosen Technologies**
- **Frontend**: React.js
- **Backend**: Node.js + Express
- **Visualization**: NVIDIA Omniverse USD
- **Scripting**: Python (for Omniverse integration)

### **Why These Technologies?**
1. **React.js**: 
   - Component-based architecture for modular design.
   - Real-time state management using hooks.
2. **Node.js**: 
   - High-performance backend with scalable API routes.
   - Seamless integration with Python scripts and Omniverse.
3. **Omniverse USD**:
   - Industry-leading 3D visualization tools.
   - Real-time data mapping for digital twin environments.
4. **Python**:
   - Extensive libraries for data simulation and Omniverse scripting.

### **Best Alternatives**
- **Frontend**: Angular, Vue.js
- **Backend**: Django (Python), Flask
- **Visualization**: Unity3D, Unreal Engine
- **Mobile App Development**: React Native, Flutter

---

## 📂 **Folder Structure**

```plaintext
digital-twin/
├── omniverse/              # Python for Omniverse
│   ├── src/
│   │   ├── app.py               # Main application script
│   │   ├── twin_visualization.py # Handles loading USD models
│   │   ├── data_simulator.py    # Simulates real-time data
│   │   ├── ui.py                # Omniverse UI components
│   ├── templates/               # USD models for the digital twin
│   │   ├── factory.usda         # Industrial layout (from models pack)
│   │   ├── machines.usda        # Machine components
│   │   ├── warehouse.usda       # Warehouse/tower components
│   ├── requirements.txt         # Python dependencies
├── server/                 # Node.js Backend
│   ├── app.js                  # Node.js server
│   ├── routes/
│   │   ├── data.js             # Routes for real-time data API
│   ├── package.json            # Node.js dependencies
│   └── utils/
│       ├── omniverse.js        # Integrates with Omniverse Python scripts
├── client/                 # React Frontend
│   ├── public/                 # Static files
│   ├── src/
│   │   ├── App.js              # React entry point
│   │   ├── components/         # Reusable React components
│   │   │   ├── Dashboard.js    # Main dashboard for digital twin
│   │   ├── utils/
│   │   │   ├── api.js          # API calls to Node.js server
│   ├── package.json            # React dependencies
└── README.md                # Documentation
```

---

## 📸 **Images and Visuals**
1. **Omniverse USD Files**: Factory layouts, machine components, and 3D models.
2. **3D Model Placement**: Objects placed at various locations using Omniverse.
3. **Omniverse Connection**: Localhost integration with server.
4. **Real-Time Dashboard**: Real-time data visualization and USD model integration.
5. **Code Screenshots**: Omniverse scripts and React components.
6. **Maintenance Workflow**: Alerts, tickets, and predictive maintenance setup.
7. **Energy Monitoring**: HVAC and lighting system tracking in a smart building.
8. **Analytics Panel**: Long-term trends and bottleneck identification.

---

## 🚀 **Getting Started**

### **Installation**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/digital-twin.git
   cd digital-twin
   ```

2. **Install Dependencies**:
   - Backend:
     ```bash
     cd server
     npm install
     ```
   - Frontend:
     ```bash
     cd client
     npm install
     ```
   - Omniverse:
     ```bash
     cd omniverse
     pip install -r requirements.txt
     ```

3. **Start the Servers**:
   - Backend:
     ```bash
     npm start
     ```
   - Frontend:
     ```bash
     npm start
     ```
   - Omniverse:
     ```bash
     python src/app.py
     ```

### **Environment Variables**
Create `.env` files in `server/` and `omniverse/` for API keys, database credentials, and local configurations.

---

## 🌟 **Features**

### **Core Functionalities**
1. **Real-Time Data Dashboard**:
   - Live updates from integrated sensors and devices.
   - Visualization of key metrics and alerts.

2. **USD Model Integration**:
   - Seamless connection between Omniverse and the dashboard.
   - 3D visual representation of real-world systems.

3. **Alert and Analytics System**:
   - Customizable alerts for maintenance, energy consumption, and downtime.
   - Long-term trend analysis for optimization.

4. **Feedback Loop**:
   - Data-driven improvements fed back into operational processes.

---

## 🧠 **Next Steps**
- Complete Omniverse USD testing.
- Finalize real-time data integration.
- Connect USD 3D models to dashboard for live updates.
- Expand features for sustainable building management.

**Stay tuned!** Updates will be shared here soon.
