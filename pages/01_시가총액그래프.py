import streamlit as st
import plotly.express as px
import pandas as pd
import yfinance as yf
from datetime import date, timedelta

# 타이틀
st.title("📈 전 세계 시가총액 TOP10 기업의 3년간 변화")

# 시가총액 기준 상위 10개 기업 (2024년 기준, Ticker 기준)
top10_companies = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Saudi Aramco': '2222.SR',
    'Alphabet (Google)': 'GOOGL',
    'Amazon': 'AMZN',
    'Nvidia': 'NVDA',
    'Berkshire Hathaway': 'BRK-B',
    'Meta (Facebook)': 'META',
    'Tesla': 'TSLA',
    'TSMC': 'TSM'
}

# 날짜 범위 설정
end_date = date.today()
start_date = end_date - timedelta(days=3*365)

# 데이터 가져오기
@st.cache_data
def get_market_cap_data(tickers, start, end):
    data = {}
    for name, ticker in tickers.items():
        stock = yf.Ticker(ticker)
        df = stock.history(start=start, end=end)
        if 'Close' in df.columns and not df.empty:
            df = df[['Close']].copy()
            df['Market Cap'] = df['Close'] * stock.info.get('sharesOutstanding', 1)
            df['Company'] = name
            df = df.reset_index()
            data[name] = df[['Date', 'Market Cap', 'Company']]
    combined = pd.concat(data.values())
    return combined

with st.spinner("데이터 불러오는 중..."):
    df = get_market_cap_data(top10_companies, start_date, end_date)

# Plotly 그래프 그리기
fig = px.line(df, x='Date', y='Market Cap', color='Company',
              title='전 세계 시가총액 TOP10 기업의 시가총액 변화 (최근 3년)',
              labels={'Market Cap': '시가총액 (USD)', 'Date': '날짜'},
              hover_name='Company')

fig.update_layout(hovermode="x unified", height=600)

st.plotly_chart(fig, use_container_width=True)
