import streamlit as st
import random
import sympy

# -----------------
# 1. 앱 설정 및 제목
# -----------------
st.set_page_config(page_title="유리함수의 역함수 마스터 🎓", layout="centered")
st.title("유리함수의 역함수 마스터 🎓")
st.markdown("---")

# -----------------
# 2. 개념 학습 섹션
# -----------------
st.header("1. 유리함수의 역함수 개념 학습")

st.markdown("""
유리함수 $f(x) = \frac{ax + b}{cx + d}$ ($c \neq 0, ad - bc \neq 0$)의 역함수 $f^{-1}(x)$는 $x$와 $y$를 바꾸어 구합니다.
이때, 역함수를 쉽게 구하는 공식은 다음과 같습니다.
""")

# 공식 표시
st.latex(r'''
f(x) = \frac{ax + b}{cx + d} \quad \xrightarrow{\text{역함수}} \quad f^{-1}(x) = \frac{-dx + b}{cx - a}
''')

st.markdown("""
🔑 **핵심:** 원래 함수의 분자 $x$ 계수 **$a$**와 분모 상수항 **$d$**의 **위치와 부호를 서로 바꿉니다.**
""")
st.info("💡 $ad - bc \neq 0$ 일 때만 역함수가 존재하며, 분수함수의 점근선은 $y=x$에 대해 대칭이 됩니다. ")
st.markdown("---")

# -----------------
# 3. 문제 생성 함수 (세션 상태 관리)
# -----------------

def generate_problem():
    """역함수 문제가 될 수 있는 계수 (a, b, c, d)를 생성합니다."""
    # a, b, c, d를 -5부터 5 사이의 정수로 무작위 생성 (단, 0은 제외)
    
    while True:
        # 무작위 계수 생성
        a = random.randint(-5, 5)
        b = random.randint(-5, 5)
        c = random.choice([x for x in range(-5, 6) if x != 0]) # c는 0이 아니어야 함
        d = random.randint(-5, 5)
        
        # 역함수 존재 조건: ad - bc != 0
        if (a * d - b * c) != 0:
            break
            
    # 정답 계수 계산 (역함수 공식: (-d)x + b / cx + (-a))
    inv_a = -d
    inv_b = b
    inv_c = c
    inv_d = -a
    
    # 세션 상태에 저장 (상태 유지)
    st.session_state.problem_a = a
    st.session_state.problem_b = b
    st.session_state.problem_c = c
    st.session_state.problem_d = d
    st.session_state.inv_a = inv_a
    st.session_state.inv_b = inv_b
    st.session_state.inv_c = inv_c
    st.session_state.inv_d = inv_d
    st.session_state.checked = False # 채점 여부 초기화

# 초기 문제 생성 (앱 시작 시)
if 'problem_a' not in st.session_state:
    generate_problem()

# -----------------
# 4. 문제 풀이 섹션
# -----------------

st.header("2. 역함수 문제 풀이")
st.subheader("아래 함수의 역함수를 구하시오.")

# 현재 문제 표시
a = st.session_state.problem_a
b = st.session_state.problem_b
c = st.session_state.problem_c
d = st.session_state.problem_d

st.latex(f'''
f(x) = \frac{{{a}x + {b}}}{{{c}x + {d}}}
''')

st.markdown("---")

# -----------------
# 5. 사용자 입력 및 채점 로직
# -----------------

# 정답 입력 필드
st.subheader("🔑 정답 입력")
st.markdown("$$f^{-1}(x) = \\frac{A x + B}{C x + D}$$ 일 때, A, B, C, D의 값을 입력하세요.")

col1, col2 = st.columns(2)
with col1:
    user_inv_a = st.number_input("분자 $x$ 계수 (A):", key="user_inv_a", value=0, format="%d")
    user_inv_b = st.number_input("분자 상수항 (B):", key="user_inv_b", value=0, format="%d")

with col2:
    user_inv_c = st.number_input("분모 $x$ 계수 (C):", key="user_inv_c", value=0, format="%d")
    user_inv_d = st.number_input("분모 상수항 (D):", key="user_inv_d", value=0, format="%d")


def check_answer():
    """사용자 입력과 정답을 비교하여 채점합니다."""
    st.session_state.checked = True
    
    # 정답 계수
    inv_a = st.session_state.inv_a
    inv_b = st.session_state.inv_b
    inv_c = st.session_state.inv_c
    inv_d = st.session_state.inv_d
    
    # 사용자 입력 계수
    user_a = st.session_state.user_inv_a
    user_b = st.session_state.user_inv_b
    user_c = st.session_state.user_inv_c
    user_d = st.session_state.user_inv_d
    
    # 분수 형태의 역함수는 분자/분모에 상수 k를 곱해도 같은 함수이므로,
    # **두 분수식의 비례 관계**를 확인해야 합니다.
    # 즉, (user_A / 정답_A) = (user_B / 정답_B) = (user_C / 정답_C) = (user_D / 정답_D)를 만족해야 합니다.
    
    # 간단하게는, 사용자가 입력한 계수들이 정답 계수들의 *정수 배*인지를 확인합니다.
    try:
        if inv_a != 0:
            ratio = user_a / inv_a
        elif inv_c != 0:
            ratio = user_c / inv_c
        else:
             # ad - bc != 0 조건 때문에 이 경우는 거의 발생하지 않음
             ratio = 1 
             
        # 정답과 입력 값의 비율이 모두 같고, 입력값에 0이 아닌 계수가 하나라도 있으면 정답
        is_correct = (
            (user_a == inv_a * ratio) and 
            (user_b == inv_b * ratio) and 
            (user_c == inv_c * ratio) and 
            (user_d == inv_d * ratio) and
            (ratio != 0)
        )
        
    except ZeroDivisionError:
        # 정답 계수와 사용자 계수가 모두 0인 경우를 처리 (간단화를 위해)
        is_correct = (user_a == inv_a) and (user_b == inv_b) and (user_c == inv_c) and (user_d == inv_d)

    
    if is_correct:
        st.success("🎉 **정답입니다!** 역함수 공식을 완벽하게 이해했어요.")
    else:
        st.error("❌ **오답입니다.** 다시 한번 공식을 확인하고 풀어보세요.")
        st.markdown("---")
        st.subheader("📝 정답 해설")
        st.markdown(f"""
        주어진 함수 $f(x) = \\frac{{{a}x + {b}}}{{{c}x + {d}}}$ 에 대해
        * **$a = {a}$** 와 **$d = {d}$** 의 위치와 부호를 바꿉니다.
        * 바꾼 값: $-d = {-d}$, $-a = {-a}$
        
        따라서 정답은 다음과 같습니다.
        $$f^{-1}(x) = \\frac{{({inv_a}) x + {inv_b}}}{{{inv_c} x + {inv_d}}}$$
        """)


col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    st.button("✅ 정답 확인", on_click=check_answer)

with col_btn2:
    st.button("🔄 새 문제", on_click=generate_problem)

# 채점 후 정답 해설 표시
if st.session_state.checked:
    # check_answer 함수에서 이미 결과를 표시했으므로 추가 로직은 필요 없음
    pass
