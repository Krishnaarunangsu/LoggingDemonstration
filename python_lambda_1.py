#  lambda arguments : expression

def x(a):
    return a

x = lambda a: a

print(x(1)
      )
#  A lambda function that adds 10 to the number passed in as an argument, and print the result:
x =  lambda a : a + 10
print(x(5))

#  Lambda functions can take any number of arguments:

#  A lambda function that multiplies argument a with argument b and print the result:
x = lambda a, b : a * b
print(x(5, 10))

#  A lambda function that sums argument a, b, and c and print the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 7))
