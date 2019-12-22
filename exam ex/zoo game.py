
class Animal:
    
    def __init__(self,name,diurnal=None,nb_legs=None,asleep=False):
        self.name= name
        self.diurnal=diurnal
        self.nb_legs=nb_legs
        self.asleep=asleep

    def sleep(self):
        if self.asleep == False:
            self.asleep= True
        else:
            raise RuntimeError
    def wake_up(self):
        if self.asleep == True:
            self.asleep= False
        else:
            raise RuntimeError

class Lion(Animal):
    
    def __init__(self,name):
        super().__init__(name)
        self.diurnal= True
        self.nb_legs= 4
        
    def roar(self):
        print("ROARRR!!!")
        
class Owl(Animal):   
    
    def __init__(self,name):
        super().__init__(name)
        self.diurnal= False
        self.nb_legs= 2
        
    def fly(self):
        pass
    
class Giraffe(Animal):
    
    def __init__(self,name,neck_length):
        super().__init__(name)
        self.diurnal= True
        self.nb_legs= 4
        if neck_length > 0:
            self.neck_length = neck_length
        else:
            raise ValueError
        
class Zoo:
    
    def __init__(self,animals=[]):
        self.animals= animals
        
    def add_animal(self,animal):
        if issubclass(type(animal),Animal):
            self.animals.append(animal)
        else:
            raise ValueError

def create_my_zoo():
    zoo= Zoo()
    zoo.add_animal(Lion("Ben"))
    zoo.add_animal(Owl("John"))
    zoo.add_animal(Giraffe("Giant",0.2))
    zoo.add_animal(Giraffe("Stacy",10))
    return zoo
        
    
lion= Lion("john") 
lion.roar()       
zoo = create_my_zoo()
owl= Owl("John")
owl.fly()
print(zoo.animals[1].nb_legs)
print(len(zoo.animals))