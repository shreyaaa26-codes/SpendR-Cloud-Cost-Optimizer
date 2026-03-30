# SpendR-Cloud-Cost-Optimizer
Tech Solstice 2026 - Marco Polo

An AI-powered cloud cost optimization system that monitors AWS resources in real-time, detects anomalies using Machine Learning, and automatically takes cost-saving actions.

🚀 Features

- 📊 Real-time CloudWatch monitoring
- 🤖 ML anomaly detection (Isolation Forest)
- ⚡ Automatic EC2 instance optimization
- 🚨 Smart alerts (Slack + Email simulation)
- 💰 Cost savings visualization
- 📉 Cost prediction dashboard
- 🧠 AI insights panel

🛠 Tech Stack

- AWS EC2 + CloudWatch
- Python (Boto3, Scikit-learn)
- Streamlit (Frontend Dashboard)

📸 Demo

Live dashboard showing:
- CPU usage trends
- ML-based decisions
- Automated actions
- Real-time alerts

⚙️ Setup

```bash
pip install streamlit boto3 pandas scikit-learn numpy
python3 -m streamlit run app.py --server.address 0.0.0.0
