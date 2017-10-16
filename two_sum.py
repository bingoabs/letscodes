# -*- coding: utf-8 -*-
# @Author: bingokarl
# @Date:   2017-09-11 14:16:43
# @Last Modified by:   bingokarl
# @Last Modified time: 2017-09-11 14:39:10
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :typ taget: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None 

    def two(self, nums, target):
        for i in range(len(nums) - 1):
            if (target - i) in nums:
                return [i, target-i]
        return None
if __name__ == "__main__":
    nums = [2, 3, 4]
    target = 6
    r = Solution().twoSum(nums, target)
    print r
