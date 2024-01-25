import heapq

# Create an empty heap
heap = []

# Insert elements into the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)

# Remove and return the smallest element
smallest = heapq.heappop(heap)
print(smallest)  # Output: 1

# Retrieve the smallest element without removing it
smallest = heap[0]
print(smallest)  # Output: 3

# Convert a list into a heap
lst = [9, 2, 4, 6, 1]
heapq.heapify(lst)
print(lst)  # Output: [1, 2, 4, 6, 9]

###########################################
import queue

# Create a queue
my_queue = queue.Queue()

# Add items to the queue
my_queue.put(10)
my_queue.put(20)
my_queue.put(30)

# Get and remove items from the queue
item1 = my_queue.get()
item2 = my_queue.get()

print(item1)  # Output: 10
print(item2)  # Output: 20

# queue 2
import queue

# Create a priority queue
my_queue = queue.PriorityQueue()

# Add items to the queue with priorities
my_queue.put((2, 'Task 1'))
my_queue.put((1, 'Task 2'))
my_queue.put((3, 'Task 3'))

# Get and remove items from the queue
item1 = my_queue.get()
item2 = my_queue.get()

print(item1)  # Output: (1, 'Task 2')
print(item2)  # Output: (2, 'Task 1')

########################################
# linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
