import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="한국인이 사랑하는 여행지 지도", page_icon="🗺️", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #FF69B4;'>🗺️ 한국인이 사랑하는 TOP 10 여행지 지도 🗺️</h1>",
    unsafe_allow_html=True
)

# 여행지 정보 (위도/경도 포함)
travel_data = [
    {"name": "서울", "lat": 37.5665, "lon": 126.9780, "desc": "대한민국의 수도이자 문화 중심지"},
    {"name": "제주도", "lat": 33.4996, "lon": 126.5312, "desc": "자연이 살아 숨 쉬는 아름다운 섬"},
    {"name": "부산", "lat": 35.1796, "lon": 129.0756, "desc": "해운대, 광안대교로 유명한 항구 도시"},
    {"name": "경주", "lat": 35.8562, "lon": 129.2247, "desc": "천년 고도의 문화유산 도시"},
    {"name": "강릉", "lat": 37.7519, "lon": 128.8761, "desc": "푸른 동해와 커피 향 가득한 도시"},
    {"name": "속초", "lat": 38.2048, "lon": 128.5911, "desc": "설악산과 바다의 만남, 속초"},
    {"name": "전주", "lat": 35.8242, "lon": 127.1480, "desc": "한옥마을과 전통 한식의 도시"},
    {"name": "여수", "lat": 34.7604, "lon": 127.6622, "desc": "밤바다로 낭만 가득한 남해 도시"},
    {"name": "인천", "lat": 37.4563, "lon": 126.7052, "desc": "국제공항과 차이나타운의 도시"},
    {"name": "남해", "lat": 34.8373, "lon": 127.8925, "desc": "독일마을과 다랭이마을의 아름다움"},
]

df = pd.DataFrame(travel_data)

# 지도 표시
st.map(df[['lat', 'lon']], zoom=6)

# 여행지 설명 표시
st.markdown("### 📝 여행지 설명")

for spot in travel_data:
    st.markdown(f"**{spot['name']}** – {spot['desc']}")

# 하단 인삿말
st.markdown("---")
st.markdown(
    "<h4 style='text-align: center; color: #FFB6C1;'>💕 지도에서 다음 여행지를 골라보세요! 💕</h4>",
    unsafe_allow_html=True
)
