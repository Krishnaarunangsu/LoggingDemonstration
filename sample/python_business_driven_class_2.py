# Python program to show that the variables with a value
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
    stream = 'cse'                  # Class Variable
    def __init__(self,name,roll):
        self.name = name            # Instance Variable
        self.roll = roll            # Instance Variable

# Objects of CSStudent class
css_student_1 = CSStudent('Geek', 1)
css_student_2 = CSStudent('Nerd', 2)

print(f'Stream of Student 1:{css_student_1.stream}')  # prints "cse"
print(f'Stream of Student 2:{css_student_2.stream}')  # prints "cse"
print(f'Name of Student 1:{css_student_1.name}')    # prints "Geek"
print(f'Name of Student 2:{css_student_2.name}')    # prints "Nerd"
print(f'Roll of Student 1:{css_student_1.roll}')    # prints "1"
print(f'Roll of Student 2:{css_student_2.roll}')    # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"
