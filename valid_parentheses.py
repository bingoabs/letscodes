"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r, match = [], {"(": ")", "{": "}", "[": "]"}

        for i in s:
            last = r[-1] if r else None
            if i != match.get(last, None):
                r.append(i)
            else:
                r = r[:-1]
        return bool(r) == False





if __name__ == "__main__":
    a = "()"
    s = Solution().isValid(a)
    print(s)