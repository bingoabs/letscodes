class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        r = list(str(x))
        r.reverse()
        t = "".join(r)
        if int(t) == x:
            return True
        else: 
            return False
