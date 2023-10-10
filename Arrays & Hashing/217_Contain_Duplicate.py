"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # using the set to record the appearance of num
        numset = set()
        # iterate through the nums array
        # if it is in the set, means there is a duplicate, return True
        for num in nums:
            if num in numset:
                return True
            numset.add(num)
            

if __name__ == "__main__":
    nums = [1,2,3,1]
    result = Solution().containsDuplicate(nums)
    print(result)