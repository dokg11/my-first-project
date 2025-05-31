import streamlit as st
from datetime import datetime

# 🎀 타이틀
st.markdown("<h1 style='text-align:center; color:#ff66cc;'>🧥 오늘의 통합 패션 추천 👚</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>🎨 좋아하는 색 + 날씨 + 기온 + 체형을 분석해 딱 맞는 스타일을 제안해드려요!</p>", unsafe_allow_html=True)
st.markdown("---")

# 📅 날짜 표시
today = datetime.now().strftime("%Y년 %m월 %d일")
st.markdown(f"<p style='text-align:center;'>📅 오늘은 <strong>{today}</strong> 입니다.</p>", unsafe_allow_html=True)

# 🌤️ 날씨/온도 선택
weather = st.selectbox("🌦️ 오늘 날씨는 어떤가요?", ["맑음", "흐림", "비", "눈"])
temperature = st.slider("🌡️ 현재 기온은 몇 도인가요? (℃)", min_value=-10, max_value=40, value=18)

# 🎨 좋아하는 색
color = st.radio(
    "🎈 좋아하는 색깔을 골라주세요!",
    ["❤️ 빨강", "💙 파랑", "💛 노랑", "💚 초록", "🖤 검정", "🤍 하양", "💜 보라", "💕 분홍"],
    horizontal=True
)

# 🧍 체형 입력
st.markdown("### 📏 체형 정보를 알려주세요")
height = st.number_input("키 (cm)", min_value=130, max_value=220, value=170)
weight = st.number_input("몸무게 (kg)", min_value=30, max_value=150, value=65)

st.markdown("---")
st.subheader("💡 오늘의 패션 총평")

# 🧠 총평 생성
summary = ""

# 1. 색 기반 문장
if "빨강" in color:
    summary += "강렬하고 에너지 넘치는 빨강으로 포인트를 주면 활기찬 분위기를 낼 수 있어요. "
elif "파랑" in color:
    summary += "시원하고 차분한 파랑은 안정적인 느낌을 주는 스타일이에요. "
elif "노랑" in color:
    summary += "밝고 생기 있는 노랑은 활발한 인상을 줘요. "
elif "초록" in color:
    summary += "자연스러운 초록 계열은 편안함과 신뢰감을 주는 색이에요. "
elif "검정" in color:
    summary += "시크하고 모던한 검정은 어떤 스타일에도 어울리며 날씬해 보이는 효과도 있어요. "
elif "하양" in color:
    summary += "깔끔하고 순수한 하양은 깨끗하고 정돈된 느낌을 줘요. "
elif "보라" in color:
    summary += "보라는 감성적이고 세련된 이미지를 연출할 수 있어요. "
elif "분홍" in color:
    summary += "사랑스럽고 부드러운 핑크는 부드러운 인상을 줘요. "

# 2. 날씨 기반 문장
if weather == "맑음":
    summary += "☀️ 맑은 날씨엔 밝은 색감과 통기성 좋은 옷이 잘 어울려요. "
elif weather == "흐림":
    summary += "🌥️ 흐린 날에는 차분한 톤이나 톤다운된 색이 좋습니다. "
elif weather == "비":
    summary += "🌧️ 비가 오는 날엔 방수 재질의 아우터나 어두운 톤의 옷이 좋겠어요. "
elif weather == "눈":
    summary += "❄️ 눈 오는 날엔 두꺼운 외투와 방한 아이템이 필수입니다. "

# 3. 기온 기반 문장
if temperature < 5:
    summary += "기온이 매우 낮아 두꺼운 패딩, 코트와 보온 아이템이 필요해요. "
elif 5 <= temperature < 15:
    summary += "조금 쌀쌀한 날씨엔 니트나 자켓이 적당하겠어요. "
elif 15 <= temperature < 25:
    summary += "선선한 날씨에는 긴팔 셔츠나 가디건이 좋습니다. "
else:
    summary += "기온이 높아 반팔과 시원한 소재가 좋겠습니다. "

# 4. 체형 기반 문장
bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    summary += "체형이 마른 편이므로 루즈핏 스타일로 균형 잡힌 실루엣을 연출하는 것이 좋아요. "
elif 18.5 <= bmi < 23:
    summary += "체형이 균형 잡혀 있어 다양한 스타일을 소화할 수 있어요. "
elif 23 <= bmi < 27:
    summary += "조금 통통한 체형이므로 어두운 톤과 직선 라인으로 슬림한 연출이 좋아요. "
else:
    summary += "체형이 통통한 편이라면 체형 커버가 되는 A라인이나 긴 기장의 아우터가 잘 어울려요. "

# ✅ 최종 출력
st.markdown(
    f"<div style='background-color:#f8f8ff; padding:20px; border-radius:10px;'>"
    f"<p style='font-size:16px'>{summary}</p>"
    f"</div>",
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown("<p style='text-align:center;'>💖 오늘도 자신 있는 하루, 나만의 스타일로 빛나세요!</p>", unsafe_allow_html=True)
