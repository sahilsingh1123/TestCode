# sort the list and pick the last 3 element of the list
li = [89, 2, 76, 99, 1, 45]


class DoMergeSort:
    '''
    Divide the list in its single form
    once we got the single value in the list
    return that and merge it with the other list
    -> means do splitting on two list always and
        merge it once it reaches its leaf/bottom

    '''

    def mergeSort(self, array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = self.mergeSort(array[:mid])
        right = self.mergeSort(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        left_index = 0
        right_index = 0
        sorted_list = []

        while len(left) > left_index and len(right) > right_index:
            if left[left_index] < right[right_index]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1
        sorted_list.extend(left[left_index:])
        sorted_list.extend(right[right_index:])
        return sorted_list


# mergeList = DoMergeSort().mergeSort(li)

#######################################################################

# Binary search (Recursive)

class DoBinarySearch:
    '''
    perform Binary search on un-sorted list
    -> first of all sort the list
    -> split the list in half till we get the single element
    -> compare that single element with the provided value and return the success message
    '''
    value_to_search = 99

    def binarySearch(self, array):
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        if array[mid] == self.value_to_search:
            return print(f"found the value: {self.value_to_search}")
        elif array[mid] > self.value_to_search:
            self.binarySearch(array[:mid])
        else:
            self.binarySearch(array[mid:])

    def search(self, left, right):
        pass

# sorted_list = [1,2,45,76,89,90,92,94,96,97,99,101,125,140]
# output = DoBinarySearch().binarySearch(sorted_list)
