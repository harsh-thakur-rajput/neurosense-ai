# 🏥 NeuroSense AI: Adaptive Medical & Smart Ward Cloud Monitoring System

**NeuroSense AI** is an advanced, closed-loop cyber-physical system designed for multi-ward clinical environments. It features an **Adaptive Intelligence Framework** that transitions between General Ward, ICU, and NICU protocols. The system combines **Edge AI (Reflex)** and **Cloud Deep Learning (Predictive)** to ensure precise environmental control and patient safety across various medical scenarios.

![Project Status](https://img.shields.io/badge/Status-Prototype%20v5.0-blue)
![Tech Stack](https://img.shields.io/badge/Stack-Python%20|%20Firebase%20|%20ESP32%20|%20JS-green)

## 🚀 Key Features

### 🧠 1. Dual-AI Architecture
- **Edge AI (Brain.js):** Runs locally on the dashboard to calculate a real-time **Stability Index** and detect micro-fluctuations in sensor data (Zero-Latency Reflex).
- **Cloud AI (TensorFlow LSTM):** A **Long Short-Term Memory (LSTM)** Neural Network that analyzes historical telemetry to forecast future Core Temperature (T-Core) and provide **Early Warning Alerts** (e.g., Hypothermia/Overheating trajectories).

### 🎛️ 2. Intelligent Hardware Control (Fuzzy Logic)
- Replaced traditional PID controllers with a custom **4-Way Fuzzy Inference System (FIS)**.
- Actively controls the **Thermal Emitter, Ventilation Fan, Ultrasonic Atomizer, and Desiccant Extractor** using human-like linguistic states (e.g., *Critical Cold, Warm, Optimal, Moist, Rain-out risk*).
- **Multi-Protocol Support:** Ensures smooth, jerk-free hardware actuation to strictly maintain clinical environments for **Standard Care, ICU, and Neonatal (NICU)** protocols.

---

## 🛠️ Tech Stack
- **Hardware Endpoints:** ESP32 (Dual Core MCU), DHT11 Environmental Sensor
- **Frontend / Edge Node:** HTML5, Tailwind CSS, Chart.js, Brain.js
- **Cloud Backend:** Python, TensorFlow (Keras), Scikit-Learn, Pandas, Numpy
- **Database & Middleware:** Google Firebase Realtime Database & Admin SDK

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/your-username/neurosense-ai.git](https://github.com/your-username/neurosense-ai.git)
   cd neurosense-ai

2. **Install Python Dependencies**
   Ensure Python 3.x is installed, then run:
   ```bash
   pip install tensorflow scikit-learn pandas numpy firebase-admin

4. **Configure Environment Secrets**

   Place your firebase-keys.json (Admin SDK key) in the root directory.

   Update the firebaseConfig in index.html with your project's Web API keys.

5. **Initialize Cloud AI Engine**
     ```bash
     python ml_backend.py

7. **Launch Dashboard**
   Open index.html in any modern web browser.

Lead Developer: Harsh Thakur

License: MIT
