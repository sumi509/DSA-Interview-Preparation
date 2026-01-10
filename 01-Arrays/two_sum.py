"""
Problem: Two Sum (LeetCode #1)

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Approach:
Use a hash map to store numbers and their indices.
For each element, check if (target - current number) exists in map.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# Example
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]
