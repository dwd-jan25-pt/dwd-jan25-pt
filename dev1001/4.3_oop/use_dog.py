# dog.py

'''
--- MODIFY TASKS ---

1. Add a new instance variable age to our Dog.

2. Add a new method 'celebrate_birthday' that increases the dog's age by 1 and prints a message.
'''

class Dog:
    # This is the constructor method
    def __init__(self, name_param, breed_param, age_param):
        print(f"A new dog named {name_param} is being created!")
        self.name = name_param  # Instance variable
        self.breed = breed_param # Instance variable
        self.age = age_param

    # This is a method
    def bark(self):
        print(f"{self.name} says: Woof!")

    def celebrate_birthday(self):
        self.age += 1
        print(f'HAPPY BIRTHDAY {self.name}!!! You are {self.age} years old today!')

    def describe(self):
        print(f"{self.name} is a {self.breed}.")

# --- Let's USE the Dog class ---
print("--- Creating and Using Dog Objects ---")
# Create an object (instance) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever", 5)

# Create another object
dog2 = Dog("Lucy", "Poodle", 2)

# Call methods on the objects
dog1.describe()
dog1.bark()

print("-" * 10) # Separator

dog2.describe()
dog2.bark()

print("\n--- Accessing Instance Variables (generally done via methods) ---")
print(f"Dog 1's name is: {dog1.name}")
print(f"Dog 2's breed is: {dog2.breed}")

print(f"{dog1.name} is {dog1.age} years old.")
dog1.celebrate_birthday()
print(f"{dog1.name} is {dog1.age} years old.")
