 
def two_sum (nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target -num
        if complement in num_indices:
            return [num_indices[complement],i]
        num_indices[num] = i
    return None

print(two_sum([2,7, 11, 15], 9))
print(two_sum([2,7, 11, 15], 18))
print(two_sum([2,7, 11, 15], 26))