X= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

element_list = []

for i in X:
    element_list.extend(i)
    
for i in Y:
    element_list.extend(i)

result = 0
for i in element_list:
    result += i
    
print("The addition of X and Y metrics is : ", result)

