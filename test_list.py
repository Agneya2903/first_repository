#Python Program To remove duplicate values from the list
lis=['apple','banana','apple','mango','apple','pineapple','mango','apple','cherry','apple']
for i in lis:
    if i =="apple":
        lis.remove(i)
print(lis)

