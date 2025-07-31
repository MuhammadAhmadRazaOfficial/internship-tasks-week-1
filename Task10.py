full_name = input("Enter your full name: ")
parts = full_name.strip().split()
if len(parts) >= 2:
    first_name = parts[0]
    last_name = parts[-1]
    username = (first_name[0] + last_name).lower()
    print("Generated username:", username)
else:
    print("Please enter at least a first and last name.")
