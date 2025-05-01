# partialmethod
from functools import partialmethod


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def multiply(self, x, y):
        return x * y * self.factor

    double = partialmethod(multiply, y=2)
    triple = partialmethod(multiply, y=3)


# Create an instance of Multiplier
multiplier = Multiplier(10)

# Call the original multiply method
result1 = multiplier.multiply(5, 2)
print(result1)  # Output: 100

# Call the double method created using partialmethod
result2 = multiplier.double(5)
print(result2)  # Output: 100

# Call the triple method created using partialmethod
result3 = multiplier.triple(5)
print(result3)  # Output: 150


#############################################################
# reduce
from functools import reduce

# Calculate the sum of a list of numbers
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # Output: 15

# Concatenate a list of strings
strings = ["Hello", " ", "world", "!"]
concatenated = reduce(lambda x, y: x + y, strings)
print(concatenated)  # Output: Hello world!

#############################################################
# partial
from functools import partial

# Create a new function based on the built-in `int` function
# where the base argument is pre-set to 2
binary_to_decimal = partial(int, base=2)

# Use the new function to convert binary strings to decimal numbers
decimal_number = binary_to_decimal("101010")
print(decimal_number)  # Output: 42

#############################################################
# singledispatch
from functools import singledispatch


@singledispatch
def process_data(data):
    raise NotImplementedError("Unsupported data type")


@process_data.register(int)
def process_int(data):
    print("Processing integer:", data)


@process_data.register(str)
def process_str(data):
    print("Processing string:", data)


@process_data.register(list)
def process_list(data):
    print("Processing list:", data)


# Example usage
process_data(42)  # Output: Processing integer: 42
process_data("Hello, World!")  # Output: Processing string: Hello, World!
process_data([1, 2, 3])  # Output: Processing list: [1, 2, 3]
process_data(3.14)  # Raises NotImplementedError

#############################################################
# singledispatchmethod
from functools import singledispatchmethod


class Shape:
    pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height


class AreaCalculator:
    @singledispatchmethod
    def calculate_area(self, shape):
        raise NotImplementedError("Unsupported shape")

    @calculate_area.register
    def _(self, shape: Circle):
        return 3.14 * shape.radius**2

    @calculate_area.register
    def _(self, shape: Rectangle):
        return shape.width * shape.height

    @calculate_area.register
    def _(self, shape: Triangle):
        return 0.5 * shape.base * shape.height


# Usage
calculator = AreaCalculator()
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print(calculator.calculate_area(circle))  # Output: 78.5
print(calculator.calculate_area(rectangle))  # Output: 24
print(calculator.calculate_area(triangle))  # Output: 12

#############################################################
# total ordering
from functools import total_ordering


@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1 == person2)  # Output: False
print(person1 != person2)  # Output: True
print(person1 < person2)  # Output: True
print(person1 > person2)  # Output: False
print(person1 <= person2)  # Output: True
print(person1 >= person2)  # Output: False

#############################################################
# cache
from functools import cache


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # Output: 5
print(fibonacci(10))  # Output: 55

### cache_property
from functools import cached_property


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        print("Calculating area...")
        return 3.14 * self.radius**2


circle = Circle(5)
print(circle.area)  # Output: Calculating area... 78.5
print(circle.area)  # Output: 78.5 (cached value)

## lru_cache
from functools import lru_cache


@lru_cache(maxsize=3)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # Output: 5
print(fibonacci(10))  # Output: 55
print(fibonacci(15))  # Output: 610
print(fibonacci(5))  # Output: 5 (cached value)
print(fibonacci(20))  # Output: 6765 (recomputes due to cache limit)
