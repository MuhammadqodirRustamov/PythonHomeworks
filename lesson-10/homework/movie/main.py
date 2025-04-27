from data_fetcher import DataFetcher
from data_fetcher import get_genre_strings
import textwrap

data_fetcher = DataFetcher()
while True:
    genre = input("Enter movie genre: ")
    print()
    random_movie_by_genre = data_fetcher.get_random_movie_by_genre(genre)
    if random_movie_by_genre is None:
        print("Incorrect entry")
        print()
        continue
    print(f'Movie: {random_movie_by_genre["title"]} ({random_movie_by_genre['release_date'][:4]})' )
    print("Rating: " + f'{round(random_movie_by_genre["vote_average"], 1)} ({random_movie_by_genre['vote_count']} votes)')
    print("Original language: " + f'{str(random_movie_by_genre["original_language"]).capitalize()}')
    print(f"Genres: {get_genre_strings(random_movie_by_genre["genre_ids"])}")
    print(f'Overview: {textwrap.fill(random_movie_by_genre["overview"], width=50, subsequent_indent="          ")}')
    print()
