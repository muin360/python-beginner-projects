# project no.001
name = input("Enter your name: ")
current_age = int(input("Enter your age: "))
after_5_years = current_age + 5
height_in_meter = float(input("Enter your height in meters: "))
height_in_cm = height_in_meter * 100


results = [
    f"Name: {name}",
    f"Current Age: {current_age} years old",
    f"After 5 years: {after_5_years} years old",
    f"Height: {height_in_cm} cm"
]


if current_age >= 18:
    status = "Adult"
else:
    status = "Minor"
    if after_5_years >= 18:
        status += " (After 5 years, you will be an adult)"


results.append(f"Status: {status}")


for item in results:
    print(item)


