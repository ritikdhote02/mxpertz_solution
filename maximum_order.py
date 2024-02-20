lst = [20,25,10,45,22,50,40]
result = []

while lst:
    maximum = lst[0] 
    for x in lst: 
        if x > maximum:
            maximum = x
    result.append(maximum)
    lst.remove(maximum)    

print (result)