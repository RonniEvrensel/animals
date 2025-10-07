from abc import ABC, abstractmethod

# Now we define an abstract base class for animals
class Animal(ABC):
# Defines attributes and initializes them
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age  
        self.breed = breed
        self.owner = owner
    
# common method to all animals that inherit this class
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
# abstract method for speak
    @abstractmethod
    def speak(self):
        pass



# Dog
class Dog(Animal):

    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed, owner)
    
    def speak(self):
        print(f"{self.name} shouts Woof Woof!")

    
# Cat
class Cat(Animal):
    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed, owner)


    def speak(self):
        print(f"{self.name} says Meow!")


# rabbit
class Rabbit(Animal):
    def __init__(self, name, age, breed, owner=None):
        super().__init__(name, age, breed, owner)

    def speak(self):
        print(f"{self.name} says Sniff Sniff!")
    
  
    

# owner 
class Owner:
    def __init__(self, name, city, email, number):
        self.name = name
        self.city = city    
        self.email = email
        self.number = number



#owners
o1 = Owner("Alice", "Halmstad", "alice@hh.se", "0701234567")
o2 = Owner("Bob", "Stockholm", "Bob@hotmail.com", "0737654321")
o3 = Owner("Charlie", "Gothenburg", "cc@live.se", "0769876543")
o4 = Owner("Diana", "Malmö", "borfed@outlook.com", "0794561238")
o5 = Owner("Eva", "Uppsala", "EvaU@msn.com", "0723216549")
    
# dogs
dog1 = Dog("Gustav", 3, "Golden Retriever", o1)
dog2 = Dog("Fido", 5, "Labrador", o2)

# cats
cat1 = Cat("Polly", 2, "Siamese", o3) 
cat2 = Cat("Misse", 4, "Persian", o4)
cat3 = Cat("Whiskers", 1, "Maine Coon", o5)

# rabbits
rabbit1 = Rabbit("Sylas", 1, "wild rabbit")
rabbit2 = Rabbit("Bunny", 3, "Netherland Dwarf")
rabbit3 = Rabbit("Thumper", 2, "Lionhead")
rabbit4 = Rabbit("Coco", 4, "Flemish Giant")
rabbit5 = Rabbit("Oreo", 2, "Dutch")


# prints
dog1.speak()
dog2.sleep()
dog2.speak()    
cat1.speak()
cat2.sleep()
cat3.speak()
cat3.sleep()
rabbit1.sleep()
rabbit1.speak()
rabbit2.sleep()
rabbit3.speak()
rabbit4.speak()
rabbit5.sleep()
rabbit5.speak()



