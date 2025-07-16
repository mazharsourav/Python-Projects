def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254
    }

    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Invalid units for length conversion.")

    value_in_meters = value * length_units[from_unit]
    return value_in_meters / length_units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        raise ValueError("Invalid units for temperature conversion.")


def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'kg': 1,
        'grams': 1000,
        'pounds': 2.20462,
        'ounces': 35.274
    }

    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Invalid units for weight conversion.")
    

    value_in_kg = value * weight_units[from_unit]
    return value_in_kg / weight_units[to_unit]


def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'liters': 1,
        'milliliters': 1000,
        'gallons': 3.78541,
        'cubic_meters': 1000
    }

    if from_unit not in volume_units or to_unit not in volume_units:
        raise ValueError("Invalid units for volume conversion.")
    

    value_in_liters = value * volume_units[from_unit]
    return value_in_liters / volume_units[to_unit]


def main():
    print("Welcome to the Unit Converter!")

    while True:
        print("\nSelect the type of conversion:")
        print("1. Length")
        print("2. Temperature")
        print("3. Weight")
        print("4. Volume")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1/2/3/4/5): "))

            if choice == 5:
                print("Thank you for using the Unit Converter! Goodbye!")
                break
            

            value = float(input("Enter the value to convert: "))

            if choice == 1:  
                print("\nAvailable units: meters, kilometers, miles, feet, inches")
                from_unit = input("Enter the from unit: ").lower()
                to_unit = input("Enter the to unit: ").lower()
                result = convert_length(value, from_unit, to_unit)
                print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

            elif choice == 2: 
                print("\nAvailable units: Celsius, Fahrenheit, Kelvin")
                from_unit = input("Enter the from unit: ").capitalize()
                to_unit = input("Enter the to unit: ").capitalize()
                result = convert_temperature(value, from_unit, to_unit)
                print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

            elif choice == 3: 
                print("\nAvailable units: kg, grams, pounds, ounces")
                from_unit = input("Enter the from unit: ").lower()
                to_unit = input("Enter the to unit: ").lower()
                result = convert_weight(value, from_unit, to_unit)
                print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

            elif choice == 4:  
                print("\nAvailable units: liters, milliliters, gallons, cubic_meters")
                from_unit = input("Enter the from unit: ").lower()
                to_unit = input("Enter the to unit: ").lower()
                result = convert_volume(value, from_unit, to_unit)
                print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
            
            else:
                print("Invalid choice. Please select a valid option.")
        
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()
