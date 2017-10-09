class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # init, length = 0, len(strs)

        sets = list(set(strs))
        if len(sets) == 0: return ""
        if len(sets) == 1: return sets[0]

        smallest = min(strs, key=lambda string: len(string))
        if smallest == "":
            return ""

        start, end, index = 0, len(smallest), 0

        target, isCommonPrefix = "", True
        while self.isCommonPrefix(smallest[start:index], strs) and index <= end:
            target = smallest[start:index]
            index += 1

        return target

    def isCommonPrefix(self, target, strs):
        r = True
        for str_ in strs:
            if str_.startswith(target) == False:
                r = False
                break
        return r




if __name__ == "__main__":
    inp = ["a", "b"]
    r = Solution().longestCommonPrefix(inp)
    print(r)