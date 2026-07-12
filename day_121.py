"""
Write a program demonstrating polymorphism.
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the function with different animal instances
animal_sound(dog)  # Outputs: Woof!
animal_sound(cat)  # Outputs: Meow!