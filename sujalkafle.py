# A simple mock weather app
user_input = input("Enter a city (e.g., London, Tokyo, New York): ").lower()

if user_input == "london":
    print("Weather: 15°C, Rainy 🌧️")
elif user_input == "tokyo":
    print("Weather: 22°C, Sunny ☀️")
elif user_input == "new york":
    print("Weather: 18°C, Cloudy ☁️")
else:
    print(f"Weather data for '{user_input}' is not available right now.")
    
