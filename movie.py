import pandas as pd
movie_data = pd.read_csv("movies.csv")

def get_genre(movie_name):
    for index, row in movie_data.iterrows():
        if row['title'].strip().lower() == movie_name.strip().lower():
            return row['genres']
    return None

def recmovies(genre):
    recommendations = []
    if genre:
        target_genres = [g.strip().lower() for g in genre.split('|')]
        for index, row in movie_data.iterrows():
            movie_genres = [g.strip().lower() for g in str(row['genres']).split('|')]
            if any(g in movie_genres for g in target_genres):
                recommendations.append(row['title'])
    return recommendations

movie_name = input("Enter the movie name: ")
genre = get_genre(movie_name)

if genre:
    print(f"The genre of {movie_name} is: {genre}")
    recommended = recmovies(genre)
    if recommended:
        print("\nMovies you may also like:")
        for movie in recommended:
            print(f"- {movie}")
    else:
        print("No similar movies found.")
else:
    print(f"Movie '{movie_name}' not found in the database.")