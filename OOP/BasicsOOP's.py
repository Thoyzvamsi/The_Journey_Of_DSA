#Class is a blueprint ,we use this to store related functions in single unit

#Object is an entity which is created from the blueprint
#Objects are stored in real memory (heap memory)

#Method is like a verb in the sentence,we can call this as a function
# * we cannot call the method directly which is declared in a class
# * we have call it with an object : doing work , who's doing work we have to specify with object

#__init__ : it is special method used install default variables and 
# it runs automatically it also as constructor

#class
class laptop:
    #constructor
    def __init__(self,processor,graphics,RAM,ROM,VRAM):
        self.processor = processor
        self.graphics = graphics
        self.RAM = RAM
        self.ROM = ROM
        self.VRAM = VRAM

    def update(self):
        self.graphics = 3060

    def compare(self,other):
        if self.VRAM < ver2.VRAM:
            print("2nd Version has greater ram")
        else:
            print("1st version greater version")

    
    # method
    def specs(self):
        print("Specs of current version :",self.processor,self.graphics,self.RAM,self.ROM,self.VRAM)
        
#objects
ver1 = laptop("ryzen 3",3050,16,256,2)
ver2 = laptop("ryzen 5",3050,16,512,4)
ver3 = laptop("ryzen 7",4050,16,512,4)

ver2.update()

ver1.specs()
ver2.specs()
ver3.specs()
ver1.compare(ver2)

print(id(ver1))
print(id(ver2))