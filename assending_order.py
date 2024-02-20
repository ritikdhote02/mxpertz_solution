lst = [20,25,10,45,22,50,40]
result = []

while lst:
    minimum = lst[0]   
    for x in lst: 
        if x < minimum:
            minimum = x
    result.append(minimum)
    lst.remove(minimum)    

print (result)