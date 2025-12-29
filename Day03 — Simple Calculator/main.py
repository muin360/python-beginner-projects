def analyze_result(result):
    if result == 0:
        print("Result is Zero")
    elif result > 0 and result % 2 == 0:
        print("Result is Even and Positive")
    elif result > 0 and result % 2 != 0:
        print("Result is Odd and Positive")
    elif result < 0 and result % 2 == 0:
        print("Result is Even and Negative")
    else:
        print("Result is Odd and Negative")


while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Program closed")
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
        print("Invalid choice")
        continue

    print("Result:", result)
    analyze_result(result)
