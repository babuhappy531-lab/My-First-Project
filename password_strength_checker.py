print("Password Strength Checker")
psk=input("Enter your password:")

upperc=False
lowerc=False
numc=False
lengthc=False
symbolc=False

def check():
    for password in psk:
        if password.isupper():
            global upperc
            upperc=True
        if password.islower():
            global lowerc
            lowerc=True
        if password.isdigit():
            global numc
            numc=True
        if len(psk) > 8:
            global lengthc
            lengthc=True
        if not password.isalnum():
            global symbolc
            symbolc=True
         
    result=upperc + lowerc + numc + lengthc + symbolc
    if upperc:
        print("uppercase :✅")
    if lowerc:
        print("lowercase :✅")
    if numc:
        print("number : ✅")
    if lengthc:
        print("length :✅")
    if symbolc:
        print("alnum :✅")
        
        
    if result == 5:
        print("Your password is very strong.")
    elif result ==4:
        print("Your password is strong.")
    elif result ==3:
        print("Your password is medium.")
    elif result <3:
        print("Your password is weak")
check()
