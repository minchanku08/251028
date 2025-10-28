import streamlit as st
import pandas as pd
import altair as alt

# -------------------------------
# 기본 설정
# -------------------------------
st.set_page_config(
    page_title="MBTI 유형별 상위 국가 TOP 10",
    page_icon="🌎",
    layout="centered"
)

st.title("🌍 MBTI 유형별 상위 국가 TOP 10 대시보드")
st.markdown("""
이 대시보드는 국가별 MBTI 유형 분포 데이터를 이용해  
**특정 MBTI 유형이 높은 국가 TOP 10**을 시각적으로 보여줍니다.  
데이터는 각 나라의 16가지 MBTI 유형 비율로 구성되어 있습니다.
""")

# -------------------------------
# 데이터 불러오기
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# MBTI 유형 컬럼 식별
mbti_types = [c for c in df.columns if c != "Country"]

# -------------------------------
# 사용자 입력
# -------------------------------
st.sidebar.header("⚙️ 설정")
selected_type = st.sidebar.selectbox("분석할 MBTI 유형 선택", mbti_types, index=0)
top_n = st.sidebar.slider("표시할 상위 국가 수", 5, 20, 10)

st.markdown(f"### 🧠 선택한 MBTI 유형: **{selected_type}**")
st.markdown("이 유형의 비율이 높은 국가 순위를 보여줍니다.")

# -------------------------------
# 데이터 처리
# -------------------------------
top_countries = df.nlargest(top_n, selected_type)[["Country", selected_type]].reset_index(drop=True)
top_countries[selected_type] = top_countries[selected_type] * 100  # 비율 → %

# -------------------------------
# 표시 (테이블)
# -------------------------------
st.subheader(f"📋 {selected_type} 비율이 높은 국가 TOP {top_n}")
st.dataframe(
    top_countries.style.format({selected_type: "{:.2f}%"}),
    use_container_width=True
)

# -------------------------------
# 시각화 (Altair)
# -------------------------------
st.subheader("📊 시각화")

chart = (
    alt.Chart(top_countries)
    .mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8)
    .encode(
        x=alt.X(f"{selected_type}:Q", title=f"{selected_type} 비율 (%)"),
        y=alt.Y("Country:N", sort="-x", title="국가"),
        color=alt.Color(f"{selected_type}:Q", scale=alt.Scale(scheme="tealblues"), legend=None),
        tooltip=["Country", alt.Tooltip(f"{selected_type}:Q", format=".2f")]
    )
    .properties(width=700, height=400)
    .configure_axis(labelFontSize=12, titleFontSize=13)
)

st.altair_chart(chart, use_container_width=True)

# -------------------------------
# 추가 정보
# -------------------------------
with st.expander("ℹ️ 참고 및 사용 방법"):
    st.markdown("""
    - 왼쪽 사이드바에서 MBTI 유형과 표시할 국가 수를 선택하세요.  
    - 그래프 색은 비율에 따라 자동으로 변합니다.  
    - 데이터는 국가별 16가지 MBTI 유형 비율을 사용합니다.  
    - 필요 시 파일을 교체하면 자동으로 새로운 결과가 반영됩니다.
    """)

st.markdown("---")
st.caption("© 2025 MBTI 데이터 시각화 데모 • Altair + Streamlit")
