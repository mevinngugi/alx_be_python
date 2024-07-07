FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to celsius"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return f"{fahrenheit}°F is {celsius}°C"

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return f"{celsius}°C is {fahrenheit}°F"

temp = int(input("Enter the temperature to convert: "))
celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if celsius_or_fahrenheit.upper() == "F":
    print(convert_to_celsius(temp))
elif celsius_or_fahrenheit.upper() == "C":
    print(convert_to_fahrenheit(temp))
