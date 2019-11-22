# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def from_birth_year(cls, name, year):
        """
        calculate age from the year of birth
        :param name:
        :param year:
        :return age:
        """
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def is_adult(age):
        return age > 18


# Function-> not intrinsic to class
def is_employee(emp_no: int) -> object:
    if emp_no >0 and emp_no <= 100:
        print('The employee is in the organisation')


person1 = Person('mayank', 21)
person2 = Person.from_birth_year('mayank', 1996)

print(person1.age)
print(person2.age)
# print(Person.age)

# print the result
print(Person.is_adult(22) )

# print if the Person is an employee of the organisation
print(is_employee(30))
