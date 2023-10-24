"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        str_map = {}
        res = []
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in str_map:
                str_map[sorted_str].append(str)
            else:
                str_map[sorted_str] = [str]
        
        res = list(str_map.values())

        return res
    

if __name__ == "__main__":
    test = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(test.groupAnagrams(strs))