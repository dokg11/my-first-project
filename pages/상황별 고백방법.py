import streamlit as st
from datetime import datetime

# 💖 타이틀
st.markdown("<h1 style='text-align:center; color:#ff6699;'>💌 고백 방법 추천기</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>당신의 상황에 딱 맞는 고백 방법을 알려드릴게요!</p>", unsafe_allow_html=True)
st.markdown("---")

# 📅 오늘 날짜
today = datetime.now().strftime("%Y년 %m월 %d일")
st.markdown(f"📅 오늘은 **{today}** 입니다.")

# 📌 정보 입력
st.markdown("## 💁 고백 상황 정보 입력")

age = st.selectbox("🧑 당신의 나이는?", ["10대", "20대", "30대", "40대 이상"])

relationship = st.radio(
    "👫 현재 상대방과의 관계는?", 
    ["친구", "동료", "오래 알고 지낸 사이", "소개팅 중", "온라인에서 알게 됨", "자주 마주치지만 말은 잘 안 함"],
    horizontal=False
)

your_personality = st.selectbox("😊 당신의 성격은?", ["내향적", "외향적", "감성적", "직설적", "차분함"])

confess_timing = st.selectbox("⏰ 고백하려는 시점은?", ["만난 지 얼마 안 됨", "몇 달 이상 만남", "썸 타는 중", "상대가 눈치 챈 것 같음", "이미 거절당한 적 있음"])

place_preference = st.radio("📍 고백 장소는 어디쯤이 좋을까요?", ["카페", "산책길", "공원/야외", "메신저/문자", "집 앞", "이벤트 공간"], horizontal=True)

st.markdown("---")
st.subheader("💡 추천 고백 방법")

# 💌 고백 방법 문장 생성
summary = "당신의 상황을 분석한 결과, 다음과 같은 고백 방식을 추천드려요: "

# 나이 기반
if age == "10대":
    summary += "풋풋하고 솔직한 표현이 좋은 나이예요. 부담 없는 분위기가 중요해요. "
elif age == "20대":
    summary += "자연스럽고 센스 있는 표현이 중요하며, 진심이 묻어나야 해요. "
elif age == "30대":
    summary += "신중하면서도 확신 있는 표현이 어필돼요. 상대의 상황을 배려하는 말투가 중요해요. "
else:
    summary += "진정성과 배려가 가장 큰 설득력이 되는 시기예요. 성숙한 대화가 중심이 되면 좋아요. "

# 관계 기반
if relationship == "친구":
    summary += "친구에서 연인으로 넘어가려면, 익숙함을 깨는 진지한 분위기 조성이 중요해요. "
elif relationship == "동료":
    summary += "직장/학교 분위기를 고려한 담백하고 조심스러운 고백이 좋습니다. "
elif relationship == "오래 알고 지낸 사이":
    summary += "오랜 신뢰를 무기로 자연스럽게 감정을 표현하면 좋아요. "
elif relationship == "소개팅 중":
    summary += "상대의 반응을 충분히 확인한 후 솔직한 고백이 적절해요. "
elif relationship == "온라인에서 알게 됨":
    summary += "직접 만나는 타이밍에 진정성을 보여주는 것이 관건이에요. "
elif relationship == "자주 마주치지만 말은 잘 안 함":
    summary += "먼저 다가가는 용기와 함께 조심스러운 분위기 조성이 중요해요. "

# 성격
if your_personality == "내향적":
    summary += "짧고 진심 어린 말 한 마디가 큰 울림을 줄 수 있어요. 준비된 한 문장이 중요해요. "
elif your_personality == "외향적":
    summary += "활기찬 분위기 속에서 감정을 자연스럽게 드러내면 좋아요. "
elif your_personality == "감성적":
    summary += "감정 표현에 자신 있다면 직접 손편지나 음악 선물도 효과적이에요. "
elif your_personality == "직설적":
    summary += "단도직입적으로 솔직하게 전하되, 감정은 부드럽게 표현하는 것이 좋아요. "
elif your_personality == "차분함":
    summary += "조용한 장소에서 진중하게 감정을 나누는 것이 어울려요. "

# 타이밍
if confess_timing == "만난 지 얼마 안 됨":
    summary += "상대의 반응을 천천히 살핀 뒤 고백하는 게 좋아요. 바로 표현보다는 작은 관심 표현부터 시작해요. "
elif confess_timing == "몇 달 이상 만남":
    summary += "이제 감정을 확실히 표현해도 좋아요. 상대로부터 기다리고 있을 가능성도 높아요. "
elif confess_timing == "썸 타는 중":
    summary += "분위기가 무르익었을 때 확실한 한 방이 필요해요. 영화 같은 고백도 어울려요. "
elif confess_timing == "상대가 눈치 챈 것 같음":
    summary += "자연스럽게 끌고 가다가 어느 순간 툭! 하고 고백하는 게 효과적이에요. "
elif confess_timing == "이미 거절당한 적 있음":
    summary += "상대가 부담스럽지 않도록, 편지나 거리를 두고 마음을 전하는 방식을 추천해요. "

# 장소
if place_preference == "카페":
    summary += "잔잔한 카페에서의 고백은 부담 없고 대화에 집중할 수 있어요. "
elif place_preference == "산책길":
    summary += "산책하며 자연스럽게 분위기를 만들고 고백하는 것이 좋아요. "
elif place_preference == "공원/야외":
    summary += "탁 트인 장소에서는 감정을 담아 자유롭게 이야기할 수 있어요. "
elif place_preference == "메신저/문자":
    summary += "직접은 어렵지만 진심을 정리해서 전달할 수 있어요. 신중하게 표현하세요. "
elif place_preference == "집 앞":
    summary += "깜짝 등장과 함께 고백하면 기억에 오래 남을 수 있어요. 조심스럽게 계획하세요. "
elif place_preference == "이벤트 공간":
    summary += "특별한 순간을 연출하고 싶다면 이곳도 좋아요. 단, 상대가 부담스러워하지 않게 유의해요. "

# 🎁 최종 출력
summary += "💖 당신만의 분위기와 진심이 담긴 고백이 가장 큰 힘이 될 거예요!"

st.markdown(
    f"<div style='background-color:#fff0f5; padding:20px; border-radius:10px;'>"
    f"<p style='font-size:16px'>{summary}</p>"
    f"</div>",
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown("<p style='text-align:center;'>🌹 용기 내세요. 진심은 언제나 전해집니다.</p>", unsafe_allow_html=True)
