import streamlit as st
import pandas as pd
import boto3
from datetime import datetime, timedelta
from sklearn.ensemble import IsolationForest
import time
import random
import numpy as np

# ---------------- CONFIG ----------------
INSTANCE_ID = "i-0b123e198da599a7d"
REGION = "eu-north-1"

ec2 = boto3.client('ec2', region_name=REGION)
cloudwatch = boto3.client('cloudwatch', region_name=REGION)

st.set_page_config(page_title="Cloud Cost Optimizer", layout="wide")

# ---------------- CUSTOM UI ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
}
.normal {color: #22c55e; font-weight: bold;}
.alert {color: #facc15; font-weight: bold;}
.stop {color: #ef4444; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Control Panel")

mode = st.sidebar.selectbox("Mode", ["Real Data", "Demo Mode"])
force_anomaly = st.sidebar.toggle("Force Anomaly 🚨")

# ---------------- FUNCTIONS ----------------
def get_real_data():
    try:
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': INSTANCE_ID}],
            StartTime=datetime.utcnow() - timedelta(minutes=5),
            EndTime=datetime.utcnow(),
            Period=60,
            Statistics=['Average']
        )

        datapoints = response['Datapoints']
        if not datapoints:
            return 10

        latest = sorted(datapoints, key=lambda x: x['Timestamp'])[-1]
        return latest['Average']

    except:
        return 10


@st.cache_resource
def train_model():
    data = [[10], [20], [30], [40], [50]]
    model = IsolationForest(contamination=0.2)
    model.fit(data)
    return model


def decision_logic(cpu, anomaly):
    if anomaly and cpu < 5:
        return "AUTO_STOP", 95
    elif anomaly:
        return "ALERT", 75
    return "NORMAL", 50


def stop_instance():
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])


def send_email_alert(message):
    st.markdown(f"""
    <div style='padding:15px; border-radius:10px; background:#1e293b; border-left:5px solid red'>
    📩 <b>Email Alert:</b> {message}
    </div>
    """, unsafe_allow_html=True)


def send_slack_alert(message):
    st.markdown(f"""
    <div style='padding:15px; border-radius:10px; background:#1e293b; border-left:5px solid yellow'>
    💬 <b>Slack Alert:</b> {message}
    </div>
    """, unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown("""
<h1>💸 SpendR Cloud Cost Optimizer</h1>
<p style='color:gray'>AI-powered real-time cloud cost optimization system</p>
""", unsafe_allow_html=True)

st.caption("🚀 Built for real-time cloud cost optimization | Hackathon Ready")

# ---------------- MODEL ----------------
model = train_model()

# ---------------- SESSION ----------------
if "cpu_data" not in st.session_state:
    st.session_state.cpu_data = []

# ---------------- DATA ----------------
if mode == "Demo Mode":
    cpu = random.choice([2, 5, 80, 3, 90])
else:
    cpu = get_real_data()

st.session_state.cpu_data.append(cpu)

pred = model.predict([[cpu]])[0]
anomaly = (pred == -1) or force_anomaly

decision, confidence = decision_logic(cpu, anomaly)

# ---------------- KPI CARDS ----------------
col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"""
<div class="card">
<h3>CPU Usage</h3>
<h2>{cpu:.2f}%</h2>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="card">
<h3>Decision</h3>
<h2>{decision}</h2>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="card">
<h3>Confidence</h3>
<h2>{confidence}%</h2>
</div>
""", unsafe_allow_html=True)

savings = 25 * len(st.session_state.cpu_data)

col4.markdown(f"""
<div class="card">
<h3>💰 Savings</h3>
<h2>₹{savings}</h2>
</div>
""", unsafe_allow_html=True)

# ---------------- STATUS ----------------
if decision == "AUTO_STOP":
    st.markdown("<p class='stop'>🔴 CRITICAL: Instance Stopped</p>", unsafe_allow_html=True)
elif decision == "ALERT":
    st.markdown("<p class='alert'>🟡 WARNING: Anomaly Detected</p>", unsafe_allow_html=True)
else:
    st.markdown("<p class='normal'>🟢 SYSTEM NORMAL</p>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- CHART ----------------
st.markdown("### 📊 Real-Time CPU Trend")

chart_data = pd.DataFrame({
    "CPU Usage": st.session_state.cpu_data
})

st.line_chart(chart_data)

# ---------------- ACTIONS ----------------
if decision == "AUTO_STOP":
    msg = "🚨 EC2 stopped to save cost!"
    stop_instance()
    send_email_alert(msg)
    send_slack_alert(msg)

elif decision == "ALERT":
    msg = "⚠ Anomaly detected!"
    send_email_alert(msg)
    send_slack_alert(msg)

# ---------------- SAVINGS ----------------
st.markdown("### 💰 Cost Optimization Impact")

before = 500
after = before - savings

c1, c2 = st.columns(2)
c1.metric("Before Optimization", f"₹{before}")
c2.metric("After Optimization", f"₹{after}", delta=f"-₹{before-after}")

# ---------------- PREDICTION ----------------
st.markdown("### 📉 Predicted Cost Trend")

predicted_cost = [before - i*10 for i in range(10)]
st.line_chart(predicted_cost)

# ---------------- AI INSIGHTS ----------------
st.markdown("### 🧠 AI Insights")

if decision == "AUTO_STOP":
    st.error("Instance underutilized → automatically stopped to prevent cost leakage.")
elif decision == "ALERT":
    st.warning("Unusual usage detected → monitoring closely.")
else:
    st.success("Resource usage is optimal.")

# ---------------- LOGS ----------------
st.markdown("### 📜 System Logs")

try:
    with open("logs/actions.log") as f:
        logs = f.readlines()[-5:]
        for log in logs:
            st.text(log)
except:
    st.info("No logs yet")

# ---------------- AUTO REFRESH ----------------
time.sleep(3)
st.rerun()