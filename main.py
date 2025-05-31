import streamlit as st
from datetime import datetime

# 🎈 제목 & 설명
st.markdown("<h1 style='text-align: center; color: #ff69b4;'>👕 오늘 뭐 입지? 컬러 & 날씨로 옷 추천받기 👗</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>🎨 좋아하는 색을 선택하고, 오늘 날씨와 기온을 입력하면 스타일을 추천해드려요!</p>", unsafe_allow_html=True)
st.markdown("---")

# 📅 오늘 날짜 표시
today = datetime.now().strftime("%Y년 %m월 %d일")
st.markdown(f"<p style='text-align:center; font-size:16px;'>📅 오늘은 <strong>{today}</strong> 입니다!</p>", unsafe_allow_html=True)

# 🌤️ 날씨 입력
weather = st.selectbox("☁️ 오늘 날씨는 어떤가요?", ["맑음", "흐림", "비", "눈"])
temperature = st.slider("🌡️ 현재 기온을 선택해주세요 (°C)", min_value=-10, max_value=40, value=20)

st.markdown("---")

# 🎨 색상 선택
color = st.radio(
    "🎈 좋아하는 색을 골라보세요!",
    ["❤️ 빨강", "💙 파랑", "💛 노랑", "💚 초록", "🖤 검정", "🤍 하양", "💜 보라", "💕 분홍"],
    horizontal=True
)

st.markdown("---")
st.subheader("👚 추천 스타일")

# 🧠 추천 로직
recommendation = ""
if "빨강" in color:
    recommendation += "🔥 열정적인 빨강 아이템 추천!\n- 빨간 후드티\n- 와인색 코트\n"
elif "파랑" in color:
    recommendation += "💙 시원하고 깔끔한 블루 아이템!\n- 청자켓\n- 네이비 셔츠\n"
elif "노랑" in color:
    recommendation += "🌞 발랄한 옐로우 스타일!\n- 머스타드 니트\n- 노란 맨투맨\n"
elif "초록" in color:
    recommendation += "🌿 자연스러운 그린 스타일!\n- 카키 야상\n- 민트 셔츠\n"
elif "검정" in color:
    recommendation += "🖤 시크한 블랙 아이템!\n- 블랙 재킷\n- 다크 팬츠\n"
elif "하양" in color:
    recommendation += "🤍 깔끔한 화이트 스타일!\n- 화이트 셔츠\n- 아이보리 니트\n"
elif "보라" in color:
    recommendation += "💜 감성적인 퍼플 룩!\n- 보라 니트\n- 라일락 블라우스\n"
elif "분홍" in color:
    recommendation += "💕 사랑스러운 핑크룩!\n- 연핑크 후드\n- 로즈 티셔츠\n"

# ☁️ 날씨에 따라 추가 제안
if weather == "비":
    recommendation += "🌧️ *비가 오니 우산과 방수 소재 아이템을 챙기세요!*\n"
elif weather == "눈":
    recommendation += "❄️ *눈이 오니 두꺼운 외투와 부츠가 좋아요!*\n"
elif weather == "흐림":
    recommendation += "🌥️ *흐린 날엔 차분한 톤으로 스타일링해보세요!*\n"
elif weather == "맑음":
    recommendation += "☀️ *햇빛이 좋아요! 산뜻한 색감이 잘 어울려요!*\n"

# 🌡️ 온도에 따라 추가 제안
if temperature < 5:
    recommendation += "🧥 *매우 추워요! 두꺼운 코트나 패딩이 필수예요.*"
elif 5 <= temperature < 15:
    recommendation += "🧣 *조금 쌀쌀해요! 얇은 니트나 겉옷을 챙기세요.*"
elif 15 <= temperature < 25:
    recommendation += "👕 *선선한 날씨! 긴팔 셔츠나 가디건이 좋아요.*"
else:
    recommendation += "🩳 *더운 날이에요! 반팔과 시원한 소재 옷을 입어보세요.*"

# 💡 최종 출력
st.markdown(f"<div style='background-color:#f9f9f9;padding:20px;border-radius:10px;'><pre style='font-size:16px'>{recommendation}</pre></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center;'>🎉 오늘도 멋지고 편안한 하루 보내세요!</p>", unsafe_allow_html=True)
