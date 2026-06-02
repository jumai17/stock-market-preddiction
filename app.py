import streamlit as st
from analysis.scoring import generate_signal

st.set_page_config(page_title="Stock AI Predictor")
st.title("AI Stock Trading Signal System")

files = {}
for tf in ["5m","15m","1h","Daily"]:
    files[tf] = st.file_uploader(f"Upload {tf} chart", type=["png","jpg","jpeg"])

if st.button("Analyze"):
    result = generate_signal()
    st.json(result)
