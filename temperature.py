def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Example usage
fahrenheit = 98.6
celsius = 37
print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F")
