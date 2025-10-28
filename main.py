import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="MBTI 유형별 TOP 10", page_icon="🌍", layout="centered")

st.title("🌎 MBTI 유형별 상위 국가 TOP 10")
st.markdown("CSV 파일을 업로드한 뒤, 특정 MBTI 유형이 높은 국가를 시각적으로 확인하세요.")

# -------------------------------
# 파일 업로드
# -------------------------------
uploaded_file = st.file_uploader("📂 MBTI 데이터 CSV 파일 업로드", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    mbti_types = [c for c in df.columns if c != "Country"]

    st.sidebar.header("⚙️ 설정")
    selected_type = st.sidebar.selectbox("분석할 MBTI 유형 선택", mbti_types, index=0)
    top_n = st.sidebar.slider("표시할 상위 국가 수", 5, 20, 10)

    st.markdown(f"### 🧠 선택한 MBTI 유형: **{selected_type}**")

    # 상위 N개 국가 추출
    top_countries = df.nlargest(top_n, selected_type)[["Country", selected_type]].reset_index(drop=True)
    top_countries[selected_type] = top_countries[selected_type] * 100

    st.subheader(f"📋 {selected_type} 비율이 높은 국가 TOP {top_n}")
    st.dataframe(top_countries.style.format({selected_type: "{:.2f}%"}), use_container_width=True)

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
    )
    st.altair_chart(chart, use_container_width=True)

else:
    st.warning("먼저 CSV 파일을 업로드하세요. 예: `countriesMBTI_16types.csv`")
