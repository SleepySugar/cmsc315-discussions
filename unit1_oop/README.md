# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Implementation

- Parent Class
I created a ParentClass that included the class variable species, and set it to "Human". The class also included instance variables name and age, initialized through the __init__() constructor.
I added an introduce() method that returned information about the parent object, including objects name and age.

- Child Class and Inheritance
I created a ChildClass that inherited from ParentClass and included a new class variable named school_type, set to "University."
The child class also added instance variables major and year. The super() function was used to initialize the inherited name and age attributes from the parent class.
I added a new study() method that displayed the student's major.
I overrode the inherited introduce() method so it displayed the student's name, age, year, and major.

- Namespaces
I created two ChildClass objects and accessed the school_type class variable through both class and object. I added a favorite_language attribute to only one object and used __dict__ to display instance and class namespaces.

- Shallow and Deep Copying
I created a nested dictionary and made a shallow copy and deep copy.
I modified the original nested data so that the shallow copy reflected changes while the deep copy retained its original values.

- Main Function
I completed main() by creating the parent and child objects, calling their methods, demonstrating inheritance, and running the namespace and copying demonstrations.

- Student-Created Extension
I added the study() method to ChildClass. This method displayed the student's area of study.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.