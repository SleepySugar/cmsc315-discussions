"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.

# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
class ParentClass:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Replace the pass statement with your implementation.
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."




# TODO 2:
# Create a child class that inherits from the parent class.

# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
class ChildClass(ParentClass):
    school_type = "University"

    def __init__(self, name, age, major, year):
        super().__init__(name, age)
        self.major = major
        self.year = year

    def study(self):
        return f"{self.name} is studying {self.major}."

# Replace the pass statement with your implementation.
    def introduce(self):
        return (
            f"My name is {self.name}, I am {self.age} years old, "
            f"and I am a {self.year} student studying {self.major}."
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    student1 = ChildClass("Teresa", 24, "Computer Science", "Junior")
    student2 = ChildClass("Max", 25, "Information Technology", "Senior")

    print("Class variable through class:", ChildClass.school_type)

    print("Class variable through object:", student1.school_type)

    student1.favorite_language = "Python"

    print("\nStudent 1 namespace:")
    print(student1.__dict__)

    print("\nStudent 2 namespace:")
    print(student2.__dict__)

    # Display information about the class namespace
    print("\nChildClass namespace:")
    print(ChildClass.__dict__.keys())

    print("\nParentClass namespace:")
    print(ParentClass.__dict__.keys())


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = {
        "name": "Morgan",
        "courses": ["Python", "Networking", "Database"],
        "grades": {"Python": 95, "Networking": 90}
    }

    shallow_copy = copy(original)

    deep_copy = deepcopy(original)


    original["courses"].append("Cybersecurity")
    original["grades"]["Python"] = 100


    print("Original:")
    print(original)

    print("\nShallow Copy:")
    print(shallow_copy)

    print("\nDeep Copy:")
    print(deep_copy)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    parent = ParentClass("Grady", 45)
    print(parent.introduce())

    print("\n=== Child Object ===")
    child = ChildClass("Jaime", 22, "Computer Science", "Senior")
    print(child.introduce())
    print(child.study())

    print("Child's inherited class variable:", child.species)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()