try:
    number = int(input("Enter a number: "))
    print("The number you entered is:", number)
except ValueError as ex:
    print("Invalid input! Please enter a valid integer.")