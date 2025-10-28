import streamlit as st
import pandas as pd
import altair as alt
import random

# ----------------------------------
# 🌟 기본 페이지 설정
# ----------------------------------
st.set_page_config(
    page_title="🎬 영화 평점 데이터 분석",
    page_icon="🎥",
    layout="centered"
)

# ----------------------------------
# 🏷️ 제목 및 소개
# ----------------------------------
st.title("🎬 영화 평점 데이터 분석 대시보드")
st.markdown("""
이 웹앱은 가상의 영화 평점 데이터를 분석하여  
**장르별 평균 평점**과 **개별 영화 순위**를 시각적으로 보여줍니다.  

> Streamlit + Altair 기반으로 제작되었으며,  
> **추가 라이브러리 설치 없이** Streamlit Cloud에서 바로 실행 가능합니다.
""")

# ----------------------------------
# ⚙️ CSV 업로드 or 자동 생성
# ----------------------------------
st.sidebar.header("⚙️ 설정")
uploaded_file = st.sidebar.file_uploader("CSV 파일 업로드 (선택)", type=["csv"])

def create_sample_data():
    """기본 예시 데이터 자동 생성"""
    genres = ["Action", "Comedy", "Drama", "Sci-Fi", "Horror", "Romance", 
              "Thriller", "Animation", "Adventure", "Fantasy"]
    titles = [f"Movie {i}" for i in range(1, 201)]

    data = {
        "Title": titles,
        "Genre": [random.choice(genres) for _ in range(200)],
        "Rating": [round(random.uniform(2.5, 5.0), 1) for _ in range(200)],
        "Reviews": [random.randint(100, 5000) for _ in range(200)]
    }

    return pd.DataFrame(data)

# 파일 로드
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ 업로드한 CSV 파일이 성공적으로 로드되었습니다!")
else:
    df = create_sample_data()
    st.info("💡 업로드된 파일이 없어, 기본 예시 데이터가 자동 생성되었습니다.")

# ----------------------------------
# 🔍 데이터 미리보기
# ----------------------------------
st.subheader("🔎 데이터 미리보기")
st.dataframe(df.head(), use_container_width=True)

# ----------------------------------
# 🎭 장르 선택
# ----------------------------------
genres = sorted(df["Genre"].unique())
selected_genre = st.sidebar.selectbox("🎭 분석할 장르 선택", genres, index=0)
top_n = st.sidebar.slider("표시할 영화 수", 5, 20, 10)

# ----------------------------------
# 📊 장르별 평균 평점 TOP 10
# ----------------------------------
st.markdown("## ⭐ 장르별 평균 평점 TOP 10")

avg_rating = (
    df.groupby("Genre")["Rating"]
    .mean()
    .reset_index()
    .sort_values("Rating", ascending=False)
)

chart1 = (
    alt.Chart(avg_rating.head(10))
    .mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
    .encode(
        x=alt.X("Rating:Q", title="평균 평점"),
        y=alt.Y("Genre:N", sort="-x", title="장르"),
        color=alt.Color("Rating:Q", scale=alt.Scale(scheme="tealblues"), legend=None),
        tooltip=[alt.Tooltip("Genre:N", title="장르"),
                 alt.Tooltip("Rating:Q", format=".2f", title="평균 평점")],
    )
    .properties(width=700, height=400, title="🎞️ 장르별 평균 평점 비교")
)
st.altair_chart(chart1, use_container_width=True)

# ----------------------------------
# 🎥 선택한 장르의 영화 순위
# ----------------------------------
st.markdown(f"## 🎥 '{selected_genre}' 장르 영화 TOP {top_n}")

filtered = (
    df[df["Genre"] == selected_genre]
    .sort_values("Rating", ascending=False)
    .head(top_n)
)

st.dataframe(filtered, use_container_width=True)

chart2 = (
    alt.Chart(filtered)
    .mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5)
    .encode(
        x=alt.X("Rating:Q", title="영화 평점"),
        y=alt.Y("Title:N", sort="-x", title="영화 제목"),
        color=alt.Color("Rating:Q", scale=alt.Scale(scheme="orangered"), legend=None),
        tooltip=["Title", "Rating", "Reviews"]
    )
    .properties(width=700, height=400, title=f"🎬 {selected_genre} 장르 영화 평점 순위")
)
st.altair_chart(chart2, use_container_width=True)

# ----------------------------------
# 📘 프로젝트 설명
# ----------------------------------
st.markdown("---")
with st.expander("ℹ️ 프로젝트 설명"):
    st.markdown("""
    **프로젝트 주제:** 영화 평점 데이터 기반 장르별 인기 분석  
    **사용 기술:** Python, Streamlit, Pandas, Altair  
    **핵심 기능:**  
    - 장르별 평균 평점 시각화  
    - 선택 장르별 영화 순위 그래프  
    - 자동 데이터 생성 기능으로 Cloud에서도 즉시 실행 가능  

    **💡 세특 포인트:**  
    데이터 시각화 도구를 활용하여 영화 데이터의 패턴을 분석하고,  
    변수 간 관계를 시각적으로 해석하는 능력을 보여줌.  
    Streamlit을 이용해 데이터 분석 결과를 웹 환경에서 공유함으로써  
    인공지능 및 데이터 과학적 사고 역량을 강화함.
    """)

st.caption("© 2025 데이터과학·머신러닝 수행평가 예시 — by AI 도우미 🎓")




   
