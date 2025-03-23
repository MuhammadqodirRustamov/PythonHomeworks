while True:
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Password is too short.")
        continue
    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
            break
    if not uppercase:
        print("Password must contain at least one uppercase letter.")
        continue
    print("Password is strong.")
    break
