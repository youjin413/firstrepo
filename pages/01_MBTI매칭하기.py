import streamlit as st

# MBTI 특성 데이터 (예시)
mbti_traits = {
    'INTJ': '독창적이며 전략적인 사고를 선호합니다. 계획적이고 목표 지향적이며, 비판적 사고가 뛰어납니다.',
    'INFP': '이상적이고 창의적인 성향을 가지고 있으며, 감정적이고 깊은 내면을 중요시합니다.',
    'ENFP': '열정적이고 창의적인 성향으로, 다양한 가능성을 탐색하며 사람들과의 소통을 즐깁니다.',
    'ESTJ': '실용적이고 조직적인 성향을 가지며, 체계적이고 효율적인 방식으로 일을 처리합니다.',
    'ISTJ': '신뢰할 수 있고, 실용적이며 세부적인 사항을 중요시합니다. 규칙과 절차를 존중합니다.',
    # 다른 MBTI 유형 추가 가능
}

# MBTI 유형 호환성 (예시)
compatibility = {
    'INTJ': {'best': 'INFJ', 'worst': 'ESFP'},
    'INFP': {'best': 'ENFJ', 'worst': 'ESTJ'},
    'ENFP': {'best': 'INFJ', 'worst': 'ISTJ'},
    'ESTJ': {'best': 'ISFJ', 'worst': 'INFP'},
    'ISTJ': {'best': 'ESTJ', 'worst': 'ENFP'},
    # 다른 MBTI 유형 추가 가능
}

# Streamlit 앱
def main():
    st.title('나의 MBTI 특성 및 호환성 확인하기 😊')

    # 사용자 이름 입력
    name = st.text_input('이름을 입력해주세요!')

    # MBTI 유형 입력
    mbti_type = st.text_input('당신의 MBTI 유형을 입력하세요 (예: INTJ, INFP, ENFP, ESTJ, ISTJ)')

    if st.button('결과 보기'):
        if name and mbti_type:
            mbti_type = mbti_type.upper()

            # MBTI 유형이 유효한지 확인
            if mbti_type in mbti_traits:
                # 특성 표시
                st.write(f"{name}님, **{mbti_type}**의 특성은 다음과 같습니다:")
                st.write(mbti_traits[mbti_type])
                
                # 호환성 추천
                best_match = compatibility[mbti_type]['best']
                worst_match = compatibility[mbti_type]['worst']
                st.write(f"가장 잘 맞는 MBTI 유형: **{best_match}**")
                st.write(f"가장 잘 맞지 않는 MBTI 유형: **{worst_match}**")
            else:
                st.error("유효하지 않은 MBTI 유형입니다. 올바른 유형을 입력하세요.")
        else:
            st.error("이름과 MBTI 유형을 모두 입력해주세요.")

if __name__ == "__main__":
    main()
