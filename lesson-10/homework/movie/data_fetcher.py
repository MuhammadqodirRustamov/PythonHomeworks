import random

import requests

genres_list = [{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 16, 'name': 'Animation'},
               {'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'},
               {'id': 18, 'name': 'Drama'}, {'id': 10751, 'name': 'Family'}, {'id': 14, 'name': 'Fantasy'},
               {'id': 36, 'name': 'History'}, {'id': 27, 'name': 'Horror'}, {'id': 10402, 'name': 'Music'},
               {'id': 9648, 'name': 'Mystery'}, {'id': 10749, 'name': 'Romance'},
               {'id': 878, 'name': 'Science Fiction'}, {'id': 10770, 'name': 'TV Movie'},
               {'id': 53, 'name': 'Thriller'}, {'id': 10752, 'name': 'War'}, {'id': 37, 'name': 'Western'}]


def get_genre_id(genre):
    for genre_dic in genres_list:
        if genre_dic["name"].lower() == str(genre).lower():
            return genre_dic["id"]
    return 0


def get_genre_strings(genre_ids: list):
    genres_string = ""
    for genre_dic in genres_list:
        if genre_dic["id"] in genre_ids:
            genres_string += genre_dic["name"].lower() + ", "
    return genres_string[0:-2].capitalize()


class DataFetcher:
    __base_url = "https://api.themoviedb.org/"
    __api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MGNlOTg4NzBiNzA2ODA1NDkzYjQ5NzE4ZGI5ZmRiMyIsIm5iZiI6MTc0NTY0NDUzNC44MTMsInN1YiI6IjY4MGM2YmY2NWNlZmQxOWQxYzg1ODg0NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LWx3BLz6zwreHYQrxPQF-Hq07JHQqKT_LDcGEB75q_s"

    def get_movies_by_genre(self, genre):
        end_point = "3/discover/movie"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MGNlOTg4NzBiNzA2ODA1NDkzYjQ5NzE4ZGI5ZmRiMyIsIm5iZiI6MTc0NTY0NDUzNC44MTMsInN1YiI6IjY4MGM2YmY2NWNlZmQxOWQxYzg1ODg0NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LWx3BLz6zwreHYQrxPQF-Hq07JHQqKT_LDcGEB75q_s"
        }
        genre_id = get_genre_id(genre)
        params = {'api_key': self.__api_key, "with_genres": genre_id}
        response = requests.get(self.__base_url + end_point, headers=headers, params=params)
        json_data = response.json()
        movies = json_data["results"]
        return movies

    def get_random_movie_by_genre(self, genre):
        movies = self.get_movies_by_genre(genre)
        if len(movies) == 0:
            return None
        random_movie = random.choice(movies)
        return random_movie

