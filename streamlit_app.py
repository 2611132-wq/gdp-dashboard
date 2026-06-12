import streamlit as st

# 1. 데이터 정의
media = ["드라마", "영화", "숏츠", "웹툰", "예능"]
genres = [
    ["로맨스", "액션", "코믹"], 
    ["로맨스", "호러", "액션"], 
    ["댄스", "챌린지", "코믹"], 
    ["로맨스", "액션", "코믹"], 
    ["코믹", "여행", "브이로그"]
]

# 2. 웹 앱 타이틀 및 미디어 목록 표시
st.title("🎬 미디어 장르 조회기")

st.subheader("📺 미디어 목록")
# 사용자가 번호를 볼 수 있도록 리스트 출력
for i, m in enumerate(media):
    st.write(f"**{i+1}번**: {m}")

st.markdown("---")

# 3. 스트림릿 숫자 입력 위젯 (기본값 1, 최소 0, 최대 5)
n = st.number_input("번호를 입력하세요 (종료: 0)", min_value=0, max_value=5, value=1, step=1)

# 4. 조건문 처리 (원본 코드의 로직 반영)
if n == 0:
    st.warning("🚪 프로그램을 종료합니다. (다시 시작하려면 번호를 변경하세요)")
elif 1 <= n <= 5:
    selected_media = media[n-1]
    selected_genres = genres[n-1]
    
    # 결과 예쁘게 출력하기
    st.success(f"### ✅ 선택한 미디어: {selected_media}")
    st.info(f"**장르:** {', '.join(selected_genres)}")
else:
    st.error("❌ 오류: 올바른 번호가 아닙니다.")