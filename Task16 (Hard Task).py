def length_converter():
    print("\nLength Conversion:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} km = {miles:.2f} miles")
    elif choice == "2":
        miles = float(input("Enter distance in miles: "))
        km = miles / 0.621371
        print(f"{miles} miles = {km:.2f} km")
    else:
        print("Invalid choice.")

def weight_converter():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kg = {pounds:.2f} pounds")
    elif choice == "2":
        pounds = float(input("Enter weight in pounds: "))
        kg = pounds / 2.20462
        print(f"{pounds} pounds = {kg:.2f} kg")
    else:
        print("Invalid choice.")

def temperature_converter():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f:.2f}°F")
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c:.2f}°C")
    else:
        print("Invalid choice.")
while True:
    print("\n=== Unit Converter Menu ===")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")

    main_choice = input("Choose a category (1-4): ")

    if main_choice == "1":
        length_converter()
    elif main_choice == "2":
        weight_converter()
    elif main_choice == "3":
        temperature_converter()
    elif main_choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please choose from 1 to 4.")
