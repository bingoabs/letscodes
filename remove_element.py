"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3, 2, 2, 3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.

"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums[index:] = nums[index+1:]
            else:
                index += 1
        print(nums)
        return len(nums)


if __name__ == "__main__":
    nums, val = [3, 3], 3
    s = Solution()
    r = s.removeElement(nums, val)
    print(r)