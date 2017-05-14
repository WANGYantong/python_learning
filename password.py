password_list = ["****", "12345"]


def account_login():
    i = 3
    while i > 0:
        password = input("Password:")
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]
        if password_correct:
            print("Login success!")
            break
        elif password_reset:
            new_password = input("Enter a new password:")
            password_list.append(new_password)
            print("Your password has changed successfully!")
        else:
            i = i-1
            print("Wrong password or invalid input!\n {} times left!".format(i))

account_login()

