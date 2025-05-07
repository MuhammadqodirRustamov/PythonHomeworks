from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as file:
    html_content = file.read()

weather_list = []

soup = BeautifulSoup(html_content, "html.parser")
table_body = soup.find("tbody")
table_rows = table_body.find_all("tr")

for row in table_rows:
    data = row.find_all("td")
    day = [data[0].text, data[1].text, data[2].text]
    weather_list.append(day)

for day_weather in weather_list:
    print(str(day_weather[0]).ljust(9) + "  " + day_weather[1] + "   " + day_weather[2])

temperatures = [int(str(day_weather[1])[:-2]) for day_weather in weather_list]
max_temp = max(temperatures)
avg = sum(temperatures)/len(temperatures)

print()
print(f"Hottest day(s) ({max_temp}°C): ", end="")

hottest_days_string = ""
for day_weather in weather_list:
    if int(str(day_weather[1])[:-2]) == max_temp:
        hottest_days_string += ", " + day_weather[0]
hottest_days_string = hottest_days_string[2:]
print(hottest_days_string)
print(f"Weekly average: {round(avg, 1)}°C")