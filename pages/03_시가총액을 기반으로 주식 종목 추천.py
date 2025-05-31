import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

st.set_page_config(page_title="맞춤형 종목 추천", layout="wide")
st.title("📈 예산 + 관심 분야 기반 종목 추천")

# 예제 종목 pool
top_stocks = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Nvidia': 'NVDA',
    'Meta': 'META',
    'Tesla': 'TSLA',
    'J&J': 'JNJ',
    'Visa': 'V',
    'Walmart': 'WMT',
    'Pfizer': 'PFE'
}

# 사용자 입력
budget = st.number_input("💰 투자 가능한 예산 (USD)", min_value=100.0, step=100.0)
sector_options = ['All', 'Technology', 'Healthcare', 'Consumer Defensive', 'Financial Services']
selected_sector = st.selectbox("📌 관심 업종 선택", sector_options)

start_date = date.today() - timedelta(days=365)
end_date = date.today()

@st.cache_data
def get_stock_data(tickers):
    rows = []
    for name, ticker in tickers.items():
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(start=start_date, end=end_date)
            if hist.empty:
                continue

            start_price = hist["Close"].iloc[0]
            end_price = hist["Close"].iloc[-1]
            growth = (end_price - start_price) / start_price * 100

            info = stock.info
            mkt_cap = info.get("marketCap", 0)
            sector = info.get("sector", "Unknown")
            price = info.get("currentPrice", None)
            pe = info.get("trailingPE", None)

            rows.append({
                "Company": name,
                "Ticker": ticker,
                "Sector": sector,
                "Price": price,
                "Market Cap (B)": round(mkt_cap / 1e9, 2),
                "1Y Growth (%)": round(growth, 2),
                "P/E": pe
            })
        except Exception as e:
            print(f"{ticker} error: {e}")
    return pd.DataFrame(rows)

with st.spinner("📊 데이터 로딩 중..."):
    df = get_stock_data(top_stocks)

# 조건 필터링
if selected_sector != "All":
    df = df[df["Sector"] == selected_sector]
df = df[df["Price"] <= budget]
df = df.sort_values(by="1Y Growth (%)", ascending=False)

st.subheader("✅ 추천 종목")
st.dataframe(df, use_container_width=True)

# 종목 선택 후 시각화
st.subheader("📉 시가총액 추이 보기")
if not df.empty:
    selected_company = st.selectbox("종목 선택", df["Company"].tolist())
    if selected_company:
        ticker = top_stocks[selected_company]
        stock = yf.Ticker(ticker)
        hist = stock.history(start=start_date, end=end_date)
        shares = stock.info.get("sharesOutstanding", 1)
        hist["Market Cap"] = hist["Close"] * shares
        hist = hist.reset_index()

        fig = px.line(hist, x="Date", y="Market Cap", title=f"{selected_company} - 시가총액 추이")
        st.plotly_chart(fig, use_container_width=True)
