import streamlit as st
from datetime import datetime

# 💖 타이틀
st.markdown("<h1 style='text-align:center; color:#ff6699;'>💌 상황별 고백 방법 & 멘트 추천</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>당신의 상황에 맞춘 완벽한 고백 전략과 멘트를 알려드릴게요!</p>", unsafe_allow_html=True)
st.markdown("---")

# 📅 날짜
today = datetime.now().strftime("%Y년 %m월 %d일")
st.markdown(f"📅 오늘은 **{today}** 입니다.")

# 📌 사용자 정보 입력
st.markdown("## 💁 고백 상황 정보 입력")

age = st.selectbox("🧑 당신의 나이는?", ["10대", "20대", "30대", "40대 이상"])
relationship = st.radio("👫 현재 상대방과의 관계는?", ["친구", "동료", "오래 알고 지낸 사이", "소개팅 중", "온라인에서 알게 됨", "자주 마주치지만 말은 잘 안 함"])
your_personality = st.selectbox("😊 당신의 성격은?", ["내향적", "외향적", "감성적", "직설적", "차분함"])
confess_timing = st.selectbox("⏰ 고백하려는 시점은?", ["만난 지 얼마 안 됨", "몇 달 이상 만남", "썸 타는 중", "상대가 눈치 챈 것 같음", "이미 거절당한 적 있음"])
place_preference = st.radio("📍 고백 장소는 어디쯤이 좋을까요?", ["카페", "산책길", "공원/야외", "메신저/문자", "집 앞", "이벤트 공간"])

st.markdown("---")

# ✅ 추천 생성
st.subheader("💡 추천 고백 방법")

method = "당신의 상황을 분석한 결과, 다음과 같은 고백 방식을 추천드려요: "

if age == "10대":
    method += "풋풋하고 솔직한 표현이 좋아요. 부담 없는 분위기에서 진심을 전해보세요. "
elif age == "20대":
    method += "센스와 진심을 함께 담은 자연스러운 고백이 어울립니다. "
elif age == "30대":
    method += "신중하지만 확신 있는 고백이 인상 깊을 거예요. "
else:
    method += "성숙하고 진중한 분위기 속에서 감정을 전하는 것이 좋습니다. "

if relationship in ["친구", "오래 알고 지낸 사이"]:
    method += "익숙한 관계일수록 진지하고 조심스럽게 접근하세요. "
elif relationship == "동료":
    method += "상황을 고려한 차분한 분위기에서 담백한 고백이 어울립니다. "
elif relationship == "소개팅 중":
    method += "좋은 분위기를 유지하며 솔직하게 감정을 표현하세요. "
elif relationship == "온라인에서 알게 됨":
    method += "만남이 있다면 직접, 없다면 신중한 메시지로 진심을 전달하세요. "
elif relationship == "자주 마주치지만 말은 잘 안 함":
    method += "천천히 말을 걸며 자연스럽게 관계를 쌓은 뒤 고백을 시도하세요. "

if confess_timing == "썸 타는 중":
    method += "타이밍을 놓치지 마세요! 눈빛과 분위기를 잘 활용해보세요. "

if your_personality == "내향적":
    method += "짧지만 진심이 담긴 한 문장이 강한 인상을 줄 수 있어요. "
elif your_personality == "감성적":
    method += "감정을 꾸밈없이 표현하면 상대에게 크게 와닿습니다. "

if place_preference == "산책길":
    method += "자연스러운 흐름 속에서 편안하게 이야기 나누기 좋아요. "

method += "💖 무엇보다 중요한 건 당신의 진심이에요."

# 출력
st.markdown(
    f"<div style='background-color:#fff0f5; padding:15px; border-radius:10px;'>"
    f"<p style='font-size:16px'>{method}</p>"
    f"</div>",
    unsafe_allow_html=True
)

# 💬 고백 멘트 추천
st.subheader("💬 고백 멘트 예시")

# 멘트 예시 조건부 생성
examples = []

if relationship == "친구":
    examples = [
        "우리 오래 봐왔잖아… 근데 요즘엔 그냥 친구로만 보기 어려워.",
        "솔직히 말할게. 네가 웃을 때마다 자꾸 내 마음이 흔들려."
    ]
elif relationship == "소개팅 중":
    examples = [
        "이제는 더 알고 싶고, 함께 하고 싶은 사람이 너야.",
        "만날수록 더 좋아져서, 마음 고백하고 싶었어."
    ]
elif relationship == "썸 타는 중":
    examples = [
        "혹시 나만 그런 거 아니지? 우리 마음, 같은 방향이면 좋겠어.",
        "이제는 표현하고 싶어. 너 좋아해."
    ]
elif your_personality == "감성적":
    examples = [
        "밤하늘 별처럼 널 생각하는 시간이 많아졌어.",
        "너를 생각할 때마다 마음이 따뜻해져. 그래서 용기 냈어."
    ]
else:
    examples = [
        "좋아해. 더 늦기 전에 꼭 말하고 싶었어.",
        "솔직히 말해서, 요즘 너 생각이 너무 많아."
    ]

# 예시 출력
for ex in examples:
    st.markdown(f"- 💌 *{ex}*")

st.markdown("---")
st.markdown("<p style='text-align:center;'>🌹 당신의 고백이 따뜻하게 전해지길 응원할게요!</p>", unsafe_allow_html=True)
