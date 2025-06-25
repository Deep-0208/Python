class Animal :
    pass

class Pet(Animal):
    pass

class dog(Pet):
    def bark(self):
        print("Dog is barking")
    
d = dog()
d.bark()