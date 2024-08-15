class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printList(self, head=None):
        res = []
        while head != None:
            res.append(head.val)
            head = head.next
        print(res)

class Solution(object):
    def mergeKLists(self, lists):
        def check(lists):
            for list in lists:
                if list != None:
                    return True
            return False
        head = ListNode()
        curr_P = head
        while check(lists):
            curr_min = 10001
            for i in range(len(lists)):
                if lists[i] != None:
                    curr_min = min(curr_min, lists[i].val)
            for i in range(len(lists)):
                if lists[i] != None and lists[i].val == curr_min:
                    curr_P.next = ListNode(val=curr_min)
                    curr_P = curr_P.next
                    lists[i] = lists[i].next
        return head.next

lists_1 = []
# [1,4,5]
head_1 = ListNode(1)
head_1.next = ListNode(4)
head_1.next.next = ListNode(5)
lists_1.append(head_1)
# [1,3,4]
head_2 = ListNode(1)
head_2.next = ListNode(3)
head_2.next.next = ListNode(4)
lists_1.append(head_2)
# [2,6]
head_3 = ListNode(2)
head_3.next = ListNode(6)
lists_1.append(head_3)

lists_2 = []

lists_3 = [None]

ListNode().printList((Solution().mergeKLists(lists=lists_1)))