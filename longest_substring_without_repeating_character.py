# -*- coding: utf-8 -*-
# @Author: bingo_zhou
# @Date:   2017-09-11 16:38:42
# @Last Modified by:   bingo_zhou
# @Last Modified time: 2017-09-12 11:04:06

"""
Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
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
        longest = ""
        for i in range(len(s)):
            new = self.get_start(s[i:])
            if len(new) > len(longest):
                longest = new
        return len(longest)

if __name__ == "__main__":
    string = "abcajserwera"
    r = Solution().lengthOfLongestSubstring(string)
    print r
