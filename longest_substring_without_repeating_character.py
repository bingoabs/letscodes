# -*- coding: utf-8 -*-
# @Author: bingo_zhou
# @Date:   2017-09-11 16:38:42
# @Last Modified by:   bingo_zhou
# @Last Modified time: 2017-09-11 16:39:11

"""
Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """