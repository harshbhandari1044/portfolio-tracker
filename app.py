import streamlit as st
import yfinance as yf

st.title("📊 Portfolio Tracker")

ticker = st.text_input("Enter Stock (e.g., RELIANCE.NS)")
buy_price = st.number_input("Buy Price")
quantity = st.number_input("Quantity")

if st.button("Analyze"):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")

    if not data.empty:
        current_price = data["Close"].iloc[-1]
        investment = buy_price * quantity
        current_value = current_price * quantity
        pnl = current_value - investment

        st.success(f"Current Price: ₹{current_price:.2f}")
        st.write(f"Investment: ₹{investment:.2f}")
        st.write(f"Current Value: ₹{current_value:.2f}")
        st.write(f"P&L: ₹{pnl:.2f}")

        if pnl > 0:
            st.success("Profit ✅")
        else:
            st.error("Loss ❌")
    else:
        st.error("Invalid ticker")
