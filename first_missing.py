class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = 1
        last = None
        for num in nums:
            if last == None:
                last = num
                target = num + 1
                continue
            if num == target:
                target += 1
            else:
                break
        return target


