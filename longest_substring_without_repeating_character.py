# -*- coding: utf-8 -*-
# @Author: bingo_zhou
# @Date:   2017-09-11 16:38:42
# @Last Modified by:   bingo_zhou
# @Last Modified time: 2017-09-12 12:24:14

"""
Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
from time import time

class Solution(object):
    def get_start(self, string):
        longest = ""
        l = list(string)
        while len(l) != len(set(l)):
            half = len(l)/2
            l = l[:half]
        if len(l) < len(string):
            for i in range(len(l), len(string)):
                if len(string[:i]) == len(set(string[:i])):
                    continue
                return string[:i-1]
        return l

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1 or len(set(s)) == 1:
            return 1

        end = s[-1]
        while end == s[0] and len(s) > 1:
            s = s[:-1]
        split = s[0]
        substrings = s.split(split)
        substrings = [split + el for el in substrings if el]
        substrings = list(set(substrings))
        longest = 0
        for i in substrings:
            if len(i) == len(set(i)):
                longest = len(i)

        for i in substrings:
            if len(i) > longest:
                for j in range(len(i)):
                    new = self.get_start(i[j:])
                    if len(new) > longest:
                        longest = len(new)
        return longest

if __name__ == "__main__":
    string = 'werhwqker'
    
    a = time()
    r = Solution().lengthOfLongestSubstring(string)
    print r
    b = time() - a 
    print b
