while True:
    print('enter you age')
    age = input()
    if age.isdecimal():
        break
    print('enter your age in years')
while True:
    print("enter you password")
    password = input()
    if password.isalnum():
        break
    print("enter only password")
