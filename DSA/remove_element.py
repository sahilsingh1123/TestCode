print("find index of substring")
# haystack = "sutestsub"
haystack = "susubtestsub"
needle = "sub"
i, j = 0, 0
index = 0
continue_execution = True
while continue_execution:
    if needle[i] == haystack[j]:
        i += 1
        j += 1
        is_matched = True
    else:
        i = 0
        j += 1
        is_matched = False
    # if i != 0:
    #     j += 1
    if i - 1 == len(needle) - 1 and is_matched:
        index = j - len(needle)
        break


# palindrome
import re

s = "A man, a plan, a canal: Panama"
s = re.sub(r"[^A-Za-z0-9]", "", s)
s = s.strip().lower()
# v = s[::-1]
if s == s[::-1]:
    is_palindrone = True


# print("highest number count having half of the length")
nums = [0, 1, 2, 2, 3, 4, 5, 0, 3, 3, 3, 5, 1, 1, 1]
nums = [1, 2, 2, 3, 2, 5, 6]

candidate = None
count = 0

# Step 2: Iterate through the array
for num in nums:
    if count == 0:
        candidate = num
    count += 1 if num == candidate else -1


# remove the duplicate element
nums = [0, 1, 2, 2, 3, 4, 5, 0, 2]
val = 2
inside = 0
while val in nums:
    inside += 1
    nums.remove(val)


# remove duplicate elements from a list
nums = [0, 1, 2, 2, 3, 4, 5, 0, 2, 5]
# nums = [1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
total_idx = len(nums) - 1
i = 0
j = 1
inside = 0
while i < total_idx:
    inside += 1
    popped = False
    if nums[i] == nums[j]:
        nums.pop(j)
        total_idx = len(nums) - 1
        popped = True
    if j >= total_idx:
        i += 1
        j = i + 1
    elif not popped:
        j += 1

# answer by chat-gpt
for i in range(len(nums) - 1, -1, -1):
    if nums[i] in nums[:i]:
        nums.pop(i)


# find prefix
strs = ["flower", "flow", "flight"]
# strs = ["cap", "captain", "capital"]
# strs = ["ab", "a"]
first_word = strs[0]
max_prefix_index = len(first_word) - 1
prefix = ""
i = 0
while i <= max_prefix_index:
    is_matched = False
    for word in strs:
        if len(word) - 1 >= i:
            if first_word[i] == word[i]:
                is_matched = True
            else:
                is_matched = False
                break
        else:
            is_matched = False
            break
    if is_matched:
        prefix = prefix + word[i]
        i += 1
    else:
        break
