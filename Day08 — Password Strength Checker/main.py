def check_password_strength(password):

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True



    score = 0

    if len(password) >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1


    if score <= 2:
        return "Password is Weak ❌"
    elif score <= 4:
        return "Password is Medium ⚠"
    else:  # score == 5
        return "Password is Strong ✅"



password = input("Enter your password: ")
result = check_password_strength(password)
print("\nPassword Strength:", result)
