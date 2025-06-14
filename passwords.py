# File to store passwords
PASSWORD_FILE = "passwords.txt"
passwords = {}

def load_passwords():
    try:
        with open(PASSWORD_FILE, "r") as f:
            for line in f:
                if ':' in line:
                    nick, pwd = line.strip().split(":", 1)
                    passwords[nick] = pwd
    except FileNotFoundError:
        pass  # It's okay if the file doesn't exist yet

def save_passwords():
    with open(PASSWORD_FILE, "w") as f:
        for nick, pwd in passwords.items():
            f.write(f"{nick}:{pwd}\n")

def validate_password(password):
    assert len(password) >= 6, "Your password must contain at least 6 characters!"

    has_lower = has_upper = has_digit = has_special = False
    special_characters = "~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"

    for char in password:
        if 'a' <= char <= 'z':
            has_lower = True
        elif 'A' <= char <= 'Z':
            has_upper = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in special_characters:
            has_special = True
        else:
            raise Exception("Unsupported symbol in password!")

    assert has_lower, "Password must include at least one lowercase letter."
    assert has_upper, "Password must include at least one uppercase letter."
    assert has_digit, "Password must include at least one digit."
    assert has_special, "Password must include at least one special character."

def create_password():
    try:
        new_password = input("Create new password: ")
        validate_password(new_password)

        while True:
            nick_name = input("Type your nickname: ")
            if nick_name in passwords:
                raise KeyError("This nickname is already used. Please choose another one.")
            else:
                passwords[nick_name] = new_password
                save_passwords()
                print(f"Dear {nick_name}, your password is successfully created! Please sign in.")
                validate_existing_password()
                break

    except AssertionError as ae:
        print(f"Password Error: {ae}")
    except Exception as e:
        print(f"Error: {e}")

def validate_existing_password():
    tries = 0
    while tries < 3:
        try:
            nick = input("Please type your nickname: ")
            password = input("Please type your password: ")

            assert nick in passwords, "Nickname does not exist!"
            assert passwords[nick] == password, "Incorrect password!"
            print("Welcome to your profile page!")
            return

        except AssertionError as ae:
            tries += 1
            print(f"Login Error: {ae}")
            if tries == 3:
                raise Exception("You've used all 3 attempts to sign in.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

def main():
    load_passwords()

    try:
        todo = input("Do you want to generate a new password? (yes/no): ").strip().lower()
        assert todo in ('yes', 'no'), "You must type 'yes' or 'no' only."

        if todo == 'yes':
            create_password()
        elif todo == 'no':
            validating = input("Do you want to validate your password? (yes/no): ").strip().lower()
            if validating == 'yes':
                validate_existing_password()
            else:
                print("No operation performed. Goodbye!")

    except AssertionError as ae:
        print(f"Input Error: {ae}")
    except Exception as e:
        print(f"Unhandled Error: {e}")

main()
