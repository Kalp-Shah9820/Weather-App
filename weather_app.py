import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "7f0e65891b935181fd877eb110062e16",
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Check if the response contains valid weather data
        if data["cod"] != 200:
            return None
        
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"].title(),
            "city": data["name"]
        }
        
    except requests.exceptions.RequestException:
        return None
    except (KeyError, json.JSONDecodeError):
        return None

def display_weather(weather_data):
    if not weather_data:
        print("\n❌ Error: City not found or invalid input!")
        return
    
    print(f"\n🌤️ Weather in {weather_data['city']}:")
    print(f"  🌡 Temperature: {weather_data['temperature']}°C")
    print(f"  💧 Humidity: {weather_data['humidity']}%")
    print(f"  🌬 Wind Speed: {weather_data['wind_speed']} m/s")
    print(f"  ☁️ Conditions: {weather_data['description']}")

def main():
    API_KEY = "7f0e65891b935181fd877eb110062e16"  # Replace with your OpenWeatherMap API key
    
    print("🌍 Weather App 🌞")
    print("------------------")
    
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        
        if city.lower() == "quit":
            print("\n👋 Goodbye!")
            break
            
        if not city:
            print("❌ Please enter a valid city name!")
            continue
            
        weather_data = get_weather(API_KEY, city)
        display_weather(weather_data)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
