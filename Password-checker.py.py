import string
common_passwords = ['123456', 'password', '123456789', '12345678', '12345', '1234567', '1234567890', 'qwerty', 'abc123']
def password_strength(password):
    length = 0
    diversity = 0
    if len(password) >= 8:
        length = 1
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    diversity = sum([has_upper, has_lower, has_digit, has_special])
    strength = length + diversity
    issues = []
    if length == 0:
        issues.append("Password is too short.")
    if not has_upper:
        issues.append("Add uppercase letters.")
    if not has_lower:
        issues.append("Add lowercase letters.")
    if not has_digit:
        issues.append("Add digits.")
    if not has_special:
        issues.append("Add special characters.")
    if password in common_passwords or '@123' in password:
        issues.append("Your password is too common.")
    return strength, issues
password = input("Enter a password to test: ")
strength, issues = password_strength(password)
print(f"Password strength: {strength}")
if issues:
    print("Issues with password:")
    for f in issues:
        print(f" - {f}")
else:
    print("Your password is strong!")