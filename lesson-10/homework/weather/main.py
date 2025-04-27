from data_fetcher import DataFetcher

data_fetcher = DataFetcher()

response = data_fetcher.get_weather("Tashkent", "UZ")
json_data = response.json()
print('url: ' + response.url)
print('status_code: ' + str(response.status_code))
print('ok: ' + str(response.ok))
print()
print(f'Location: {json_data['name']}, {json_data['sys']['country']}')
print(f'Description: {str(json_data['weather'][0]['description']).capitalize()}')
print(f'Temperature: {json_data['main']['temp']} °C')
print(f'Feels like: {json_data['main']['feels_like']} °C')
print(f'Humidity: {json_data['main']['humidity']} %')
print(f'Wind: {json_data['wind']['speed']} m/s')
print(f'Cloudiness: {json_data['clouds']['all']} %')
# response.raise_for_status()
