age_input = input("Please tell me your age:")
try:
    age = int(age_input)
    print(f"You are currently {age} years old.")
    print(f"In 10 years, you'll be {age + 10} years old.")
    print(f"In 20 years, you'll be {age + 20} years old.")
    print(f"In 30 years, you'll be {age + 30} years old.")
except ValueError:
    print("Please enter a valid number for your age.")