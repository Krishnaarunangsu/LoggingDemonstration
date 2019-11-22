#  A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a: a + 10

print(f'Lambda Output:{x(5)}')

#  Lambda functions can take any number of arguments:
y = lambda a, b: a * b
print(f'Lambda Output:{y(5, 7)}')

#  A lambda function that sums argument a, b, and c and print the result:
z = lambda a, b, c: a + b + c
print(f'Lambda Output:{z(5, 6, 7)}')

#  Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:
def my_func(n):
    """
    Doing some functionality
    :param n:
    :return:
    """
    return lambda a: a * n

my_double = my_func(2)
my_double_Result: int = my_double(5)
print(f'Complex Lambda Output:{my_double_Result}')


#  https://www.w3schools.com/python/python_lambda.asp
#  https://www.programiz.com/python-programming/anonymous-function
#  https://www.geeksforgeeks.org/lambda-expressions-java-8/
#  https://beginnersbook.com/2017/10/java-lambda-expressions-tutorial-with-examples/
#  https://www.journaldev.com/16703/java-lambda-expression

#  Lambda Java example
#  lambda expressions are added in Java 8 and provide below functionalities.
#  Enable to treat functionality as a method argument, or code as data.
#  A function that can be created without belonging to any class.
#  A lambda expression can be passed around as if it was an object and executed on demand.
#  https://www.javatpoint.com/java-lambda-expressions
