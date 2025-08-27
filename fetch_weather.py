import requests
from config import API_KEY

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        raise Exception(f"Error fetching weather data: {data.get('message', 'Unknown error')}")

    return  {   
        'city': data['name'],
        'temperature': data['main']['temp'],
        'weather': data['weather'][0]['description']
    }
        

if __name__ == "__main__":
    city = input("Enter the city name: ")
    weather_data = fetch_weather(city)
    print(weather_data)
