"""
Implement strStr()
Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_length = len(needle)
        if n_length and len(haystack) >= n_length:
            index = 0
            while len(haystack[index:]) >= n_length:
                if needle == haystack[index:n_length + index]:
                    return index
                index += 1
            return -1
        elif len(haystack) < n_length:
            return -1
        else:
            return 0



if __name__ == "__main__":
    haystack, needle = "mississippi", "a"
    s = Solution().strStr(haystack, needle)
    print(s)

