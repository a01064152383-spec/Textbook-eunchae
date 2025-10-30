import streamlit as st
import random
import pandas as pd

# 앱 기본 설정
st.set_page_config(page_title="🍀 로또 번호 생성기", layout="centered")

# 헤더
st.title("🇰🇷 대한민국 로또 번호 생성기")
st.subheader("1부터 45까지의 숫자 중 6개의 고유한 숫자를 추천합니다.")

# 게임 수 입력 (슬라이더 사용, 1부터 10까지)
game_count = st.slider(
    "몇 게임을 생성하시겠어요? (1~10)",
    min_value=1,
    max_value=10,
    value=5,  # 기본값 5게임
    step=1
)

# 로또 번호 생성 함수
def generate_lotto_numbers(count):
    """지정된 횟수만큼 로또 번호 조합(1-45 중 6개, 오름차순 정렬)을 생성합니다."""
    results = []
    for i in range(count):
        # 1부터 45까지의 숫자 중 중복 없이 6개의 숫자를 무작위로 추출
        numbers = random.sample(range(1, 46), 6)
        # 오름차순으로 정렬
        numbers.sort()
        results.append(numbers)
    return results

# 생성 버튼
if st.button("✨ 로또 번호 생성하기"):
    # 로딩 메시지 표시
    with st.spinner(f'{game_count}게임의 로또 번호를 생성 중...'):
        lotto_combinations = generate_lotto_numbers(game_count)
    
    # 결과 출력
    st.success(f"총 **{game_count}** 게임의 로또 번호 추천입니다!")
    
    # 결과를 보기 쉽게 데이터프레임으로 정리
    data = {}
    
    # 열 이름은 "번호 1", "번호 2", ... 로 설정
    for i in range(6):
        data[f"번호 {i+1}"] = [combo[i] for combo in lotto_combinations]
        
    df = pd.DataFrame(data)
    
    # 인덱스(게임 번호)를 1부터 시작하도록 설정
    df.index = [f"Game {i+1}" for i in range(game_count)]
    
    # 스타일링을 적용하여 결과 출력 (숫자 강조)
    st.dataframe(df.style.applymap(lambda x: 'background-color: lightgreen; font-weight: bold'), use_container_width=True)
    
    st.balloons()

# 안내 메시지
st.markdown(
    """
    ---
    **사용 방법:**
    1. 위의 슬라이더를 사용하여 원하는 게임 수(1~10)를 선택하세요.
    2. '로또 번호 생성하기' 버튼을 누르면, 선택한 수만큼의 로또 번호 조합을 추천해 드립니다.
    """
)
