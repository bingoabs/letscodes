# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""
class Solution(object):

    def find_min(self, lists):
        start, target_index = 99999, 0
        for index in range(len(lists)):
            value = lists[index].val
            if value != None and value < start:
                target_index = index
                start = value

        return start, target_index

    def delete_none(self, lists):
        return [l for l in lists if l]

    def to_node_lists(self, lists):
        return [self.to_node(l) for l in lists if l]

    def to_node(self, l):
        l.reverse()

        node = ListNode(l[0])

        for i in range(1, len(l)):
            new = ListNode(l[i])
            new.next = node
            node = new

        return node

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        raw = target = ListNode(0)
        lists = self.to_node_lists(lists)

        while any(lists):
            start, index = self.find_min(lists)
            new_target = ListNode(start)
            lists[index] = lists[index].next
            target.next = new_target
            lists = self.delete_none(lists)
        return raw.next

def test_to_node():
    l = [1, 2, 3, 4, 5]
    r = []
    for i in range(len(l)):
        r.append(l[i])
    print(r == l)
            

if __name__ == "__main__":
    test_to_node()