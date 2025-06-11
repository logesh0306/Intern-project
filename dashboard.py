import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crypto Sentiment Signals", layout="wide")

st.title("📈 Crypto News Sentiment Dashboard")

try:
    df = pd.read_excel("crypto_signals.xlsx")
    st.dataframe(df)

    st.subheader("📊 Signal Summary")
    buy_count = (df["Signal"] == "Buy").sum()
    sell_count = (df["Signal"] == "Sell").sum()
    hold_count = (df["Signal"] == "Hold").sum()

    st.metric("🟢 Buy", buy_count)
    st.metric("🔴 Sell", sell_count)
    st.metric("🟡 Hold", hold_count)
except:
    st.error("❌ No data found. Please run the main script first to generate crypto_signals.xlsx.")
