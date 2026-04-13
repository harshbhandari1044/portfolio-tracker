import streamlit as st
import yfinance as yf

# Page config
st.set_page_config(page_title="Portfolio Tracker", layout="centered")

# -------------------------------
# FUNCTIONS (Analysis Engine)
# -------------------------------

def get_scores(current_price, buy_price):
    # Technical (price momentum)
    technical = 70 if current_price > buy_price else 50

    # Fundamental (placeholder)
    fundamental = 75

    # Sentiment (placeholder)
    sentiment = 65

    # Risk (inverse logic)
    risk = 60

    # Thesis
    thesis = 70

    return technical, fundamental, sentiment, risk, thesis


def calculate_trade_score(t, f, s, r, th):
    score = (
        t * 0.25 +
        f * 0.25 +
        s * 0.20 +
        r * 0.15 +
        th * 0.15
    )
    return round(score)


# -------------------------------
# UI
# -------------------------------

st.title("📊 Portfolio Tracker")

ticker = st.text_input("Enter Stock (e.g., RELIANCE.NS)")
buy_price = st.number_input("Buy Price")
quantity = st.number_input("Quantity")

# -------------------------------
# BASIC ANALYSIS (P&L)
# -------------------------------

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

        # Chart
        st.line_chart(data["Close"])

    else:
        st.error("Invalid ticker")


# -------------------------------
# FULL ANALYSIS (Advanced)
# -------------------------------

if st.button("Full Analysis"):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")

    if not data.empty:
        current_price = data["Close"].iloc[-1]

        t, f, s, r, th = get_scores(current_price, buy_price)
        score = calculate_trade_score(t, f, s, r, th)

        st.subheader("📊 Trade Score")
        st.write(f"Score: {score}/100")

        if score >= 70:
            st.success("BUY 🟢")
        elif score >= 55:
            st.warning("HOLD 🟡")
        else:
            st.error("AVOID 🔴")

        st.subheader("📊 Score Breakdown")
        st.write(f"Technical: {t}")
        st.write(f"Fundamental: {f}")
        st.write(f"Sentiment: {s}")
        st.write(f"Risk: {r}")
        st.write(f"Thesis: {th}")

        # Chart
        st.line_chart(data["Close"])

        # Basic AI Insight
        st.subheader("🧠 Insight")
        if current_price > buy_price:
            st.write("Stock is showing positive momentum. Trend is favorable.")
        else:
            st.write("Stock is underperforming your entry. Review position.")

    else:
        st.error("Invalid ticker")
