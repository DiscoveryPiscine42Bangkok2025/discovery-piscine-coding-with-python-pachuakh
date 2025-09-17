first_input = input("Give me the first number: ")
second_input = input("Give me the second number: ")
try:
    num1 = int(first_input)
    num2 = int(second_input)
    print("Thank you!")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print(f"{num1} / {num2} = Cannot divide by zero")
    print(f"{num1} * {num2} = {num1 * num2}")
except ValueError:
    print("Please enter valid numbers.")