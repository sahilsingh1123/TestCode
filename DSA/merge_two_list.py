class Merge:

    def __init__(self):
        pass

    def merge_list(self, nums1, m, nums2, n):
        """
        m = size of nums1 and n = size of nums2 (eliminating 0 value)
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                try:
                    nums1[k] = nums1[i]
                except Exception as e:
                    nums1.insert(k, nums1[i])
                i -= 1
            else:
                try:
                    nums1[k] = nums2[j]
                except Exception as e:
                    nums1.insert(k, nums2[j])
                j -= 1
            k -= 1
        print(nums1)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 0, 0, 0, 0]
    m = 5
    nums2 = [3, 6, 7, 8]
    n = 4
    Merge().merge_list(nums1, m, nums2, n)
