#/usr/bin/env python

# Regular Expression Matching

"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char*p)

Some examples:
isMatch('aa', 'a') -> false
isMatch('aa', 'aa') -> true
isMatch('aaa', 'aa') -> false
isMatch('aa', 'a*') -> true
isMatch('aa', '.*') -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true
"""
import logging

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if ".*" in p or s in p: return True 

        if len(s) == 0: return True
        if len(p) == 0: return False

        start = s[0]

        for i in range(len(p)):
            if p[i] in [start, "."]:
                is_match = self.check(s, p[i:])
                if is_match: return True
        return False

    def check(self, s, p):
        print(" s: {}; p: {}".format(s, p))
        if len(s) == 0: return True
        if len(p) == 0: return False

        if "*" in p:
            pre, last = p.split("*", 1)
            if self.same(pre, s[:len(pre)]):
                return False
            left = self.subtract(s[len(pre):], pre[-1])
            return self.check(left, last)
        else:
            pass

    def subtract(self, subtracted, substraction):
        for i in range(len(subtracted)):
            if subtracted[i] != substraction:
                break
        return subtracted[i:]


    def same(self, expression, string):
        for index in range(len(expression)):
            if expression[index] != string[index] and expression[index] != ".":
                return False
        return True

        


if __name__ == "__main__":
    s, p = "aa", "a*"
    s = Solution().isMatch(s, p)
    print(s)


