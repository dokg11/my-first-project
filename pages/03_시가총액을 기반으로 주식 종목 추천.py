import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

st.set_page_config(page_title="맞춤형 종목 추천 시스템", layout="wide")
st.title("📈 예산 + 관심 업종 + 가치 기반 종목 추천")

# 주요 대형주 예시 (필요시 100개까지 확장 가능)
stock_pool = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Nvidia': 'NVDA',
    'Meta': 'META',
    'Tesla': 'TSLA',
    'Johnson & Johnson': 'JNJ',
    'Pfizer': 'PFE',
    'Procter & Gamble': 'PG',
    'Visa': 'V',
    'Walmart': 'WMT',
    'Coca-Cola': 'KO',
    'Intel': 'INTC',
    'Chevron': 'CVX',
    'JPMorgan': 'JPM',
    'Adobe': 'ADBE',
    'Netflix': 'NFLX',
    'Salesforce': 'CRM',
    'PepsiCo': 'PEP',
    'Costco': 'COST',
}

start_date = date.today() - timedelta(days=365)
end_date = date.today()

@st.cache_data
def load_data():
    data = []
    for name, ticker in stock_pool.items():
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(start=start_date, end=end_date)
            if hist.empty:
                continue

            info = stock.info
            shares = info.get("sharesOutstanding", 0)
            price = info.get("currentPrice", None)
            sector = info.get("sector", "Unknown")
            pe = info.get("trailingPE", None)
            pb = info.get("priceToBook", None)
            mkt_cap = info.get("marketCap", 0)

            start_price = hist["Close"].iloc[0]
            end_price = hist["Close"].iloc[-1]
            growth = (end_price - start_price) / start_price * 100

            data.append({
                "Company": name,
                "Ticker": ticker,
                "Sector": sector,
                "Price": price,
                "P/E": pe,
                "P/B": pb,
                "1Y Growth (%)": round(growth, 2),
                "Market Cap (B)": round(mkt_cap / 1e9, 2),
            })
        except Exception as e:
            print(f"{ticker} error: {e}")
    return pd.DataFrame(data)

# 데이터 로딩
with st.spinner("📊 데이터 불러오는 중..."):
    df = load_data()

# 🔧 사용자 입력
st.sidebar.header("🔍 필터 조건")

budget = st.sidebar.number_input("💰 투자 예산 (USD)", min_value=100.0, step=100.0)

sector_list = sorted(df["Sector"].dropna().unique())
selected_sectors = st.sidebar.multiselect("📌 관심 업종 (복수 선택 가능)", sector_list, default=sector_list)

min_growth = st.sidebar.slider("📈 최소 시가총액 성장률 (%)", -100.0, 200.0, 10.0)
max_pe = st.sidebar.slider("💡 최대 PER (P/E)", 0.0, 100.0, 50.0)
max_pb = st.sidebar.slider("💡 최대 PBR (P/B)", 0.0, 30.0, 10.0)

# 필터링
filtered_df = df[
    (df["Sector"].isin(selected_sectors)) &
    (df["Price"] <= budget) &
    (df["1Y Growth (%)"] >= min_growth) &
    ((df["P/E"].isnull()) | (df["P/E"] <= max_pe)) &
    ((df["P/B"].isnull()) | (df["P/B"] <= max_pb))
]

# 📊 결과 출력
st.subheader("✅ 추천 종목 리스트")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

# 📉 시가총액 추이
if not filtered_df.empty:
    st.subheader("📉 시가총액 추이 시각화")
    selected_company = st.selectbox("종목 선택", filtered_df["Company"].tolist())
    ticker = stock_pool[selected_company]
    stock = yf.Ticker(ticker)
    hist = stock.history(start=start_date, end=end_date)
    shares = stock.info.get("sharesOutstanding", 1)
    hist["Market Cap"] = hist["Close"] * shares
    hist = hist.reset_index()
    fig = px.line(hist, x="Date", y="Market Cap", title=f"{selected_company} - 1년간 시가총액 추이")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("조건에 맞는 종목이 없습니다. 필터를 완화해 보세요.")
