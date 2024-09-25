class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hi, I'm {self.name}, I'm {self.age} years old and my gender is {self.gender}.")

person1 = Person("Jeepers", 20, "male")
person1.introduce()
