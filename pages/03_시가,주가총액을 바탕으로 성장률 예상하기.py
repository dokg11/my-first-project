import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import difflib

st.set_page_config(page_title="기업 성장 예측기", layout="wide")
st.title("📈 시가총액 & 주가 기반 기업 성장 예측기")

# -----------------------------
# 1. 회사명 → 티커 자동 매핑
# -----------------------------
# 수동 매핑 예시 (추후 확장 가능)
manual_map = {
    "삼성전자": "005930.KS",
    "현대차": "005380.KS",
    "LG에너지솔루션": "373220.KQ",
    "카카오": "035720.KQ",
    "네이버": "035420.KQ",
    "SK하이닉스": "000660.KS",
    "애플": "AAPL",
    "마이크로소프트": "MSFT",
    "테슬라": "TSLA",
    "구글": "GOOGL",
    "알파벳": "GOOGL",
    "아마존": "AMZN",
    "엔비디아": "NVDA",
}

# 주요 글로벌 기업 티커 리스트 (yfinance에서 검색 가능)
top_tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META", "BRK-B", "JPM", "V", "005930.KS",
    "005380.KS", "000660.KS", "035720.KQ", "035420.KQ", "373220.KQ"
]

def company_name_to_ticker(name):
    # 우선 수동 매핑 우선
    if name in manual_map:
        return manual_map[name]
    
    # yfinance에서 자동 검색
    try:
        search_result = yf.Ticker(name)
        info = search_result.info
        if 'symbol' in info and info['symbol']:
            return info['symbol']
    except:
        pass

    # 이름과 유사한 종목 추천
    close_match = difflib.get_close_matches(name.upper(), top_tickers, n=1)
    if close_match:
        return close_match[0]
    return None

# -----------------------------
# 2. 사용자 입력
# -----------------------------
company_input = st.text_input("🔍 분석할 기업명을 입력하세요 (예: 삼성전자, Apple, 테슬라 등)", value="삼성전자")

ticker_input = company_name_to_ticker(company_input)

if ticker_input:
    try:
        # 날짜 범위 설정
        end_date = datetime.today()
        start_date = end_date - timedelta(days=365 * 5)
        stock = yf.Ticker(ticker_input)
        hist = stock.history(start=start_date, end=end_date)

        if hist.empty:
            st.warning("📉 데이터를 찾을 수 없습니다. 올바른 티커를 입력했는지 확인해보세요.")
        else:
            info = stock.info
            market_cap = info.get("marketCap", None)
            company_name = info.get("shortName", company_input)

            st.subheader(f"📊 {company_name} ({ticker_input}) 시가총액 및 주가 분석")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("💰 현재 시가총액", f"${market_cap/1e9:.2f}B" if market_cap else "N/A")
            with col2:
                st.metric("📅 분석기간", f"{start_date.date()} ~ {end_date.date()}")

            # 주가 그래프 출력
            st.markdown("### 📉 주가 추이")
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(hist.index, hist['Close'], label='종가', color='blue')
            ax.set_xlabel("날짜")
            ax.set_ylabel("주가 ($)")
            ax.set_title("과거 주가")
            ax.grid(True)
            st.pyplot(fig)

            # CAGR 계산
            start_price = hist['Close'].iloc[0]
            end_price = hist['Close'].iloc[-1]
            cagr = ((end_price / start_price) ** (1 / 5) - 1) * 100

            st.markdown("### 📈 성장 분석")
            st.success(f"📌 최근 5년 간 연평균 성장률(CAGR): **{cagr:.2f}%**")

            # 미래 시가총액 예측
            if market_cap:
                future_5y_cap = market_cap * ((1 + cagr / 100) ** 5)
                st.markdown("### 🔮 성장 예측")
                st.info(f"예상 5년 후 시가총액 (단순 예측): **${future_5y_cap/1e9:.2f}B**")

            # 매수 판단
            st.markdown("### 🧐 그래서 이 주식을 사야 할까?")
            recommendation = "❓ 판단 보류"
            if cagr > 10:
                if market_cap and market_cap < 1e11:
                    recommendation = "✅ 매수 고려 가능 (고성장 + 중소형 시총)"
                else:
                    recommendation = "🟡 성장성은 좋지만 시총이 이미 큼 (안정적)"
            elif cagr > 0:
                recommendation = "⚠️ 성장은 있지만 제한적"
            else:
                recommendation = "❌ 최근 5년간 주가 하락 - 투자 신중 필요"

            st.subheader(recommendation)
            st.caption("※ 이 판단은 단순 참고용이며, 실제 투자 결정은 본인의 책임입니다.")

    except Exception as e:
        st.error(f"에러가 발생했습니다: {e}")
else:
    st.error("해당 기업명을 티커로 변환할 수 없습니다. 다른 이름이나 영어명을 시도해보세요.")
