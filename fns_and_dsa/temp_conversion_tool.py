FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


if __name__ == "__main__":
    try:
        temperature = float(input("Enter the temperature to convert: "))
        type_t = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    
        temperature = float(temperature)            
        if type_t == "F":
            print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
        elif type_t == "C":
            print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
        else:
            print("Invalid unit. Please enter a numeric value.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")