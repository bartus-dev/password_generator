import random

data = "ABCDEFGHIJKLMNOPRTSUWYZabcdefghijklmnoprstuwyz1234567890!@#$%^&*()"

password = ""

i = 0

try:
    password_length = int(input("Choose length of your password: "))
    if password_length <= 0:
        print("\nPassword length must be greater than 0!\n")
    else:
        while i < password_length:
            password += random.choice(data)
            i += 1

        print(f"Your password: {password}")
except ValueError:
    print("\nPassword length cannot be represented by anything other than an integer\n")