# Name: <Raga Mohammad Aidil Fitra>
# NIM: <2611532002>
# Question 5

username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")


Nim = input("NIM: ")

if len(Nim) != 10:
    print("Invalid: must be 10 digits")
elif not Nim.isdigit():
    print("Invalid: must contain only digits")
else:
    print("Valid")