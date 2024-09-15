# Definition for a Node.
class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def printList(self):
        node = self
        while node != None:
            print(node.val, end=' ')
            node = node.next

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # level by level
        def step(node):
            curr, last = node, None
            while curr != None:
                next = curr.next
                if curr.child != None:
                    childLast = step(curr.child)
                    curr.next = curr.child
                    curr.child.prev = curr
                    if next != None:
                        childLast.next = next
                        next.prev = childLast
                    curr.child = None
                    last = childLast
                else:
                    last = curr
                curr = next
            return last
        step(head)
        return head
    
    # wrong answer - missing last part
    def flatten2(self, head):
        def step(currNode, prevNode):
            if currNode.child != None:
                currNode.child.prev = currNode
                if currNode.next != None:
                    currNode.next = step(currNode.child, currNode.next)
                else:
                    currNode.next = step(currNode.child, prevNode)
                currNode.child = None
            elif currNode.next != None:
                currNode.next = step(currNode.next, prevNode)
            elif prevNode != None:
                currNode.next = prevNode
                prevNode.prev = currNode
            return currNode
        if head != None:
            step(head, None)
        return head
'''
[1, 2, 3, 4, 5, null, null, null, 6, 7, null, null, 8, 9]
1---2---3---4---5---NULL
        |
        6---7---8---NULL
            |
            9--10--NULL
'''
node1, node2, node3, node4, node5, node6, node7, node8, node9, node10 = \
Node(val=1), Node(val=2), Node(val=3), Node(val=4), Node(val=5), Node(val=6), Node(val=7), Node(val=8), Node(val=9), Node(val=10)
node1.next = node2
node2.prev, node2.next = node1, node3
node3.prev, node3.next, node3.child = node2, node4, node6
node4.prev, node4.next = node3, node5
node5.prev = node4
node6.next = node7
node7.prev, node7.next, node7.child = node6, node8, node9
node8.prev = node7
node9.next = node10
node10.prev = node9
node1 = Solution().flatten(node1)
node1.printList()