"""

Test code for recursion

"""

from basic.ColorMessagePrint import ColorPrint


def recursion(n):
    if n == 1:
        return 1
    return n * recursion(n - 1)


ColorPrint.print_bold(str(recursion(5)))
ColorPrint.print_pass("end of program")
