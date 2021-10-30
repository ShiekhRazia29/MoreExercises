number=int(input("Enter a number:"))
factorial=1
if number>=0:
    for i in range(1,number+1):
        factorial=factorial*i
    print("the factorial of the number",number,"is",factorial)
else:
    print("Factorial doesnot apply for negative numbers")