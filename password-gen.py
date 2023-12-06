import random
import string
import ctypes

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

custom_title = "Password Gen - Mr Dan"

set_console_title(custom_title)

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = ""
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        print("Please select at least one character set.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_special_chars = input("Include special characters? (y/n): ").lower() == "y"

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
    
    if password:
        print("Generated password:", password)
    
    input("Press Enter to exit...")
