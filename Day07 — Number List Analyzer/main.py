def analyze_numbers(numbers):
    even = 0
    odd = 0
    positive = 0
    negative = 0

    for number in numbers:

        if number % 2 == 0:
            even += 1
        else:
            odd += 1


        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1

    print("\n---- Result ----")
    print(f"Total Numbers: {len(numbers)}")
    print(f"Even Numbers: {even}")
    print(f"Odd Numbers: {odd}")
    print(f"Positive Numbers: {positive}")
    print(f"Negative Numbers: {negative}")
    print(f"Maximum Number: {max(numbers)}")
    print(f"Minimum Number: {min(numbers)}")
    print(f"Average Number: {sum(numbers)/len(numbers):.2f}")



numbers = []

print("Enter numbers (type 0 to stop):")

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    numbers.append(number)

if len(numbers) == 0:
    print("No numbers entered.")
else:
    analyze_numbers(numbers)
