'''

This will consist the code related with generators
'''


# Concept structure for generators
class firstn:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.n:
            cur = self.num
            self.num += 1
            return cur
        else:
            raise StopIteration()


firstn_object = firstn(1000000)
print(sum(firstn_object))

'''
Get the sequence of number
'''


def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_of_first_n = sum(firstn(30))
