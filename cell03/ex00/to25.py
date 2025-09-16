def main():
    try:
        user_input = input("Enter a number : ")
        number = int(user_input)
        if number > 25:
            print("Error")
        else:
            for i in range(number, 26):
                print(i)
    except ValueError:
        print("Please enter a valid intefer.")
if __name__ == "__main__":
    main()