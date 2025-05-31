import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

# 타이틀
st.set_page_config(page_title="시가총액 기반 종목 추천", layout="wide")
st.title("📈 시가총액 기반 종목 추천 시스템")

# 예시 기업 (대형주 중심)
top_stocks = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Nvidia': 'NVDA',
    'Meta': 'META',
    'Tesla': 'TSLA',
    'Alphabet': 'GOOGL',
    'TSMC': 'TSM',
    'Berkshire Hathaway': 'BRK-B',
    'Johnson & Johnson': 'JNJ'
}

start_date = date.today() - timedelta(days=365)
end_date = date.today()

# 데이터 가져오기
@st.cache_data
def get_market_cap_data(tickers, start, end):
    rows = []
    for name, ticker in tickers.items():
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(start=start, end=end)
            if df.empty:
                continue
            shares_outstanding = stock.info.get("sharesOutstanding", None)
            if not shares_outstanding:
                continue
            df["Market Cap"] = df["Close"] * shares_outstanding
            df["Company"] = name
            start_cap = df["Market Cap"].iloc[0]
            end_cap = df["Market Cap"].iloc[-1]
            growth = (end_cap - start_cap) / start_cap * 100
            rows.append({
                "Company": name,
                "Ticker": ticker,
                "Start Market Cap": start_cap,
                "End Market Cap": end_cap,
                "1Y Growth (%)": round(growth, 2)
            })
        except Exception as e:
            print(f"Error with {ticker}: {e}")
    return pd.DataFrame(rows)

with st.spinner("📊 데이터 불러오는 중..."):
    growth_df = get_market_cap_data(top_stocks, start_date, end_date)

# 성장률 필터
min_growth = st.slider("🔎 최소 시가총액 성장률 (%)", -100.0, 200.0, 10.0)
filtered = growth_df[growth_df["1Y Growth (%)"] >= min_growth]

# 추천 종목 테이블 출력
st.subheader("✅ 추천 종목 리스트")
st.dataframe(filtered, use_container_width=True)

# 종목 선택 후 시가총액 그래프
st.subheader("📉 시가총액 변화 추이")
selected_company = st.selectbox("종목 선택", filtered["Company"].tolist())
if selected_company:
    ticker = top_stocks[selected_company]
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    shares_outstanding = stock.info.get("sharesOutstanding", 1)
    df["Market Cap"] = df["Close"] * shares_outstanding
    df = df.reset_index()

    fig = px.line(df, x="Date", y="Market Cap", title=f"{selected_company} - 최근 1년 시가총액 추이",
                  labels={"Market Cap": "시가총액 (USD)"})
    st.plotly_chart(fig, use_container_width=True)
