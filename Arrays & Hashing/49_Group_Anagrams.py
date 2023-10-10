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
        # using a dict to record the str as key and its anagram as value
        anagram_dict = {}

        # iterate through the strs list
        for str in strs:
            sorted_str = ''.join(sorted(str))

            # if the sorted_str exists in the anagram_dict, append its original str to the value
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(str)
            else:
                anagram_dict[sorted_str] = [str]

        res = list(anagram_dict.values())

        return res
    

if __name__ == "__main__":
    test = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(test.groupAnagrams(strs))