import streamlit as st

# 페이지 설정
st.set_page_config(page_title="한국인이 사랑하는 여행지 TOP10", page_icon="🌸", layout="wide")

# 타이틀
st.markdown(
    "<h1 style='text-align: center; color: #FF69B4;'>🌸 한국인이 사랑하는 여행지 TOP 10 🌸</h1>",
    unsafe_allow_html=True,
)
st.markdown("---")

# 여행지 데이터
travel_spots = [
    {"name": "서울", "emoji": "🏙️", "desc": "대한민국의 수도이자 문화, 쇼핑, 음식의 중심지예요! 경복궁, 한강, 홍대 거리에서 다양한 즐거움을 느껴보세요."},
    {"name": "제주도", "emoji": "🌋", "desc": "자연이 살아 숨 쉬는 섬! 한라산, 협재해수욕장, 오름, 돌하르방까지! 휴식과 힐링을 위한 완벽한 여행지예요."},
    {"name": "부산", "emoji": "🌊", "desc": "해운대와 광안대교로 유명한 바다 도시! 활기찬 시장과 시원한 해변을 동시에 즐겨보세요."},
    {"name": "경주", "emoji": "🏺", "desc": "신라 천년의 고도, 찬란한 문화유산이 가득한 도시예요. 불국사, 첨성대, 황리단길을 거닐어 보세요."},
    {"name": "강릉", "emoji": "🏖️", "desc": "동해안의 푸른 바다와 커피거리, 그리고 경포대! 로맨틱한 여행지로 인기 만점이에요."},
    {"name": "속초", "emoji": "🦀", "desc": "설악산의 웅장한 자연과 속초 중앙시장, 바다 풍경이 어우러진 아름다운 도시예요."},
    {"name": "전주", "emoji": "🏘️", "desc": "한옥마을과 전통음식이 유명한 도시! 전주비빔밥과 함께 한국의 멋을 느껴보세요."},
    {"name": "여수", "emoji": "🌉", "desc": "밤바다로 유명한 낭만 도시 여수! 돌산공원, 오동도, 낭만포차거리로 여행을 떠나보세요."},
    {"name": "인천", "emoji": "✈️", "desc": "공항의 도시에서 차이나타운, 송도 센트럴파크까지 도심 속 이색 여행을 즐겨보세요."},
    {"name": "남해", "emoji": "🏞️", "desc": "자연과 바다가 어우러진 힐링 명소! 독일마을, 다랭이마을 등 예쁜 여행지로 가득해요."},
]

# 컬럼 기반 레이아웃
for i in range(0, len(travel_spots), 2):
    col1, col2 = st.columns(2)
    with col1:
        spot = travel_spots[i]
        st.markdown(f"### {spot['emoji']} {spot['name']}")
        st.markdown(f"<div style='background-color:#FFF0F5; padding:10px; border-radius:10px;'>{spot['desc']}</div>", unsafe_allow_html=True)

    if i + 1 < len(travel_spots):
        with col2:
            spot = travel_spots[i + 1]
            st.markdown(f"### {spot['emoji']} {spot['name']}")
            st.markdown(f"<div style='background-color:#FFF0F5; padding:10px; border-radius:10px;'>{spot['desc']}</div>", unsafe_allow_html=True)

# 하단 인삿말
st.markdown("---")
st.markdown(
    "<h3 style='text-align: center; color: #FFB6C1;'>💖 여러분의 다음 여행지는 어디인가요? 행복한 여행 되세요! 💖</h3>",
    unsafe_allow_html=True,
)
