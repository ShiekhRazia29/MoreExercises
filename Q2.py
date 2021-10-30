number_of_students=int(input("Enter total number of students in NG:"))
budget_of_1student=int(input("Enter the budget of one student:"))
sum=number_of_students*budget_of_1student
print("Total budget",sum)
if sum<=50000:
    print("We are managing within our budget per student")
else:
    print("We are not within budget")