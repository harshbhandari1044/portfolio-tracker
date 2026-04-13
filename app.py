import streamlit as st
import yfinance as yf

st.title("📊 Portfolio Tracker")

ticker = st.text_input("Enter Stock (e.g., RELIANCE.NS)")

if st.button("Get Price"):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")

    if not data.empty:
        price = data["Close"].iloc[-1]
        st.success(f"Current Price: ₹{price:.2f}")
    else:
        st.error("Invalid ticker")
