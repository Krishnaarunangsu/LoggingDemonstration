# Fibonacci Series

class FibonacciWithRecursion:
    """
    Fibonacci Series with Recursion
    """

    def recur_fibo(n):
        if n <= 1:
            return n
        else:
            return(recur_fibo(n-1) + recur_fibo(n-2))
        
# take input from the user

    @staticmethod
    def calculate_fibonacci(input_num):
        if input_num <= 1:
            return 1
        else:
            return (calculate_fibonacci(input_num - 1) + calculate_fibonacci(input_num - 2))
