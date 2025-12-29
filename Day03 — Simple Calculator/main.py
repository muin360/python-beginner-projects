def analyze_result(result):
    if result == 0:
        print("The result is 0")
    elif result > 0 and result % 2 == 0:
        print("The result is even and positive")
    elif result > 0 and result % 2 != 0:
        print("The result is odd and positive")
    elif result < 0 and result % 2 == 0:
        print("The result is even and negative")
    else:
        print("The result is odd and negative")


while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Program is closed")
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        if num2 == 0:
            print("Cannot divide by zero")
            continue
        result = num1 // num2
    else:
        print("Please enter a valid choice")
        continue

    print("The result is:", result)
    analyze_result(result)

