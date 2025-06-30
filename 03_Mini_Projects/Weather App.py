import requests

API_KEY = "7c280f4a80b04481b28115001252806"  # Replace with your real key
BASE_URL = "https://api.weatherapi.com/v1/current.json"

city = input("Enter city name: ")

# 🌐 Build the full URL
url = f"{BASE_URL}?key={API_KEY}&q={city}"

# 🔁 Send GET request
response = requests.get(url)

# ✅ If request is successful
if response.status_code == 200:
    data = response.json()

    location = data['location']['name']
    country = data['location']['country']
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']
    humidity = data['current']['humidity']
    wind_kph = data['current']['wind_kph']
    feels_like = data['current']['feelslike_c']

    print(f"\n🌍 Weather in {location}, {country}:")
    print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
    print(f"📝 Condition: {condition}")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_kph} km/h")
else:
    print("❌ Failed to get weather data. Please check city name or API key.")
