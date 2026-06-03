# 💸 SpendR — AI-Powered Cloud Cost Optimization Platform

<div align="center">

### 🚀 Intelligent Cloud Resource Monitoring • 🤖 Machine Learning-Based Anomaly Detection • ☁️ AWS EC2 Automation

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Isolation%20Forest-green?style=for-the-badge)
![AWS](https://img.shields.io/badge/AWS-EC2-orange?style=for-the-badge&logo=amazonaws)
![Flask](https://img.shields.io/badge/Flask-REST%20API-black?style=for-the-badge&logo=flask)
![Cloud Computing](https://img.shields.io/badge/Cloud-Optimization-blueviolet?style=for-the-badge)
![Boto3](https://img.shields.io/badge/Boto3-AWS%20SDK-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Hackathon Project](https://img.shields.io/badge/Project-Hackathon-red?style=for-the-badge)

</div>

---

# 📖 Overview

SpendR is an AI-powered cloud cost optimization platform designed to automatically identify underutilized cloud resources and perform intelligent cost-saving actions in real time.

The system continuously monitors cloud usage metrics such as:

- CPU Utilization
- Request Traffic
- Storage Consumption

Using Machine Learning, SpendR detects anomalous resource behavior and automatically triggers optimization actions such as stopping idle AWS EC2 instances, helping organizations reduce unnecessary cloud expenditure.

Unlike traditional monitoring systems that only provide alerts, SpendR takes proactive decisions using AI-driven analysis and AWS automation.

---

# 🎯 Problem Statement

Cloud platforms provide tremendous scalability, but organizations often face significant challenges in controlling operational costs.

Common issues include:

❌ Idle EC2 instances running continuously

❌ Unused cloud resources consuming budget

❌ Manual monitoring of infrastructure

❌ Delayed response to abnormal resource usage

❌ Lack of intelligent cost optimization mechanisms

As cloud infrastructure grows, manually identifying waste becomes increasingly difficult.

SpendR addresses these challenges by combining Machine Learning and Cloud Automation to create a self-optimizing infrastructure management system.

---

# 💡 Proposed Solution

SpendR introduces an intelligent cloud optimization pipeline capable of:

### 1. Continuous Resource Monitoring
Tracks cloud usage patterns in real time.

### 2. AI-Based Anomaly Detection
Uses Isolation Forest to identify abnormal resource behavior.

### 3. Intelligent Decision Making
Evaluates anomalies using confidence scoring and rule-based logic.

### 4. AWS Infrastructure Automation
Automatically performs cost-saving actions on EC2 instances.

### 5. Dashboard Visualization
Provides a user-friendly interface for monitoring system decisions.

### 6. Action Logging
Maintains detailed logs for transparency and auditing.

---

# 🏗️ High-Level Architecture

```text
                  ┌─────────────────────┐
                  │  Cloud Usage Data   │
                  │ CPU • Requests •    │
                  │ Storage Metrics     │
                  └──────────┬──────────┘
                             │
                             ▼

                ┌─────────────────────────┐
                │ Data Processing Layer   │
                │ Pandas Data Pipeline    │
                └──────────┬──────────────┘
                           │
                           ▼

                ┌─────────────────────────┐
                │ Isolation Forest Model  │
                │ Anomaly Detection       │
                └──────────┬──────────────┘
                           │
                           ▼

                ┌─────────────────────────┐
                │ Decision Engine         │
                │ Confidence Scoring      │
                └──────────┬──────────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼

      NORMAL           ALERT          AUTO_STOP

                                            │
                                            ▼

                              ┌────────────────────┐
                              │ AWS EC2 Automation │
                              │ Boto3 Integration  │
                              └─────────┬──────────┘
                                        │
                                        ▼

                              ┌────────────────────┐
                              │ Flask REST API     │
                              └─────────┬──────────┘
                                        │
                                        ▼

                              ┌────────────────────┐
                              │ Frontend Dashboard │
                              └────────────────────┘
```

---

# 🌟 Key Features

### 1. Machine Learning-Based Anomaly Detection

Utilizes the Isolation Forest algorithm to identify unusual cloud resource usage patterns.

---

### 2. AWS EC2 Automation

Direct integration with AWS using Boto3 enables automated instance management.

---

### 3. Real-Time Monitoring

Continuously analyzes incoming cloud metrics and updates decisions dynamically.

---

### 4. Confidence-Based Decision Engine

Generates confidence scores before performing automated actions.

---

### 5. Audit Logging

Stores all optimization actions with timestamps for accountability and debugging.

---

### 6. REST API Support

Flask API exposes real-time optimization data to frontend applications.

---

### 7. Cost Reduction

Automatically detects and eliminates unnecessary cloud spending.

---

# 🛠️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| Programming Language | Python |
| Machine Learning | Scikit-Learn |
| Algorithm | Isolation Forest |
| Cloud Platform | AWS EC2 |
| Cloud SDK | Boto3 |
| Backend Framework | Flask |
| API Development | Flask REST API |
| Data Processing | Pandas |
| Frontend | HTML, CSS, JavaScript |
| Version Control | Git |
| Repository Hosting | GitHub |

---

# 🔨 Project Development Workflow

## Phase 1: Cloud Infrastructure Setup

The project began with provisioning an AWS EC2 instance that served as the deployment and testing environment.

### Steps Performed

### 1. Launch EC2 Instance

- Created an AWS EC2 Instance
- Selected Amazon Linux AMI
- Configured Security Groups
- Enabled SSH Access

### 2. Connect to EC2

Using SSH:

```bash
ssh -i "hackathon-key.pem" ec2-user@PUBLIC_IP
```

This established a secure remote connection to the cloud server.

---

### 3. Install Required Dependencies

```bash
sudo yum update -y

pip3 install pandas
pip3 install scikit-learn
pip3 install boto3
pip3 install flask
pip3 install flask-cors
```

---

## Phase 2: Data Processing Layer

The next step involved creating a lightweight data ingestion pipeline.

### Dataset Structure

```text
CPU Usage
Request Count
Storage Usage
```

Sample:

```csv
cpu,requests,storage
10,100,50
20,200,60
15,150,55
```

### Data Handling

Using Pandas:

```python
df = pd.read_csv("data/live_usage.csv")
```

The system continuously reads usage data and prepares it for machine learning analysis.

---

## Phase 3: Machine Learning Implementation

### Objective

Identify abnormal cloud resource utilization patterns.

### Model Selection

Isolation Forest was selected because:

- Efficient for anomaly detection
- Works with unlabeled data
- Lightweight and fast
- Suitable for real-time systems

### Training Process

```python
model = IsolationForest(
    contamination=0.2
)

model.fit(df)
```

The model learns normal behavior patterns from historical usage data.

---

### Prediction Process

```python
prediction = model.predict([data])[0]
```

Output:

```text
1   = Normal
-1  = Anomaly
```

---

## Phase 4: Decision Engine

Machine Learning predictions are passed into a custom decision engine.

### Logic

```python
if anomaly and cpu < 5:
    return "AUTO_STOP", 95

elif anomaly:
    return "ALERT", 75

else:
    return "NORMAL", 50
```

### Why?

The ML model identifies anomalies, but business logic decides the final action.

---

### Example

| CPU Usage | Anomaly | Action |
|------------|----------|----------|
| 1% | Yes | AUTO_STOP |
| 20% | Yes | ALERT |
| 40% | No | NORMAL |

---

## Phase 5: AWS Automation Layer

After generating a decision, the system automatically interacts with AWS infrastructure.

### AWS SDK Integration

```python
import boto3
```

### EC2 Client Creation

```python
ec2 = boto3.client(
    'ec2',
    region_name='eu-north-1'
)
```

### Automated Cost Optimization

```python
ec2.stop_instances(
    InstanceIds=[INSTANCE_ID]
)
```

When low utilization is detected, the EC2 instance is automatically stopped.

---

## Phase 6: Logging & Audit Trail

Every system action is recorded.

### Example

```python
log_action(
    "Instance stopped to save cost"
)
```

Stored in:

```text
logs/actions.log
```

Example Log:

```text
2025-03-28 12:45:21
Instance stopped to save cost
```

---

# 🌐 Backend API Development

After completing the AI engine, we developed a REST API layer to expose predictions to external applications.

### Framework

Flask

### API Endpoint

```python
@app.route("/data")
```

### Response

```json
{
    "cpu": 1,
    "decision": "AUTO_STOP",
    "confidence": 95
}
```

This allows frontend applications to fetch live optimization data.

---

# 🎨 Frontend Development

After the backend was operational, a monitoring dashboard was developed.

### Technologies Used

- HTML
- CSS
- JavaScript

### Dashboard Features

✅ CPU Usage Monitoring

✅ ML Prediction Display

✅ Confidence Score Visualization

✅ Optimization Action Status

---

### Frontend Workflow

```text
User Opens Dashboard
          │
          ▼

Frontend Sends Request
          │
          ▼

GET /data
          │
          ▼

Flask API Returns JSON
          │
          ▼

Dashboard Updates UI
```

---

# 🔄 End-to-End System Flow

```text
AWS Cloud Resources
          │
          ▼

Resource Usage Data
          │
          ▼

Data Processing Layer
          │
          ▼

Isolation Forest Model
          │
          ▼

Decision Engine
          │
          ▼

AWS EC2 Automation
          │
          ▼

Logging System
          │
          ▼

Flask API
          │
          ▼

Frontend Dashboard
          │
          ▼

User Monitoring Interface
```

---

# 👨‍💻 Our Contributions

### Cloud Deployment - Rida Azam

- Provisioned AWS EC2 infrastructure
- Configured Security Groups
- Managed SSH access
- Deployed and tested the backend on cloud infrastructure
  
### Backend Development - Avani Verma and Niharika G

- Built the data ingestion pipeline
- Developed the Isolation Forest anomaly detection model
- Implemented the decision engine
- Integrated AWS EC2 automation using Boto3
- Developed logging functionality
- Built Flask REST APIs

### Frontend Development - Shreya L

- Designed dashboard UI
- Connected frontend with Flask API
- Displayed live cloud optimization metrics
- Visualized ML decisions and confidence scores

---

# 🏆 Key Achievements

✅ Automated Cloud Cost Optimization

✅ Real-Time Anomaly Detection

✅ AWS EC2 Infrastructure Automation

✅ Machine Learning Integration

✅ REST API Development

✅ Dashboard Visualization

✅ End-to-End Cloud Deployment

✅ Full Stack AI Solution

---

# 🚀 Future Enhancements

We plan to extend SpendR with:

-  Email and SMS Alerting System
-  Multi-Cloud Support (AWS, Azure, GCP)
-  Cloud Cost Forecasting using Predictive Analytics
-  Reinforcement Learning-Based Optimization
-  Grafana & Prometheus Monitoring Integration
-  DynamoDB/PostgreSQL Integration
-  Docker & Kubernetes Deployment
-  Slack and Microsoft Teams Notifications

---

# 🏆 Hackathon Showcase

This project was successfully developed and presented during **Tech Solstice Hackathon 2026** at **Manipal Institute of Technology, Bengaluru**.

SpendR represents our vision of combining **Artificial Intelligence, Cloud Computing, and Automation** to solve real-world cloud cost management challenges. Through this project, we explored end-to-end system design, machine learning-driven decision making, AWS cloud integration, backend API development, and frontend visualization.

The project demonstrates how intelligent systems can proactively optimize cloud resources, reduce operational costs, and improve infrastructure efficiency without constant human intervention.

---

