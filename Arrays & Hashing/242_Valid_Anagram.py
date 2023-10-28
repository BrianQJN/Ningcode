"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :time complexity:
            iterate through s: O(n)
            iterate through t: O(n)
            total: O(n)
        :space complexity:
            dict: O(n)
            total: O(n)
        """
        # initialize a dict to record the frequency of each letter
        char_freq = {}

        # if len of s and t is not equal, return False
        if len(s) != len(t):
            return False
        
        # iterate through s
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # iterate through t
        for char in t:
            if char not in char_freq:
                return False
            char_freq[char] -= 1
            if char_freq[char] == 0:
                char_freq.pop(char)
        
        return len(char_freq.keys()) == 0

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    test = Solution()
    print(test.isAnagram(s,t))
    s = "rat"
    t = "car"
    print(test.isAnagram(s,t))