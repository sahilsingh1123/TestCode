"""this class consists of the recursive method implementation.."""

"""
Fibonacci series testing
"""
from ColorMessagePrint import ColorPrint as pm


def fibonacci_iterative(number):
    """

    :param number: int
    :return: int - Fibonacci number.
    """
    a, b = 0, 1
    if number == 1:
        return a
    elif number == 2:
        return b
    elif number > 2:
        c = None
        for i in range(number - 2):
            c = a + b
            a, b = b, c

        return c


def fibonacci_recursion(number):
    """

    :param number:
    :return: int: value of the fibonacci.
    """
    print("fibonnaci main function call: ", number)
    if number.__lt__(2):
        return number
    else:
        print(number - 2, "inside the else condition of fib", number - 1)
        return fibonacci_recursion(number - 2) + fibonacci_recursion(number - 1)


while True:
    pm.print_warn("press q to quit the execution")
    pm.print_info("Fibonacci Position : ")
    userInputData: str = input()
    if userInputData.__eq__("q") or userInputData.__eq__("Q") or userInputData.__eq__("quit"):
        break
    else:
        pm.print_pass("Fibonacci Number is : {}".format(fibonacci_recursion(int(userInputData))))
