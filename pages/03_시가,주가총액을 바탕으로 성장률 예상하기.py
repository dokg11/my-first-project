import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.set_page_config(page_title="기업 성장 예측기", layout="wide")
st.title("📈 시가총액 & 주가 기반 기업 성장 예측기")

ticker_input = st.text_input("🔍 종목 티커를 입력하세요 (예: AAPL, MSFT, TSLA, 삼성전자=005930.KS)", value="AAPL")

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
            company_name = info.get("shortName", ticker_input)

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
