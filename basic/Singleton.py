from typing import Any


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # If there's no instance yet, create one by calling the super().__new__ method
            # This also means __init__ will be called after this new instance is created
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        # If cls._instance is already set, just return it
        # __init__ will not be called in this case, because we're not creating a new instance
        return cls._instance

    def __init__(self, value):
        # This will only be called the first time an instance is created
        self.value = value

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # This will be called every time you call the instance
        # example: my_singleton = Singleton('value')
        # my_singleton('some', 'args') -> __call__ will be called
        # if my_singleton is called
        pass


# Testing the singleton
first_instance = Singleton("First")
second_instance = Singleton("Second")

print(first_instance.value)  # Output: First
print(second_instance.value)  # Output: First
print(first_instance is second_instance)  # Output: True
