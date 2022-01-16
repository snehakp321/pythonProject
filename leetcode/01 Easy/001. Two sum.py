# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 1
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 1
# Input: nums = [3,3], target = 6
# Output: [0,1]

def bruteforcemethod(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9
print(bruteforcemethod(nums, target))
# time complexity of the above solution is O(n2)

def twopasshashtablemethod(nums,target):
    hash_table={}
    for i in range(len(nums)):
        complement = target-nums[i]
        if complement not in hash_table:
            hash_table[nums[i]] = i
        else:
            return [hash_table[complement], i]

nums = [2, 7, 11, 15]
target = 9
print(twopasshashtablemethod(nums, target))


