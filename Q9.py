def check_harshad(number):
    rem=0
    digit_sum=0
    check=False
    n=number
    while(n>0):
        rem=n % 10
        digit_sum=digit_sum+rem
        n= n//10
    if number % digit_sum==0:
        check=True
    return check
lower=int(input("Enter lowest number:"))
upper=int(input("Enter upper number:"))
for i in range(lower,upper+1):
    if check_harshad(i):
      print(i,end=" ")
