# 🚗 Vehicle Security Monitor

A Python-based cybersecurity monitoring system for detecting, analyzing, scoring, and logging vehicle security events.

The Vehicle Security Monitor (VSM) provides a simulated security-monitoring environment that combines event modeling, threat detection, risk scoring, persistent SQLite logging, a FastAPI backend, and a Streamlit dashboard.

---

## 🎯 Project Overview

Modern vehicles contain interconnected electronic systems that can be exposed to security threats such as unauthorized access, tampering, suspicious unlock attempts, and abnormal electrical activity.

The Vehicle Security Monitor demonstrates how a cybersecurity monitoring system can process security events and provide actionable risk information.

The system currently supports:

* Security event modeling with Pydantic
* Threat detection based on event type and severity
* Numerical security risk scoring
* Risk-level classification
* Persistent event logging using SQLite
* REST API endpoints using FastAPI
* Interactive monitoring using Streamlit
* Automated testing with pytest
* Isolated database testing

---

## 🛡️ Security Features

### Security Event Detection

The system recognizes the following event types:

| Event Type         | Description                       |
| ------------------ | --------------------------------- |
| `DOOR_OPEN`        | Vehicle door opening event        |
| `IGNITION_ATTEMPT` | Vehicle ignition attempt          |
| `UNLOCK_ATTEMPT`   | Vehicle unlock attempt            |
| `MOTION_DETECTED`  | Vehicle movement detected         |
| `TAMPER_DETECTED`  | Possible vehicle tampering        |
| `BATTERY_ANOMALY`  | Abnormal vehicle battery activity |

The detection engine evaluates the event type and severity to determine whether an event should be treated as a potential threat.

### Risk Scoring

Each security event receives a numerical risk score based on its severity and event type.

Base severity scores:

| Severity   | Points |
| ---------- | -----: |
| `LOW`      |      1 |
| `MEDIUM`   |      3 |
| `HIGH`     |      6 |
| `CRITICAL` |     10 |

Additional points are applied to certain security-sensitive events:

* `TAMPER_DETECTED` → +5
* `UNLOCK_ATTEMPT` → +2
* `BATTERY_ANOMALY` → +2

The resulting score is classified as:

| Score | Risk Level |
| ----: | ---------- |
|   0–4 | LOW        |
|   5–9 | MEDIUM     |
| 10–14 | HIGH       |
|   15+ | CRITICAL   |

---

## 🏗️ System Architecture

```text
                  ┌──────────────────────┐
                  │   Security Event     │
                  │      Input           │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │  Security Detection  │
                  │       Engine         │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │     Risk Engine      │
                  │                      │
                  │ Score → Risk Level   │
                  └──────────┬───────────┘
                             │
                ┌────────────┴────────────┐
                ▼                         ▼
       ┌─────────────────┐       ┌─────────────────┐
       │  SQLite Logger  │       │    FastAPI      │
       │                 │       │      API        │
       └────────┬────────┘       └────────┬────────┘
                │                         │
                └────────────┬────────────┘
                             ▼
                  ┌──────────────────────┐
                  │ Streamlit Dashboard  │
                  │                      │
                  │ Security Monitoring  │
                  └──────────────────────┘
```

---

## 🔍 Threat Model

The current system is designed as a security-monitoring prototype.

### Potential Threats

The monitor is designed to identify events representing scenarios such as:

* Unauthorized vehicle tampering
* Suspicious unlock attempts
* Abnormal battery activity
* Unauthorized ignition attempts
* Unexpected vehicle movement
* Security-related sensor events

### Security Monitoring Approach

The system follows this general flow:

```text
Event
  ↓
Validate Event
  ↓
Analyze Threat
  ↓
Calculate Risk Score
  ↓
Classify Risk
  ↓
Log Event
  ↓
Expose Security Information
```

### Important Scope

This project is currently a **software-based vehicle security monitoring prototype**.

It does not directly interface with a real vehicle CAN bus, ECU, immobilizer, physical alarm system, or vehicle sensors.

The event data is supplied to the application through the API and represents simulated vehicle-security telemetry.

---

## ⚙️ Technology Stack

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| Python     | Core application language          |
| FastAPI    | REST API                           |
| Pydantic   | Event validation and data modeling |
| SQLite     | Persistent event storage           |
| Streamlit  | Security monitoring dashboard      |
| pytest     | Automated testing                  |
| Uvicorn    | ASGI application server            |
| Git        | Version control                    |
| GitHub     | Source-code hosting                |

---

## 📁 Project Structure

```text
Vehicle-Security-Monitor/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── event.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── event_logger.py
│       ├── risk_engine.py
│       └── security_engine.py
│
├── dashboard/
│   └── dashboard.py
│
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_event_logger.py
│   ├── test_risk_engine.py
│   └── test_security_engine.py
│
├── data/
│   └── .gitkeep
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

The SQLite database is generated locally under `data/` and is excluded from version control.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/ifeoluwaolukayode343-dev/Vehicle-Security-Monitor.git
cd Vehicle-Security-Monitor
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution for the current session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

---

## 🔌 Running the FastAPI Backend

Start the API with:

```powershell
uvicorn app.main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available through FastAPI's documentation interface.

### Health Check

Endpoint:

```text
GET /health
```

Example response:

```json
{
  "status": "online",
  "service": "Vehicle Security Monitor"
}
```

---

## 📡 Security Event API

### Create a Security Event

Endpoint:

```text
POST /events
```

Example request:

```json
{
  "event_id": "EVT-001",
  "vehicle_id": "VSM-001",
  "event_type": "TAMPER_DETECTED",
  "source": "vehicle_security_sensor",
  "severity": "CRITICAL",
  "description": "Unauthorized tampering detected on vehicle."
}
```

The system will:

1. Validate the event
2. Analyze the event for threats
3. Calculate its risk score
4. Determine the risk level
5. Store the event in SQLite
6. Return the security analysis

Example response:

```json
{
  "event_id": "EVT-001",
  "vehicle_id": "VSM-001",
  "event_type": "TAMPER_DETECTED",
  "is_threat": true,
  "risk_score": 15,
  "risk_level": "CRITICAL",
  "alert": "Vehicle tampering detected."
}
```

### Retrieve Security Events

Endpoint:

```text
GET /events
```

This returns previously stored security events from the SQLite database.

---

## 📊 Running the Dashboard

The Streamlit dashboard provides a visual security-monitoring interface.

Start it with:

```powershell
streamlit run dashboard/dashboard.py
```

The dashboard provides:

* System status
* Total security events
* Threat count
* Critical-event count
* High-risk count
* Medium/low event count
* Vehicle filtering
* Severity filtering
* Security event details
* Risk distribution chart
* Latest event information
* Event refresh functionality

---

## 🧪 Testing

The project includes automated tests covering the major components.

Run the complete test suite with:

```powershell
python -m pytest
```

Current test result:

```text
10 passed
```

Tests cover:

### API

* Health endpoint
* Security-event creation
* Event retrieval

### Security Engine

* Tamper detection
* Normal door events
* Suspicious unlock attempts

### Risk Engine

* Low-risk calculation
* Critical tampering score
* Risk-level classification

### Event Logger

* SQLite event persistence
* Event retrieval

The API tests use isolated temporary databases so that test execution does not modify the application's real local database.

---

## 🔐 Security Considerations

This project demonstrates defensive cybersecurity monitoring principles.

Important considerations for a production vehicle-security platform would include:

* Authentication and authorization
* TLS-protected communications
* Secure device identity
* Strong API access controls
* Input validation
* Rate limiting
* Secure logging
* Database access controls
* Tamper-resistant audit logs
* Secure key management
* CAN/automotive protocol security
* ECU security controls
* Intrusion detection
* Secure software updates
* Monitoring and incident response

These capabilities are outside the current prototype scope and represent potential future development areas.

---

## 🧭 Future Improvements

Potential future versions could introduce:

* Real-time event streaming
* Vehicle CAN-bus integration in a controlled test environment
* Automotive Intrusion Detection System (IDS) capabilities
* Authentication and role-based access control
* WebSocket-based live monitoring
* Email/SMS security alerts
* Event severity escalation
* IP/device tracking
* Advanced anomaly detection
* Machine-learning-assisted threat detection
* Docker deployment
* Cloud-based monitoring
* Security audit logging
* Alert acknowledgement and incident management
* Multi-vehicle fleet monitoring

---

## 🧑‍💻 Development Workflow

The project was developed incrementally using Git version control.

Major development stages include:

```text
Project Foundation
        ↓
Security Event Model
        ↓
Security Detection Engine
        ↓
Risk Engine
        ↓
SQLite Event Logger
        ↓
FastAPI API
        ↓
Streamlit Dashboard
        ↓
Automated Tests
        ↓
GitHub Repository
```

Each major component was tested before progressing to the next stage.

---

## 📌 Project Status

**Current Status: Functional Security Monitoring Prototype**

Implemented:

* ✅ Security event model
* ✅ Threat detection engine
* ✅ Risk scoring engine
* ✅ SQLite persistence
* ✅ REST API
* ✅ Security dashboard
* ✅ Automated tests
* ✅ Git version control
* ✅ GitHub repository

---

## ⚠️ Disclaimer

This project is intended for educational, research, and cybersecurity portfolio purposes.

It is a prototype security-monitoring application and should not be deployed directly in a production vehicle without appropriate automotive safety, security, reliability, validation, and regulatory engineering.

---

## 📄 License

No license has currently been specified for this repository.
