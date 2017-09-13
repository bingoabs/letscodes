"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example:

Input: "cbbd"
Output: "bb"

"""

class Solution(object):

    def get_longest_with_start(self, start, offset):
        letter = self.string[start]
        for i in range(start + 1, self.length):
            if self.string[i] == letter:
                if i - start > offset:
                    offset = i - start
                break

        return start, offset

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.string = s
        self.length = len(s)
        if self.length <= 1: return s
        start = 0
        offset = 0
        substring = ""
        while self.length - start > offset + 1:
            start, new_offset = self.get_longest_with_start(start, offset)
            if new_offset > offset:
                offset = new_offset
                substring = s[start:start + offset + 1]
                print("start: {}; offset: {}; substring: {}".format(start, offset, substring))
            start += 1

        return substring

if __name__ == "__main__":
    s = "badbsb"
    r = Solution().longestPalindrome(s)
    print r


