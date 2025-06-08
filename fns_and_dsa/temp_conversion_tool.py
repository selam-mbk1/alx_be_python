# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using a global conversion factor.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Formula: (Fahrenheit - 32) * 5/9
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using a global conversion factor.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Formula: (Celsius * 9/5) + 32
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to handle user interaction for temperature conversion.
    """
    while True:
        try:
            # Prompt the user for the temperature
            temp_str = input("Enter the temperature to convert: ")
            temperature = float(temp_str) # Convert input to a float

            # Prompt the user for the unit
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp}°C")
            elif unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp}°F")
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            break # Exit loop after successful conversion
        except ValueError:
            # Handle non-numeric input for temperature
            print("Invalid temperature. Please enter a numeric value.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
