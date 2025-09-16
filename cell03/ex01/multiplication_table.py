def main():
    try:
        number = int(input("Enter a number to display its multiplication_table: "))
    except ValueError:
        print("Please enter a valid interger.")
        return
    print(f"\nMultiplication table of {number}:")
    print("-" * 30)
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")
if __name__ == "__main__":
    main()