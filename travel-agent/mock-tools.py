def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.
    
    Args:
        city (str): The name of the city (e.g., "New York", "London", "Tokyo").
    
    Returns:
        dict: A dictionary containing the weather information.
              Includes a 'status' key ('success' or 'error').
              If 'success', includes a 'report' key with weather details.
              If 'error', includes an 'error_message' key.
    """
    print(f"Tool: get_weather called for city: {city}")
    
    # Mock weather data
    mock_weather_db = {
        "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
        "london": {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
        "tokyo": {"status": "success", "report": "Tokyo is experiencing light rain and a temperature of 18°C."},
    }
    
    city_normalized = city.lower().replace(" ", "")
    
    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}

# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Retrieves the current time in a specified city.
    
    Args:
        city (str): The name of the city (e.g., "New York", "London", "Tokyo").
    
    Returns:
        dict: A dictionary containing the time information.
              Includes a 'status' key ('success' or 'error').
              If 'success', includes a 'time' key with time details.
              If 'error', includes an 'error_message' key.
    """
    print(f"Tool: get_current_time called for city: {city}")
    
    # Mock weather data
    mock_time_db = {
        "newyork": "10:30 AM",
        "london": "11:30 AM",
        "tokyo": "12:30 AM",
    }
    
    city_normalized = city.lower().replace(" ", "")
    
    if city_normalized in mock_time_db:
        return {"status": "success", "city": city, "time": mock_time_db[city_normalized]}
    else:
        return {"status": "error", "error_message": f"Sorry, I don't have time information for '{city}'."}
