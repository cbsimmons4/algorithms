

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        cur = head
        while cur != None:
            if ( (cur.next != None) and cur.next.val == val):
                cur.next = cur.next.next
            else:
                cur = cur.next
        if head != None and head.val == val:
            head = head.next
        return head

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
mySolution = Solution()
head = ListNode(1,
ListNode(2,
ListNode(6,
ListNode(3,
ListNode(4,
ListNode(5,
ListNode(6,)))))))

head = mySolution.removeElements(head,67)

cur = head
while cur != None:
    print(cur.val)
    cur = cur.next

