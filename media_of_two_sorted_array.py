# -*- coding: utf-8 -*-
# @Author: bingo_zhou
# @Date:   2017-09-12 14:17:19
# @Last Modified by:   bingo_zhou
# @Last Modified time: 2017-09-12 14:32:44
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log(m+n)).

Example 1: 

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        print("len1: {}; len2: {}".format(len1, len2))
        sorted_all = []
        i, j = 0, 0
        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                sorted_all.append(nums1[i])
                i += 1
            else:
                sorted_all.append(nums2[j])
                j += 1
        print("i: {}; j: {}".format(i, j))
        if i == len1 and j == len2:
            sorted_all = sorted_all
        elif i == len1:
            sorted_all = sorted_all + nums2[j:]
        else:
            sorted_all = sorted_all + nums1[i:]
        len3 = len(sorted_all)
        if len3/2 * 2 == len3:
            return (sorted_all[len3/2] + sorted_all[len3/2 - 1])/2.0
        else:
            return sorted_all[len3/2]

if __name__ == "__main__":
    #  1 3 2 3 4 1
    a = [1, 2, 4, 9]
    b = [3, 9, 12, 13, 20]
    c = Solution().findMedianSortedArrays(a, b)
    print c
