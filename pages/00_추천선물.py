import streamlit as st
from datetime import datetime

# 🎉 타이틀
st.markdown("<h1 style='text-align:center; color:#ff9999;'>🎁 맞춤형 선물 추천</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>상대방의 취향을 바탕으로 완벽한 선물을 찾아드려요!</p>", unsafe_allow_html=True)
st.markdown("---")

# 🗓️ 날짜
today = datetime.now().strftime("%Y년 %m월 %d일")
st.markdown(f"📅 오늘은 **{today}** 입니다.")

# 📌 정보 입력
st.markdown("## 🧑 상대 정보 입력")

gender = st.radio("성별은 무엇인가요?", ["남성", "여성", "기타/모름"], horizontal=True)

age_group = st.selectbox("나이대는 어떻게 되나요?", ["10대", "20대", "30대", "40대", "50대 이상"])

interests = st.multiselect(
    "관심사를 선택해주세요 (복수 선택 가능)", 
    ["패션", "IT/전자기기", "여행", "게임", "미술", "음악", "독서", "운동", "인테리어", "요리", "반려동물"]
)

style = st.radio("스타일은 어떤 편인가요?", ["귀엽고 아기자기", "감성적이고 따뜻함", "실용적", "화려하고 세련됨", "모던하고 심플함"], horizontal=False)

personality = st.selectbox("성격은 어떤가요?", ["외향적", "내향적", "섬세함", "유쾌함", "조용함", "활동적"])

situation = st.selectbox("요즘 그 사람은 어떤 상황인가요?", [
    "취업/입학 준비 중", 
    "직장생활 중", 
    "여행 준비 중", 
    "연애 중", 
    "감정적으로 지쳐 있는 상태", 
    "기념일/생일이 곧 있음",
    "스트레스를 많이 받는 중"
])

st.markdown("---")
st.subheader("💡 선물 추천 총평")

# 🎯 총평 생성
summary = "선물을 고르실 때, 다음과 같은 요소들을 고려해보세요: "

# 성별 + 나이
if gender == "남성":
    summary += "상대는 남성이며, "
elif gender == "여성":
    summary += "상대는 여성이며, "
else:
    summary += "상대의 성별은 명확하지 않지만, "

summary += f"{age_group}입니다. "

# 스타일 + 성격
summary += f"{style} 스타일을 선호하고, 성격은 {personality}인 편이에요. "

# 관심사
if interests:
    summary += "특히 관심 있는 분야는 " + ", ".join(interests) + " 입니다. "

# 상황 기반 추천
if situation == "취업/입학 준비 중":
    summary += "요즘 취업이나 입학 준비 중이라 실용적이고 응원 메시지가 담긴 선물이 좋아요. 예: 고급 펜, 노트북 파우치, 동기부여 책"
elif situation == "직장생활 중":
    summary += "직장 생활 중이라면 실용적이면서도 스트레스를 줄여줄 선물이 좋아요. 예: 고급 텀블러, 안마기, 간식 박스"
elif situation == "여행 준비 중":
    summary += "여행 준비 중이라면 여행용 파우치나 미니 캐리어, 휴대용 충전기 같은 것이 좋겠네요."
elif situation == "연애 중":
    summary += "연애 중이라면 감성적인 선물도 좋아요. 예: 커플템, 향수, 손편지와 함께하는 기프트"
elif situation == "감정적으로 지쳐 있는 상태":
    summary += "지쳐있는 상태라면 위로와 안정감을 줄 수 있는 선물을 추천해요. 예: 아로마캔들, 따뜻한 담요, 힐링 책"
elif situation == "기념일/생일이 곧 있음":
    summary += "기념일이 다가오고 있으니 특별하고 의미 있는 선물이 좋아요. 예: 맞춤 포토 앨범, 이름 각인 소품"
elif situation == "스트레스를 많이 받는 중":
    summary += "스트레스를 많이 받는 시기에는 휴식을 줄 수 있는 선물이 좋아요. 예: 입욕제, 마사지기, 베개"

# 마지막 제안 마무리
summary += " 💝 상대방의 상황과 취향을 잘 고려한 선물은 마음을 깊이 전할 수 있어요."

# 출력
st.markdown(
    f"<div style='background-color:#fff0f5; padding:20px; border-radius:10px;'>"
    f"<p style='font-size:16px'>{summary}</p>"
    f"</div>",
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown("<p style='text-align:center;'>🎀 정성 가득한 선물로 당신의 마음을 전해보세요!</p>", unsafe_allow_html=True)
