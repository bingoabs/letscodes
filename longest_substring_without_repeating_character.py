# -*- coding: utf-8 -*-
# @Author: bingo_zhou
# @Date:   2017-09-11 16:38:42
# @Last Modified by:   bingo_zhou
# @Last Modified time: 2017-09-12 14:16:26

"""
Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
from time import time

class Solution(object):

    def get_max(self, string, longest):
        index = longest
        if index >= len(string):
            return index

        i = 1
        while index + i <= len(string):
            if len(list(string[:index + i ])) == len(set(string[:index + i ])):
                i += 1
                continue
            break
        return index + i - 1

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        if len(s) == 1 or len(set(s)) == 1: return 1

        sets = list(set(s))
        split = sets[0]
        while split == s[-1] and len(s) > 1:
            split = sets[1]

        # to get more convienient substring length to small the count amount
        """
        Note here, we can provided more wayt to choose many split element to
        get the longest number used to check out the longest substring detailed

        Due to the sort of checking the string,
        we can depend on struct like Plug to make the all functions work like a 
        flow ...
        """
        split = s[0]
        substrings = s.split(split)
        substrings = [split + el for el in substrings if el]
        substrings = list(set(substrings))
        longest = 0
        for i in substrings:
            if len(i) == len(set(i)):
                longest = len(i)
        # print("{}, {}".format(longest, substrings))

        for j in range(len(s)):
            new = self.get_max(s[j:], longest)

            if new > longest:
                longest = new
        return longest

if __name__ == "__main__":
    string = "aaca"
    
    a = time()
    r = Solution().lengthOfLongestSubstring(string)
    print r
    b = time() - a 
    print b
