from abc import ABC, abstractmethod

#define class for owner and staff
class Person(ABC):
# Defines attributes and initializes them
    def __init__(self, name, city, email, number):
        self.name = name
        self.city = city    
        self.email = email
        self.number = number

    @abstractmethod
    def display_info(self):
        pass
# owner 
class Owner(Person):
    def __init__(self, name, city, email, number):
        super().__init__(name, city, email, number)
        self.name = name
        self.city = city    
        self.email = email
        self.number = number
    def display_info(self):
        print(f"Name: {self.name}, city: {self.city}, Email: {self.email}, Number: {self.number}")
# NEW CLASS STAFF
class Staff(Person):
    def __init__(self, name, role, department, company, email, number):
        self.name = name
        self.role = role
        self.department = department    
        self.company = company
        self.email = email
        self.number = number
    def display_info(self):
        print(f"Name: {self.name}, Role: {self.role}, Department: {self.department}, Company: {self.company}, Email: {self.email}, Number: {self.number}")
    
    


O1 = Owner("Ronni", "Hisingen", "ronni94@live.se", "0737073070")
O1.display_info()

S1 = Staff("Ahmed", "Manager", "Sales", "Elgiganten", "AhmedJihad@elgiganten.se", "0737073071")
S1.display_info()