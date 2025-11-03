import streamlit as st
import pandas as pd
import altair as alt
import random


st.set_page_config(page_title="🎬 영화 평점 데이터 분석", page_icon="🎥", layout="centered")

st.title("🎬 실제 영화 기반 평점 분석 대시보드 (자동 데이터 생성)")
st.markdown("""
이 앱은 **실제 영화 이름**을 기반으로 생성된 가상 평점 데이터를 분석합니다.  
Streamlit Cloud에서도 **파일 업로드 없이 바로 작동**하도록 설계되었습니다.  
""")


def create_movie_data():
    movies = {
        "Action": [
            "Inception", "The Dark Knight", "John Wick", "Gladiator", "The Matrix",
            "Black Panther", "Avengers: Endgame", "Top Gun: Maverick"
        ],
        "Comedy": [
            "The Hangover", "Superbad", "Mean Girls", "Home Alone", "Zombieland",
            "Crazy Rich Asians", "21 Jump Street", "Bridesmaids"
        ],
        "Drama": [
            "Forrest Gump", "The Shawshank Redemption", "Fight Club", "The Godfather",
            "Whiplash", "Parasite", "The Green Mile", "The Social Network"
        ],
        "Sci-Fi": [
            "Interstellar", "Avatar", "The Martian", "Blade Runner 2049",
            "Dune", "Arrival", "Jurassic Park", "The Terminator"
        ],
        "Romance": [
            "La La Land", "The Notebook", "Pride and Prejudice", "About Time",
            "Before Sunrise", "Pretty Woman", "Love Actually", "A Star Is Born"
        ],
        "Thriller": [
            "Se7en", "Gone Girl", "Prisoners", "The Silence of the Lambs",
            "Shutter Island", "Memento", "Get Out", "The Prestige"
        ],
        "Horror": [
            "The Conjuring", "It", "A Quiet Place", "Hereditary",
            "The Exorcist", "The Shining", "Us", "The Ring"
        ],
        "Animation": [
            "Toy Story", "Finding Nemo", "The Lion King", "Frozen",
            "Up", "Coco", "Inside Out", "Zootopia"
        ],
        "Adventure": [
            "Indiana Jones", "Pirates of the Caribbean", "The Hobbit",
            "The Lord of the Rings", "Jurassic World", "Jumanji", "National Treasure", "The Revenant"
        ],
        "Fantasy": [
            "Harry Potter", "Doctor Strange", "The Shape of Water",
            "Fantastic Beasts", "Maleficent", "Pan’s Labyrinth", "Narnia", "Stardust"
        ]
    }

    records = []
    for genre, titles in movies.items():
        for title in titles:
            records.append({
                "Title": title,
                "Genre": genre,
                "Rating": round(random.uniform(3.0, 5.0), 1),
                "Reviews": random.randint(500, 15000)
            })
    return pd.DataFrame(records)


uploaded = st.file_uploader("📂 CSV 파일 업로드 (선택사항)", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.success("✅ 업로드한 CSV 파일이 로드되었습니다!")
else:
    df = create_movie_data()
    st.info("💡 CSV가 업로드되지 않아 자동으로 샘플 데이터가 생성되었습니다.")


st.subheader("🔎 데이터 미리보기")
st.dataframe(df.head(), use_container_width=True)


genres = sorted(df["Genre"].unique())
selected_genre = st.selectbox("🎭 장르 선택", genres)
top_n = st.slider("표시할 영화 수", 3, 10, 5)


st.markdown("## ⭐ 장르별 평균 평점")

avg_rating = df.groupby("Genre")["Rating"].mean().reset_index().sort_values("Rating", ascending=False)

chart1 = (
    alt.Chart(avg_rating)
    .mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5)
    .encode(
        x=alt.X("Rating:Q", title="평균 평점"),
        y=alt.Y("Genre:N", sort="-x", title="장르"),
        color=alt.Color("Rating:Q", scale=alt.Scale(scheme="tealblues")),
        tooltip=["Genre", "Rating"]
    )
    .properties(width=700, height=400, title="🎞️ 장르별 평균 평점 비교")
)
st.altair_chart(chart1, use_container_width=True)


st.markdown(f"## 🎥 {selected_genre} 장르의 인기 영화 TOP {top_n}")

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
        x=alt.X("Rating:Q", title="평점"),
        y=alt.Y("Title:N", sort="-x", title="영화 제목"),
        color=alt.Color("Rating:Q", scale=alt.Scale(scheme="orangered")),
        tooltip=["Title", "Rating", "Reviews"]
    )
    .properties(width=700, height=350, title=f"🎬 {selected_genre} 장르 영화 평점 순위")
)
st.altair_chart(chart2, use_container_width=True)


st.markdown("---")
with st.expander("ℹ️ 프로젝트 설명"):
    st.markdown("""
   
st.caption("© 2025 데이터과학·머신러닝 수행평가 예시 — 자동 실행형 Streamlit 앱 🎓")
