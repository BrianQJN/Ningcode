"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Evaluate the top-k-frequent element in the array

        :param nums: list[int]
        :param k: int
        :return: list[int]

        
        """
        # Step 1: Create a frequency map using Counter
        num_freqs = Counter(nums)

        # Step 2: Create a min heapq and then add elements to it based on the frequency
        min_heap = []
        for num, freq in num_freqs.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Step 3: Pop the elements from the heapq and form the result
        res = [num for freq, num in min_heap]

        # Step 4: Reverse the result to get the descending order result and return it
        res.reverse()

        return res
    

if __name__ == "__main__":
    test = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(test.topKFrequent(nums,k))