"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        :time complexity:
            update left products use O(n)
            update right products use O(n)
            form result use O(n)
            total: O(n)
        :space complextiy:
            two product lists use O(n)
            res use O(n)
            total: O(n)
        """
        # Step 1: Initialize two arrays to record the left and right side product in each position
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n

        # Step 2: Iterate through the nums and update the two arrays
        product_left = 1
        for i in range(n):
            left_product[i] = product_left
            product_left *= nums[i]

        product_right = 1
        for i in range(n - 1, -1, -1):
            right_product[i] = product_right
            product_right *= nums[i]

        # Step 3: The result in each position is left[i] * right[i]
        res = [left_product[i] * right_product[i] for i in range(n)]

        # Step 4: Return the result
        return res
    

if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3,4]
    print(test.productExceptSelf(nums))
    nums = [-1,1,0,-3,3]
    print(test.productExceptSelf(nums))
    