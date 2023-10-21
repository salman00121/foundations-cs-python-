def is_strong_password(password):
    if len(password) < 8:
        return "Weak password"


    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False


    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "#?!$":
            has_special = True
