import pandas as pd
import random

# 실제 영화 리스트 (장르별 일부 예시)
movies = {
    "Action": [
        "Inception", "The Dark Knight", "Mad Max: Fury Road", "John Wick", "Gladiator",
        "Die Hard", "The Avengers", "Black Panther", "The Batman", "Top Gun: Maverick",
        "Mission: Impossible – Fallout", "Skyfall", "The Matrix", "Avengers: Endgame",
        "The Bourne Ultimatum", "Iron Man", "Spider-Man: No Way Home", "Logan", "300", "Fast & Furious 7"
    ],
    "Comedy": [
        "The Hangover", "Superbad", "Mean Girls", "21 Jump Street", "Crazy Rich Asians",
        "Home Alone", "Zombieland", "The Mask", "Pitch Perfect", "Bridesmaids",
        "Step Brothers", "Juno", "Ghostbusters", "Borat", "The Intern",
        "Ted", "Mrs. Doubtfire", "The 40-Year-Old Virgin", "Rush Hour", "Anchorman"
    ],
    "Drama": [
        "Forrest Gump", "The Shawshank Redemption", "Fight Club", "The Godfather", "Titanic",
        "The Green Mile", "Whiplash", "A Beautiful Mind", "Good Will Hunting", "Joker",
        "Parasite", "12 Years a Slave", "The Pursuit of Happyness", "The Revenant", "American Beauty",
        "The Social Network", "The Pianist", "Spotlight", "Marriage Story", "The Wolf of Wall Street"
    ],
    "Sci-Fi": [
        "Interstellar", "Avatar", "Blade Runner 2049", "Ex Machina", "The Martian",
        "Dune", "Arrival", "Jurassic Park", "Edge of Tomorrow", "Minority Report",
        "E.T.", "Ready Player One", "The Fifth Element", "I, Robot", "The Matrix Reloaded",
        "Star Wars: A New Hope", "Star Wars: The Empire Strikes Back", "The Terminator", "Rogue One", "A.I. Artificial Intelligence"
    ],
    "Romance": [
        "La La Land", "The Notebook", "Pride and Prejudice", "About Time", "Notting Hill",
        "Love Actually", "Before Sunrise", "Titanic", "Pretty Woman", "Crazy Stupid Love",
        "500 Days of Summer", "Me Before You", "The Fault in Our Stars", "The Holiday", "Begin Again",
        "A Star Is Born", "To All the Boys I've Loved Before", "Dear John", "The Proposal", "Call Me by Your Name"
    ],
    "Thriller": [
        "Se7en", "Gone Girl", "Prisoners", "The Silence of the Lambs", "Shutter Island",
        "Memento", "The Girl with the Dragon Tattoo", "Zodiac", "Nightcrawler", "The Prestige",
        "Split", "The Sixth Sense", "Oldboy", "No Country for Old Men", "Enemy",
        "Get Out", "Black Swan", "Fight Club", "The Departed", "Tenet"
    ],
    "Horror": [
        "The Conjuring", "It", "A Quiet Place", "Hereditary", "The Exorcist",
        "The Ring", "The Babadook", "Annabelle", "Insidious", "The Blair Witch Project",
        "Scream", "Us", "Sinister", "Midsommar", "The Shining",
        "Paranormal Activity", "Saw", "Carrie", "Get Out", "Texas Chainsaw Massacre"
    ],
    "Animation": [
        "Toy Story", "Finding Nemo", "The Lion King", "Shrek", "Up",
        "Inside Out", "Coco", "Frozen", "Zootopia", "Moana",
        "How to Train Your Dragon", "The Incredibles", "Encanto", "Spirited Away", "Monsters, Inc.",
        "Kung Fu Panda", "Ratatouille", "Despicable Me", "Big Hero 6", "Soul"
    ],
    "Adventure": [
        "Indiana Jones", "Pirates of the Caribbean", "Jurassic World", "King Kong", "The Jungle Book",
        "The Lord of the Rings: The Fellowship of the Ring", "The Hobbit", "National Treasure", "Life of Pi", "Avatar: The Way of Water",
        "Jumanji", "The Mummy", "The Lost City", "The Goonies", "Uncharted",
        "Cast Away", "The Revenant", "Into the Wild", "The Secret Life of Walter Mitty", "The Hunger Games"
    ],
    "Fantasy": [
        "Harry Potter and the Sorcerer’s Stone", "The Lord of the Rings: The Return of the King", "Pan’s Labyrinth", "Doctor Strange", "The Shape of Water",
        "Alice in Wonderland", "Fantastic Beasts", "Maleficent", "Enchanted", "The Chronicles of Narnia",
        "Hocus Pocus", "The Golden Compass", "Percy Jackson & the Olympians", "Eragon", "Beasts of the Southern Wild",
        "Stardust", "The Witcher", "Willow", "The NeverEnding Story", "Peter Pan"
    ]
}

# 데이터프레임 생성
records = []
for genre, titles in movies.items():
    for title in titles:
        records.append({
            "Title": title,
            "Genre": genre,
            "Rating": round(random.uniform(3.0, 5.0), 1),
            "Reviews": random.randint(200, 20000)
        })

df = pd.DataFrame(records)
df.to_csv("movie_ratings_real.csv", index=False)
print("✅ 'movie_ratings_real.csv' 생성 완료!")
