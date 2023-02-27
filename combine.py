num1=int(input("Enter total right questions in combine exam: "))
num2=int(input("Enter Total number of wrong questions in combine: "))
score=(num1-num2/4)
if num1+num2 > 100:
    print("Something Went wrong please re enter again")
elif num1+num2 < 0:
    print("Wrong scores added")
else:
    print(score)
print("Your Combine Score is ",score)