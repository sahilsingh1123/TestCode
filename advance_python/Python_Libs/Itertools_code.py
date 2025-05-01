import itertools
import operator

# 1. itertools.accumulate
print("itertools.accumulate example:")
data = [1, 2, 3, 4, 5]
result = list(itertools.accumulate(data, operator.mul))  # Multiply cumulatively
print(result)  # Output: [1, 2, 6, 24, 120]
print()

# 2. itertools.batched
print("itertools.batched example:")
data = ["apple", "banana", "cherry", "date", "elderberry"]
batches = list(itertools.batched(data, 2))  # Batch data into pairs
print(batches)  # Output: [('apple', 'banana'), ('cherry', 'date'), ('elderberry',)]
print()

# 3. itertools.chain
print("itertools.chain example:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
chained = list(itertools.chain(list1, list2))  # Chain iterables together
print(chained)  # Output: [1, 2, 3, 4, 5, 6]
print()

# 4. itertools.chain.from_iterable
print("itertools.chain.from_iterable example:")
nested_lists = [[1, 2, 3], [4, 5, 6]]
flattened = list(itertools.chain.from_iterable(nested_lists))  # Flatten a list of lists
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]
print()

# 5. itertools.combinations
print("itertools.combinations example:")
letters = ["A", "B", "C", "D"]
combinations = list(itertools.combinations(letters, 2))  # All 2-length combinations
print(combinations)  # Output: [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
print()

# 6. itertools.combinations_with_replacement
print("itertools.combinations_with_replacement example:")
comb_with_replacement = list(itertools.combinations_with_replacement([1, 2, 3], 2))  # Combinations with repetition
print(comb_with_replacement)  # Output: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
print()

# 7. itertools.compress
print("itertools.compress example:")
data = ["A", "B", "C", "D"]
selectors = [1, 0, 1, 0]
compressed = list(itertools.compress(data, selectors))  # Select elements based on selectors
print(compressed)  # Output: ['A', 'C']
print()

# 8. itertools.count
print("itertools.count example:")
counter = itertools.count(10, 2)  # Start at 10, increment by 2
for i in range(5):
    print(next(counter))  # Output: 10, 12, 14, 16, 18
print()

# 9. itertools.cycle
print("itertools.cycle example:")
cycled = itertools.cycle(["A", "B", "C"])
for i in range(6):
    print(next(cycled))  # Output: A B C A B C
print()

# 10. itertools.dropwhile
print("itertools.dropwhile example:")
numbers = [1, 2, 5, 7, 9, 3]
dropped = list(itertools.dropwhile(lambda x: x < 5, numbers))  # Drop while number is less than 5
print(dropped)  # Output: [5, 7, 9, 3]
print()

# 11. itertools.filterfalse
print("itertools.filterfalse example:")
numbers = [0, 1, 2, 3, 4, 5]
filtered_false = list(itertools.filterfalse(lambda x: x % 2 == 0, numbers))  # Keep odd numbers
print(filtered_false)  # Output: [1, 3, 5]
print()

# 12. itertools.groupby
print("itertools.groupby example:")
data = [("a", 1), ("a", 2), ("b", 1), ("b", 2)]
grouped = [(key, list(group)) for key, group in itertools.groupby(data, key=lambda x: x[0])]  # Group by first element
print(grouped)  # Output: [('a', [('a', 1), ('a', 2)]), ('b', [('b', 1), ('b', 2)])]
print()

# 13. itertools.islice
print("itertools.islice example:")
sliced = list(itertools.islice(range(10), 2, 8, 2))  # Slice elements from 2 to 8 with a step of 2
print(sliced)  # Output: [2, 4, 6]
print()

# 14. itertools.permutations
print("itertools.permutations example:")
permutations = list(itertools.permutations([1, 2, 3], 2))  # All 2-length permutations
print(permutations)  # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print()

# 15. itertools.product
print("itertools.product example:")
products = list(itertools.product([1, 2], ["A", "B"]))  # Cartesian product of both lists
print(products)  # Output: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
print()

# 16. itertools.repeat
print("itertools.repeat example:")
repeated = list(itertools.repeat("Hello", 3))  # Repeat 'Hello' 3 times
print(repeated)  # Output: ['Hello', 'Hello', 'Hello']
print()

# 17. itertools.starmap
print("itertools.starmap example:")
data = [(2, 5), (3, 2), (10, 3)]
starmapped = list(itertools.starmap(pow, data))  # Apply pow() to each tuple
print(starmapped)  # Output: [32, 9, 1000]
print()

# 18. itertools.takewhile
print("itertools.takewhile example:")
numbers = [1, 2, 5, 7, 9, 3]
taken = list(itertools.takewhile(lambda x: x < 5, numbers))  # Take while number is less than 5
print(taken)  # Output: [1, 2]
print()

# 19. itertools.tee
print("itertools.tee example:")
data = [1, 2, 3, 4]
iter1, iter2 = itertools.tee(data, 2)  # Create two independent iterators
print(list(iter1))  # Output: [1, 2, 3, 4]
print(list(iter2))  # Output: [1, 2, 3, 4]
print()

# 20. itertools.zip_longest
print("itertools.zip_longest example:")
list1 = [1, 2, 3]
list2 = ["A", "B"]
zipped = list(itertools.zip_longest(list1, list2, fillvalue="?"))  # Zip lists with '?'
print(zipped)  # Output: [(1, 'A'), (2, 'B'), (3, '?')]
