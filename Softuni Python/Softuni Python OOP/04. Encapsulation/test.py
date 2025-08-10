class Person:
 def __init__(self, name, age=0):
  self.name = name
  self.__age = age
 def info(self):
   print(f"I am {self.name}, {self.__age} years old.")
person = Person('Peter', 25)
# accessing data using the class method
person.info() # I am Peter, 25 years old.
# accessing data directly from outside
print(person.name) # Peter
print(person._Person__age) # AttributeError: 'Person' object has no attribute '__age'

