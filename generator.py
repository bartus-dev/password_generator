import secrets

def ask_yes_no(question):
    while True:
        choice = input(question)
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Wrong choice, try again!")
            continue


def generate():
    lower_case = "abcdefghijklmnoprstuwyz"
    upper_case = "ABCDEFGHIJKLMNOPRSTUWYZ"
    digits = "1234567890"
    symbols = "!@#$%^&*()"
    data = ""
    password = ""
    i = 0


    try:
        options = [
            ("Lowercase letters? (y/n): ", lower_case, "lowercase letters"),
            ("Uppercase letters? (y/n): ", upper_case, "uppercase letters"),
            ("Digits? (y/n): ", digits, "digits"),
            ("Symbols? (y/n): ", symbols, "symbols")
        ]

        while True:
            for question, characters, category_name in options:
                if ask_yes_no(question):
                    data += characters
                    print("Added: ", category_name)
                else:
                    print("Skipped: ", category_name)

            if not data:
                print("You need to select at least one character type.\n")
                continue
            else:
                password_length = int(input("Choose length of your password: "))
                
                if password_length <= 0:
                    return "\nPassword length must be greater than 0!\n"    
                else:
                    while i < password_length:
                        password += secrets.choice(data)
                        i += 1

                    return f"\nYour password: {password}"
        
    except ValueError:
        return "Please enter a valid whole number.\n"

print(generate())