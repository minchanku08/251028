import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="🎬 영화 평점 데이터 분석", page_icon="🎥", layout="centered")

st.title("🎬 실제 영화 기반 평점 분석 대시보드 (경량 버전)")
st.markdown("""
이 웹앱은 **실제 영화 제목**을 사용한 가상 평점 데이터를 분석합니다.  
Streamlit Cloud에서도 **빠르게 실행되도록 최적화**된 버전입니다.
""")

uploaded = st.file_uploader("📂 CSV 파일 업로드 (movie_ratings_small.csv)", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv("movie_ratings_small.csv")

# 데이터 미리보기
st.subheader("🔎 데이터 미리보기")
st.dataframe(df.head(), use_container_width=True)

# 장르 선택
genres = sorted(df["Genre"].unique())
selected_genre = st.selectbox("🎭 장르 선택", genres)
top_n = st.slider("표시할 영화 수", 3, 10, 5)

# 장르별 평균 평점
st.markdown("## ⭐ 장르별 평균 평점")
avg_rating = df.groupby("Genre")["Rating"].mean().reset_index().sort_values("Rating", ascending=False)

chart1 = (
    alt.Chart(avg_rating)
    .mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5)
    .encode(
        x=alt.X("Rating:Q", title="평균 평점"),
        y=alt.Y("Genre:N", sort="-x", title="장르"),
        color=alt.Color("Rating:Q", scale=alt.Scale(scheme="blues")),
        tooltip=["Genre", "Rating"]
    )
    .properties(width=700, height=400)
)
st.altair_chart(chart1, use_container_width=True)

# 선택된 장르의 상위 영화 표시
st.markdown(f"## 🎥 {selected_genre} 장르의 인기 영화 TOP {top_n}")
filtered = df[df["Genre"] == selected_genre].sort_values("Rating", ascending=False).head(top_n)
st.dataframe(filtered, use_container_width=True)

chart2 = (
    alt.Chart(filtered)
    .mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5)
    .encode(
        x=alt.X("Rating:Q", title="평점"),
        y=alt.Y("Title:N", sort="-x", title="영화 제목"),
        color=alt.Color("Rating:Q", scale=alt.Scale(scheme="orangered")),
        tooltip=["Title", "Rating", "Reviews"]
    )
    .properties(width=700, height=350)
)
st.altair_chart(chart2, use_container_width=True)

st.markdown("---")
st.caption("© 2025 데이터과학·머신러닝 수행평가 예시 — 실제 영화 기반 경량 버전 🎓")
