# Login System using Arrays (Lists) and Strings
# University Presentation — Python

# Arrays to store usernames and passwords
usernames = ["ali", "sara", "john", "admin"]
passwords = ["ali123", "sara456", "john789", "admin000"]


def login():
    print("===== LOGIN SYSTEM =====")
    entered_user = input("Enter username: ")
    entered_pass = input("Enter password: ")

    found = False

    for i in range(len(usernames)):
        if usernames[i] == entered_user and passwords[i] == entered_pass:
            found = True
            break

    if found:
        print("Login Successful! Welcome,", entered_user)
    else:
        print("Login Failed! Invalid username or password.")


login()
