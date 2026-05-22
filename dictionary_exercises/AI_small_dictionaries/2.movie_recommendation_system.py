"""Store movies and genres.

movies = {
    "Inception": "Sci-Fi",
    "Titanic": "Romance",
    "Interstellar": "Sci-Fi"
}

Requirements:
- Ask user for favorite genre
- Loop through dictionary
- Recommend matching movies
"""

movies = {
    "Inception": "Sci-Fi",
    "Titanic": "Romance",
    "Interstellar": "Sci-Fi"
}
def movie_recommendation():
    favourite_genre = input("whats your favourite genre: ")
    
   
    for movie,genre in movies.items():
        if genre == favourite_genre:
            print(f"we recommend this movie {movie} ")
     
        
movie_recommendation()
        
        
    