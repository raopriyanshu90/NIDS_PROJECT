import streamlit as st
import pandas as pd
import joblib
import time
import plotly.express as px

# Load model + features
data = joblib.load("model.pkl")
model = data["model"]
features = data["features"]

# Page config
st.set_page_config(page_title="NIDS - Cyber Dashboard", layout="wide")

# 🔥 CUSTOM HACKER STYLE CSS
st.markdown("""
<style>
body {
    background-color: #0b0f19;
    color: #00ffcc;
}
h1 {
    color: #ff0033;
    text-align: center;
}
.stMetric {
    background-color: #111;
    padding: 10px;
    border-radius: 10px;
}
div[data-testid="stAlert"] {
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🚨 CYBER INTRUSION DETECTION SYSTEM 🚨</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙️ Control Panel")
threshold = st.sidebar.slider("Detection Sensitivity", 0.1, 0.9, 0.3)

uploaded_file = st.file_uploader("📂 Upload Network Traffic CSV")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Live Data Preview")
    st.dataframe(df.head())

    # Select features
    df = df[features]

    attack_count = 0
    normal_count = 0

    log = []

    chart_placeholder = st.empty()
    metrics_placeholder = st.empty()
    log_placeholder = st.empty()

    attack_history = []
    normal_history = []

    for i in range(min(len(df), 300)):

        row = df.iloc[i:i+1]

        prob = model.predict_proba(row)[:, 1][0]
        pred = 1 if prob > threshold else 0

        if pred == 1:
            attack_count += 1
            log.append(f"[🚨 ATTACK] Row {i} | Threat Score: {prob:.2f}")
        else:
            normal_count += 1
            log.append(f"[✅ NORMAL] Row {i}")

        attack_history.append(attack_count)
        normal_history.append(normal_count)

        # 🔥 METRICS
        with metrics_placeholder.container():
            col1, col2 = st.columns(2)
            col1.metric("🚨 ATTACKS", attack_count)
            col2.metric("✅ NORMAL", normal_count)

        # 🔥 GRAPH
        chart_df = pd.DataFrame({
            "Step": list(range(len(attack_history))),
            "Attacks": attack_history,
            "Normal": normal_history
        })

        fig = px.line(chart_df, x="Step", y=["Attacks", "Normal"],
                      title="📈 Live Traffic Monitoring")

        chart_placeholder.plotly_chart(fig, use_container_width=True)

        # 🔥 TERMINAL LOG
        with log_placeholder.container():
            st.subheader("💻 Live Activity Feed")
            for entry in log[-10:]:
                if "ATTACK" in entry:
                    st.markdown(f"<span style='color:red'>{entry}</span>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<span style='color:lime'>{entry}</span>", unsafe_allow_html=True)

        time.sleep(0.05)

else:
    st.warning("⚠️ Upload dataset to start monitoring")