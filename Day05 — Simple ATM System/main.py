# Day 5 Project: Simple ATM System

balance = 10000
max_amount = 8000


def check_balance():
    print(f"Your current balance is: {balance}$")


def deposit():
    global balance
    amount = int(input("Enter the amount you want to deposit: "))

    if amount <= 0:
        print("Invalid deposit amount")
        return

    balance += amount
    print(f"{amount}$ deposited successfully")
    print(f"Your current balance is: {balance}$")


def withdraw():
    global balance
    print("current balance is: ", balance)
    print(f"Max withdraw limit is {max_amount}$")
    amount = int(input("Enter the amount you want to withdraw: "))

    if amount > max_amount:
        print(f"Sorry, you cannot withdraw more than {max_amount}$")
        return
    elif amount > balance:
        print(f"Sorry, insufficient balance. Current balance: {balance}$")
        return

    balance = balance - amount
    print(f"{amount}$ withdrawn successfully")
    print(f"Your current balance is: {balance}$")

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid choice. Try again.")
