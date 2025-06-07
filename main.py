import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

# --- 앱 제목 및 설명 ---
st.title("📚 MBTI 유형별 국어 과목 성취도 분석")
st.write("각 MBTI 유형의 국어 과목 성취도를 가상의 데이터로 확인해보세요! 스크롤하여 유형을 선택할 수 있습니다.")

# --- 가상의 데이터 생성 (실제 데이터가 있다면 교체해주세요) ---
# MBTI 유형 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 각 MBTI 유형별 국어 성취도 가상 데이터 (0-100점)
data = {
    "MBTI 유형": mbti_types,
    "국어 성취도 (점)": [
        85, 90, 92, 88, 78, 82, 95, 91,
        75, 70, 89, 87, 80, 83, 93, 86
    ],
    "성취 등급": [
        "우수", "매우 우수", "매우 우수", "우수", "보통", "양호", "최우수", "매우 우수",
        "보통", "미흡", "우수", "우수", "양호", "양호", "매우 우수", "우수"
    ]
}
df = pd.DataFrame(data)

# --- MBTI 유형 선택 (스크롤) ---
st.sidebar.header("🔍 MBTI 유형 선택")
selected_mbti = st.sidebar.selectbox("보고 싶은 MBTI 유형을 선택하세요:", mbti_types)

# --- 결과 표시 ---
st.markdown("---")
st.header(f"📊 선택한 MBTI 유형: **{selected_mbti}** 의 국어 성취도")

# 선택된 MBTI 유형의 데이터 필터링
filtered_data = df[df["MBTI 유형"] == selected_mbti]

if not filtered_data.empty:
    st.dataframe(filtered_data.set_index("MBTI 유형"))
    
    st.markdown(f"**{selected_mbti}** 유형의 국어 점수는 **{filtered_data['국어 성취도 (점)'].iloc[0]}점** 이고, 성취 등급은 **{filtered_data['성취 등급'].iloc[0]}** 입니다. 🎉")
else:
    st.write("데이터를 찾을 수 없습니다. 다시 선택해주세요.")

st.markdown("---")
st.write("※ 이 데이터는 예시를 위한 **가상의 데이터**입니다. 실제 통계와는 다를 수 있습니다.")

# ... (기존 코드) ...

if not filtered_data.empty:
    st.dataframe(filtered_data.set_index("MBTI 유형"))
    st.markdown(f"**{selected_mbti}** 유형의 국어 점수는 **{filtered_data['국어 성취도 (점)'].iloc[0]}점** 이고, 성취 등급은 **{filtered_data['성취 등급'].iloc[0]}** 입니다. 🎉")

    st.subheader(f"💡 {selected_mbti} 유형의 학습 특성 (가설적 설명)")
    # 여기에 해당 MBTI 유형에 대한 설명을 조건문으로 추가합니다.
    if selected_mbti == "ISTJ":
        st.write("ISTJ는 꼼꼼하고 규칙을 중시하며, 사실과 세부사항에 강합니다. 국어 과목에서는 문법, 어휘, 독해 지문 분석 등 정확성을 요구하는 부분에서 높은 성취를 보일 수 있습니다.")
    elif selected_mbti == "INFP":
        st.write("INFP는 창의적이고 이상주의적이며, 개인적인 가치를 중시합니다. 문학 작품의 메시지나 작가의 의도를 깊이 공감하고 이해하는 데 강점을 보이며, 자기 생각을 글로 표현하는 데 뛰어날 수 있습니다.")
    # ... 모든 MBTI 유형에 대해 위와 같이 추가 ...

else:
    st.write("데이터를 찾을 수 없습니다. 다시 선택해주세요.")

st.markdown("---")
st.write("※ 이 데이터는 예시를 위한 **가상의 데이터**이며, MBTI 유형과 학업 성취도 사이에는 **과학적으로 입증된 직접적인 인과관계가 없습니다.** 위에 제시된 설명은 각 유형의 **일반적인 학습 특성**을 바탕으로 한 **가설적인 추론**임을 유의해주세요.")
