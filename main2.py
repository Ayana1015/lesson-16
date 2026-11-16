try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("The result of division is:", result)
except ValueError as ex:
    print("Invalid input! Please enter valid integers.")
except ZeroDivisionError as ex:
    print("Error! Division by zero is not allowed.")
except:
    print("An unexpected error occurred.")
else:
    print("no exceptions")
finally:
    print("Execution completed.")