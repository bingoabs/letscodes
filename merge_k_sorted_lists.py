# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# """
# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.
# """

class SolutionOne(object):

    def pop_min(self, lists):
        
        min_, index = 99999, 0

        for inx in range(len(lists)):
            value = lists[inx][0]

            if value < min_:
                index = inx
                min_ = value

        target = lists[index]

        left = target[1:]

        if left == []:
            lists = lists[0:index] + lists[index + 1:]
        else:
            lists[index] = left

        return min_, lists

    def mergeKLists(self, lists):
        lists = [self.to_list(l) for l in lists if l]
        length = len(lists)

        if length == 0: return lists
        if length == 1: return lists[0]

        r = []

        while lists:
            min_, lists = self.pop_min(lists)
            r.append(min_)

        return r

    def to_list(self, l):
        r = []
        while l:
            r.append(l.val)
            l = l.next
        return r

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def creat_node():
    l, ll, lll= ListNode(5), ListNode(2), ListNode(0)
    lll.next = ll
    ll.next = l

    return [lll]
"""
Also we can use one by one, or something, this one kind of slow,
because first change ListNode to list, so we can skip this step.
"""  

if __name__ == "__main__":
    lists = [[], []]
    s = Solution().mergeKLists(lists)
    print s









