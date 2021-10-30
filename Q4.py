num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
if (num1 and num2)<num3:
    print("Number 3 is greater",num3) 
elif (num2 and num3)< num1:
    print("Number 1 is greater",num1)
elif (num1 and num3)<num2:
    print("Number 2 is greater")
else:
    print("equal")