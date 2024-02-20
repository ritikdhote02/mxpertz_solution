class Vhicle:
    def color(self):
        print("My car has black color.")
        
class Bikes(Vhicle):
    def engine(self):
        print("My bike has 200CC engine")
        
        
obj = Bikes()

print(obj.engine())
print(obj.color())
        
        
        
        