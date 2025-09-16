def main():
    try:
        num = float(input("Enter a number: "))
        if num < 0:
            print("The number is negative.")
        elif num > 0:
            print("The number is positive.")
        else:
            print("The number is both popsitive and negative.")
    except ValueError:
        print("Invalid input - please enter a valid number.")
if __name__ == "__main__":
    main() 