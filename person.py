#week4assignment
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Creating an instance of the Person class
person1 = Person("Siana", 22, "Female")

# Calling the introduce method
person1.introduce()

