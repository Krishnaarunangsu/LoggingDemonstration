#  Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:


def my_func(n):
    """

    :param n:
    :return:
    """
    return  lambda a: a * n

#  Use that function definition to make a function that always doubles the number you send in:
my_doubler = my_func(2)
print(my_doubler(5))

my_tripler = my_func(3)
print(my_tripler(5))
