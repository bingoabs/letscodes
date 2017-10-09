"""
Implement atoi to convert a string to an integer
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str:str
        :rtype: int
        """
        str = str.strip()
        length = len(str)
        if length == 0: return 0
        start = str[0]
        if start == "+":
            return int(str[1:])
        elif start == "-":
            return int(str[1:]) * -1
        else:
            return int(str)

if __name__ == "__main__":
    pass
