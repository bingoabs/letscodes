class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # init, length = 0, len(strs)

        smallest = min(strs, key=lambda str: len(str))

        if smallest == "":
            return ""

        index = last = len(smallest)
        isCommonPrefix = False
        target = ""

        while isCommonPrefix != :
            isCommonPrefix = self.isCommonPrefix(smallest, strs)
            target = smallest
            next_index = ""

    def isCommonPrefix(self, target, strs):
        r = True
        for str_ in strs:
            if str_.startswith(target) == False:
                r = False
                break
        return r




if __name__ == "__main__":
    pass