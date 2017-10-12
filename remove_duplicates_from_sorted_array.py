"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length

Do not allocate extra space for another array, you must do this in place with constant memory

For example,
Given input array nums = [1, 1, 2]
Your function should return length = 2, with the first two elements of nums begin 1 and 2 respectively
It doesn't matter what you leave beyond the new length

So annoy 
After reading from comments I realized the question don't want us to remove elements from the list, but
to put non-duplicated list tin the beginning and return the size of it
And OJ doesn't care about the rest of the list.
"""


# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 0:return []

#         last, length= nums[0], nums[0:1]

#         for i in nums:
#             if i != last:
#                 last = i
#                 length.append(last)
#         return length


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:return 0

        r = nums[:]
        last, write = nums[0], 1
        for i in r:
            if i != last:
                nums[write] = last = i
                write += 1
        return write

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 0:return 0

#         last, indexs= nums[0], 0

#         for i in range(len(nums)):
#             c_word = nums[i]
#             if c_word != last:
#                 last = i
#                 indexs += i
#         return indexs


if __name__ == "__main__":
    nums = [1, 2]
    s = Solution().removeDuplicates(nums)
    print s


