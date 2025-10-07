from abc import ABC, abstractmethod

# Now we define an abstract base class for animals
class Animal(ABC):
# Defines attributes and initializes them
    def __init__(self, name, age, breed, weight, owner):
        self.name = name
        self.age = age  
        self.breed = breed
        self.weight = weight
        self.owner = owner
    
# common method to all animals that inherit this class
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
    def eat(self):
        print(f"{self.name} is eating.")        
    
    def greet_owner(self):
        if self.owner:
            print(f"{self.name} greets its owner {self.owner.name}.")
        else:
            print(f"{self.name} has no owner to greet.")
    
# abstract method for speak
    @abstractmethod
    def speak(self):
        pass



# Dog
class Dog(Animal):

    def __init__(self, name, age, breed, weight, owner):
        super().__init__(name, age, breed, weight, owner)
    
    def speak(self):
        print(f"{self.name} shouts Woof Woof!")

    
# Cat
class Cat(Animal):
    def __init__(self, name, age, breed, weight, owner):
        super().__init__(name, age, breed, weight, owner)


    def speak(self):
        print(f"{self.name} says Meow!")


# rabbit
class Rabbit(Animal):
    def __init__(self, name, age, breed, weight=None, owner=None):
        super().__init__(name, age, breed, weight, owner)

    def speak(self):
        print(f"{self.name} says Sniff Sniff!")

# lion
class Lion(Animal):
    def __init__(self, name, age, breed, weight=None, owner=None):
        super().__init__(name, age, breed, weight, owner)

    def speak(self):
        print(f"{self.name} is roaring Roarrr!")
    
    
# owner 
class Owner:
    def __init__(self, name, city, email, number):
        self.name = name
        self.city = city    
        self.email = email
        self.number = number
    def display_info(self):
        print(f"Name: {self.name}, city: {self.city}, Email: {self.email}, Number: {self.number}")
    
# NEW CLASS STAFF
class Staff:
    def __init__(self, name, role, department, company, email, number):
        self.name = name
        self.role = role
        self.department = department    
        self.company = company
        self.email = email
        self.number = number
    
    # method to display staff info
    def display_info(self):
        print(f"Name: {self.name}, Role: {self.role}, Department: {self.department}, Email: {self.email}, Number: {self.number}")

    # method to contact staff
    def contact(self):
        print(f"Contacting {self.name} at {self.email} or {self.number}")  

    # method to assign task 
    def assign_task(self, task):
        print(f"Assigning task '{task}' to {self.name}")

    # method to interact with an animal
    def interact_with_animal(self, animal):
        print(f"{self.name} is interacting with {animal.name}")

    # method for staff to speak
    def staff_speak(self):
        print(f"{self.name} says this dog is heavy!")

    # method to check animal weight
    def weight_check(self, animal):
        print(f"{self.name} is checking the weight of {animal.name}, which is {animal.weight}")

    # method to handle billing
    def billing(self, amount, owner):
        print(f"{self.name} is processing a billing of {amount} kr to {owner.name}")

    # reciept
    def receipt(self, amount):
        print(f"Receipt: {self.company} has received a payment of {amount} kr.")
    
    #staff shift
    def shift(self, shift_time):
        print(f"{self.name} is scheduled to work the {shift_time} shift.")




# staff members
staff1 = Staff("Ronni", "Veterinarian", "Medical", "*VetClinic Halmstad*", "ronni.vetclinic@halmstad.se", "0709876543")

staff2 = Staff("Sara", "Receptionist", "Front Desk","*VetClinic Halmstad*", "sara.vetclinic@halmstad.se", "0731234567")



#owners
o1 = Owner("Alice", "Halmstad", "alice@hh.se", "0701234567")

o2 = Owner("Bob", "Stockholm", "Bob@hotmail.com", "0737654321")

o3 = Owner("Charlie", "Gothenburg", "cc@live.se", "0769876543")

o4 = Owner("Diana", "Malmö", "borfed@outlook.com", "0794561238")

o5 = Owner("Eva", "Uppsala", "EvaU@msn.com", "0723216549")
    
# dogs
dog1 = Dog("Gustav", 3, "Golden Retriever", "5kg", o1)

dog2 = Dog("Fido", 5, "Labrador", "3kg", o2)

# cats
cat1 = Cat("Polly", 2, "Siamese", "10kg", o3) 

cat2 = Cat("Misse", 4, "Persian", "7kg", o4)

cat3 = Cat("Whiskers", 1, "Maine Coon", "11Kg", o5)

# rabbits
rabbit1 = Rabbit("Sylas", 1, "wild rabbit")

rabbit2 = Rabbit("Bunny", 3, "Netherland Dwarf")

rabbit3 = Rabbit("Thumper", 2, "Lionhead")

rabbit4 = Rabbit("Coco", 4, "Flemish Giant")

rabbit5 = Rabbit("Oreo", 2, "Dutch")

# lions
lion1 = Lion("Simba", 11, "African Lion")

lion2 = Lion("Nala", 13, "Asiatic Lion")


# prints

staff1.display_info()
staff2.display_info()
staff1.contact()
staff1.shift("8:00 AM - 4:00 PM")
staff1.assign_task("Checkup on Gustav")
staff1.interact_with_animal(dog1)
dog1.speak()
staff1.staff_speak()
staff1.weight_check(dog1)
staff2.billing(1500, o1)
staff2.receipt(1500)

