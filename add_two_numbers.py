# -*- coding: utf-8 -*-
# @Author: bingokarl
# @Date:   2017-09-11 14:39:57
# @Last Modified by:   bingokarl
# @Last Modified time: 2017-09-11 16:18:32

"""
You are given wto non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, ecvept the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x 
        self.next = None


class Solution(object):

    def get_list(self, listnode):
        l = []
        while listnode:
            l.append(listnode.val)
            listnode = listnode.next
        return l

    def combine(self, l1, l2):
        r = []
        for i in range(len(l1)):
            ri = l1[i] + l2[i]
            r.append(ri)
        return r

    def to_digit_list(self, r):
        state = 0
        for i in range(len(r)):
            new = r[i] + state
            if new >= 10:
                r[i] = new - 10
                state = 1
            else:
                r[i] = new
                state = 0
        if state >= 1:
            r.append(state)
        return r


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtypy: ListNode
        """
        l1 = self.get_list(l1)
        l2 = self.get_list(l2)
        left = len(l1) - len(l2)
        if left > 0:
            index = len(l2)
            left = l1[index:]
        elif left < 0:
            index = len(l1)
            left = l2[index:]
        else:
            index = len(l2)
            left = []

        r = self.combine(l1[:index], l2[:index])
        r = r + left if left else r
        r = self.to_digit_list(r)

        return r

def CreateListNode(*l):
    r = [ListNode(e) for e in l]
    for i in range(len(r) - 1):
        r[i].next = r[i + 1]
    return r[0]

if __name__ == "__main__":
    l1 = CreateListNode(2, 4, 3)
    l2 = CreateListNode(5, 6, 4)
    print(Solution().get_list(l1))
    print(Solution().get_list(l2))

    r = Solution().addTwoNumbers(l1, l2)
    print(r)
