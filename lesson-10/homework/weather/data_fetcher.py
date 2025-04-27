import requests


class DataFetcher:
    __api_key = "3e01cbb91550eb1528f5b1c8014334c4"
    __base_url = 'https://api.openweathermap.org/'

    def get_weather(self, city_name: str, country_code: str):
        end_point = 'data/2.5/weather'
        lat_lon = self.get_coord(city_name, country_code)
        api_key = self.__api_key
        params = {'appid': api_key, 'lat': lat_lon[0], 'lon': lat_lon[1], 'units': "metric"}
        response = requests.get(self.__base_url + end_point, params)
        return response

    def get_coord(self, city_name, country_code):
        end_point = 'geo/1.0/direct'
        api_key = self.__api_key
        q = f'{city_name, country_code}'
        params = {'q': q, 'appid': api_key, 'limit': 1}
        response = requests.get(self.__base_url + end_point, params=params)
        city = response.json()[0]
        lat = city['lat']
        lon = city['lon']
        return lat, lon
