class Result:
    def addition(self, a, b):
        return (a + b)
        
    def addition(self, a, b, c=0):
        return (a + b + c)
        
obj = Result()

print(obj.addition(10, 20))
print(obj.addition(10, 20, 30))