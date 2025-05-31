import streamlit as st
from datetime import datetime

# 🎀 타이틀
st.markdown("<h1 style='text-align:center; color:#ff66cc;'>🧥 오늘의 패션 추천 총평 👚</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>🎨 좋아하는 색 + 날씨 + 기온 = 완벽한 스타일 추천!</p>", unsafe_allow_html=True)
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

st.markdown("---")
st.subheader("💡 오늘의 패션 총평")

# 🧠 총평 생성
summary = ""

# 1. 색 기반 문장
if "빨강" in color:
    summary += "오늘은 강렬하고 에너지 넘치는 빨강을 좋아하시네요. "
elif "파랑" in color:
    summary += "차분하고 시원한 느낌의 파랑을 선택하셨군요. "
elif "노랑" in color:
    summary += "밝고 경쾌한 노랑은 기분을 업 시켜줘요. "
elif "초록" in color:
    summary += "자연스럽고 편안한 초록은 오늘 잘 어울리는 색이에요. "
elif "검정" in color:
    summary += "모던하고 시크한 블랙으로 멋을 낼 수 있어요. "
elif "하양" in color:
    summary += "깔끔하고 순수한 하양으로 심플한 멋을 더해보세요. "
elif "보라" in color:
    summary += "감성적이고 신비로운 보라는 오늘 기분과 잘 어울려요. "
elif "분홍" in color:
    summary += "사랑스럽고 부드러운 핑크로 매력을 뽐내보세요. "

# 2. 날씨 기반 문장
if weather == "맑음":
    summary += "☀️ 맑은 날씨엔 가볍고 밝은 톤의 옷이 잘 어울립니다. "
elif weather == "흐림":
    summary += "🌥️ 흐린 날에는 중간 톤이나 차분한 색상이 좋아요. "
elif weather == "비":
    summary += "🌧️ 비가 오니 방수 재질의 아우터와 어두운 톤이 유리해요. "
elif weather == "눈":
    summary += "❄️ 눈 오는 날엔 따뜻한 외투와 부츠가 필수예요. "

# 3. 온도 기반 문장
if temperature < 5:
    summary += "기온이 많이 낮으니 두꺼운 패딩이나 코트를 추천드려요. "
elif 5 <= temperature < 15:
    summary += "쌀쌀한 날씨엔 니트나 자켓이 좋습니다. "
elif 15 <= temperature < 25:
    summary += "선선한 날씨엔 가벼운 가디건이나 긴팔 셔츠가 적당해요. "
else:
    summary += "날씨가 더우니 반팔이나 시원한 소재의 옷을 추천해요. "

# ✅ 최종 출력
st.markdown(
    f"<div style='background-color:#f0f8ff; padding:20px; border-radius:10px;'>"
    f"<p style='font-size:16px'>{summary}</p>"
    f"</div>",
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown("<p style='text-align:center;'>👗 오늘도 나만의 스타일로 자신 있게! 패션도 기분도 굿~ 🎉</p>", unsafe_allow_html=True)
