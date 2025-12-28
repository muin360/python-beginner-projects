# Project no.002
numbers = []

results = []

print("Please enter 10 numbers:")

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)


    if num == 0:
        results.append("The number is Zero")

    elif num > 0:
        if num % 2 == 0:
            results.append("The number is Even and Positive")
        else:
            results.append("The number is Odd and Positive")

    else:
        if num % 2 == 0:
            results.append("The number is Even and Negative")
        else:
            results.append("The number is Odd and Negative")


print("\nAnalysis Results:")
for res in results:
    print(res)
