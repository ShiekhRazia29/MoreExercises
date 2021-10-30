password=input("Enter a password:")
if len(password)>=6 and len(password)<16:
        if  ("Z" or "A") and ("2" or "8") and "$" in password:
            print("Strong password")
        else:
            print("Weak password")
else:
    print("Too small.Password should contain atleast")
