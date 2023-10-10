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
        # if t is an anagram of s, their length must be same
        if len(s) != len(t):
            return False

        # count the appearance of each letter in s
        count_s = {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        # check the letters in t
        for char in t:
            if char not in count_s:
                return  False
            count_s[char] -= 1
            if count_s[char] < 0:
                return False
            if count_s[char] == 0:
                count_s.pop(char)

        if len(count_s.keys()) == 0:
            return True
        
        return False
    

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    test = Solution()
    print(test.isAnagram(s,t))
    s = "rat"
    t = "car"
    print(test.isAnagram(s,t))