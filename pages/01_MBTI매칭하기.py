import streamlit as st

# MBTI 특성 데이터 (이모지 추가)
mbti_traits = {
    'INTJ': '🧠 독창적이며 전략적인 사고를 선호합니다. 계획적이고 목표 지향적이며, 비판적 사고가 뛰어납니다.',
    'INFP': '🌟 이상적이고 창의적인 성향을 가지고 있으며, 감정적이고 깊은 내면을 중요시합니다.',
    'ENFP': '🎉 열정적이고 창의적인 성향으로, 다양한 가능성을 탐색하며 사람들과의 소통을 즐깁니다.',
    'ESTJ': '📊 실용적이고 조직적인 성향을 가지며, 체계적이고 효율적인 방식으로 일을 처리합니다.',
    'ISTJ': '📋 신뢰할 수 있고, 실용적이며 세부적인 사항을 중요시합니다. 규칙과 절차를 존중합니다.',
    'INTP': '🔍 호기심이 많고 분석적인 사고를 하며, 문제 해결에 뛰어난 능력을 지닙니다.',
    'INJ': '🌌 깊은 사고와 통찰력을 가지며, 독립적이고 창의적인 문제 해결을 선호합니다.',
    'ENFJ': '🤝 사람들과의 관계를 중시하며, 타인을 이해하고 돕는 데 능숙합니다.',
    'ESFJ': '💖 친근하고 협동적인 성향으로, 타인과의 관계를 중시하며 조직적인 경향이 있습니다.',
    'ISFJ': '🌿 세심하고 책임감이 강하며, 전통을 중시하고 타인을 돕는 데 만족을 느낍니다.',
    'ESTP': '🚀 현실적이고 활동적인 성향을 가지며, 즉흥적인 결정을 잘 내리고 새로운 경험을 추구합니다.',
    'ISTP': '🔧 실용적이고 문제 해결에 뛰어나며, 독립적이고 상황에 맞게 신속히 대응합니다.',
    'ISFP': '🌸 감각적이고 섬세하며, 아름다움을 중시하고 자유로운 삶을 추구합니다.',
    'ESFP': '🎈 활발하고 사교적이며, 새로운 경험을 즐기고 주변 사람들과의 관계를 소중히 여깁니다.',
    'ENTJ': '🚀 목표 지향적이고 전략적이며, 리더십을 발휘하고 효율적인 방식을 선호합니다.',
    'ENTP': '💡 창의적이고 문제 해결에 뛰어나며, 새로운 아이디어와 도전을 즐깁니다.',
}

# MBTI 유형 호환성 (이모지 추가)
compatibility = {
    'INTJ': {'best': 'INFJ', 'worst': 'ESFP'},
    'INFP': {'best': 'ENFJ', 'worst': 'ESTJ'},
    'ENFP': {'best': 'INFJ', 'worst': 'ISTJ'},
    'ESTJ': {'best': 'ISFJ', 'worst': 'INFP'},
    'ISTJ': {'best': 'ESTJ', 'worst': 'ENFP'},
    'INTP': {'best': 'ENTP', 'worst': 'ESFJ'},
    'INJ': {'best': 'INFJ', 'worst': 'ESTP'},
    'ENFJ': {'best': 'INFP', 'worst': 'ISTP'},
    'ESFJ': {'best': 'ISFJ', 'worst': 'INTP'},
    'ISFJ': {'best': 'ESFJ', 'worst': 'ENTP'},
    'ESTP': {'best': 'ISTP', 'worst': 'INFP'},
    'ISTP': {'best': 'ESTP', 'worst': 'ENFJ'},
    'ISFP': {'best': 'ESFP', 'worst': 'ENTJ'},
    'ESFP': {'best': 'ISFP', 'worst': 'INTJ'},
    'ENTJ': {'best': 'INTJ', 'worst': 'ISFP'},
    'ENTP': {'best': 'INTP', 'worst': 'ISFJ'},
}

# Streamlit 앱
def main():
    st.title('MBTI 특성 및 호환성 확인하기 😊')

    # 사용자 이름 입력
    name = st.text_input('이름을 입력해주세요!')

    # MBTI 유형 선택
    mbti_type = st.selectbox('당신의 MBTI 유형을 선택하세요!', list(mbti_traits.keys()))

    if st.button('결과 보기'):
        if name and mbti_type:
            # 특성 표시
            st.write(f"{name}님, **{mbti_type}**의 특성은 다음과 같습니다:")
            st.write(mbti_traits[mbti_type])
            
            # 호환성 추천
            best_match = compatibility[mbti_type]['best']
            worst_match = compatibility[mbti_type]['worst']
            st.write(f"가장 잘 맞는 MBTI 유형: **{best_match}**")
            st.write(f"가장 잘 맞지 않는 MBTI 유형: **{worst_match}**")
        else:
            st.error("이름과 MBTI 유형을 모두 입력해주세요.")

if __name__ == "__main__":
    main()
