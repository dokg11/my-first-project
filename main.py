import streamlit as st

# 제목 꾸미기
st.markdown(
    "<h1 style='text-align: center; color: #ff69b4;'>👗 나에게 어울리는 옷 색은? 👕</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size: 18px;'>🎨 좋아하는 색을 선택하면 그 색의 스타일을 추천해드릴게요!</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# 색상 선택
color = st.radio(
    "👇 아래에서 좋아하는 색을 골라보세요!",
    ["❤️ 빨강", "💙 파랑", "💛 노랑", "💚 초록", "🖤 검정", "🤍 하양", "💜 보라", "💕 분홍"],
    horizontal=True
)

st.markdown("---")

# 추천 결과
st.subheader("👚 추천 스타일:")

if "빨강" in color:
    st.markdown("<div style='background-color:#ffdddd;padding:20px;border-radius:10px;'>"
                "🔥 열정 가득! <br> - 빨간 후드티<br> - 레드 원피스<br> - 와인색 코트"
                "</div>", unsafe_allow_html=True)
elif "파랑" in color:
    st.markdown("<div style='background-color:#ddeeff;padding:20px;border-radius:10px;'>"
                "💙 시원하고 청량한!<br> - 청자켓<br> - 파란 셔츠<br> - 네이비 맨투맨"
                "</div>", unsafe_allow_html=True)
elif "노랑" in color:
    st.markdown("<div style='background-color:#fff5cc;padding:20px;border-radius:10px;'>"
                "🌞 밝고 상큼한!<br> - 노란 맨투맨<br> - 머스타드 니트<br> - 레몬 컬러 원피스"
                "</div>", unsafe_allow_html=True)
elif "초록" in color:
    st.markdown("<div style='background-color:#ddffdd;padding:20px;border-radius:10px;'>"
                "🌿 자연 친화 스타일!<br> - 카키 야상<br> - 민트 셔츠<br> - 올리브 니트"
                "</div>", unsafe_allow_html=True)
elif "검정" in color:
    st.markdown("<div style='background-color:#cccccc;padding:20px;border-radius:10px;'>"
                "🖤 시크하고 세련되게!<br> - 블랙 재킷<br> - 검정 슬랙스<br> - 다크 티셔츠"
                "</div>", unsafe_allow_html=True)
elif "하양" in color:
    st.markdown("<div style='background-color:#f9f9f9;padding:20px;border-radius:10px;'>"
                "🤍 깨끗하고 깔끔하게!<br> - 화이트 셔츠<br> - 아이보리 니트<br> - 흰색 원피스"
                "</div>", unsafe_allow_html=True)
elif "보라" in color:
    st.markdown("<div style='background-color:#f5e6ff;padding:20px;border-radius:10px;'>"
                "💜 감성 충만!<br> - 퍼플 맨투맨<br> - 보라색 니트<br> - 라일락 블라우스"
                "</div>", unsafe_allow_html=True)
elif "분홍" in color:
    st.markdown("<div style='background-color:#ffe6f0;padding:20px;border-radius:10px;'>"
                "💕 사랑스러운 스타일!<br> - 핑크 후드<br> - 로즈 티셔츠<br> - 연분홍 원피스"
                "</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>👗 옷은 나의 색을 담는 캔버스! 오늘도 나만의 색으로 빛나세요 ✨</p>", unsafe_allow_html=True)
