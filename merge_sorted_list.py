"""
Merge two sorted linked lists and return it as a new list 
The new list should be made by splicing together the nodes of the first two lists
"""

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
      self.val = x
      self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: Listnode
        """
        if l1 and l2:
          pass
        else:
          return []
        r = ListNode(None)
        rr = r
        while l1.val and l2.val:
          if l1.val > l2.val:
              r.next = ListNode(l1.val)
              l1 = l1.next
              r = r.next
          else:
            r.next = ListNode(l2.val)
            l2 = l2.next
            r = r.next
        while l2.val:
          r.next = ListNode(l2.val)
          l2 = l2.next
          r = r.next
        while l1.val:
          r.next = ListNode(l1.val)
          r = r.next
          l1 = l1.next
        return rr
        


if __name__ == "__main__":

    s = Solution().mergeTwoLists(l1, l2)