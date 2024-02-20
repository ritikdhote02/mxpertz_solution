lst = [20,25,10,45,22,50,40]
result = 0

for i in range(0, len(lst)):
    if result <= lst[i]:
        result = lst[i]

print("Largest number in list is : ",result)