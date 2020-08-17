class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution: 
    def reverseLinked(self, head):
        if head == None: return None
        prev = head
        cur = head.next
        if cur != None:
            nextNode = head.next.next
        head.next = None
        while cur != None:
            cur.next = prev
            prev = cur
            cur = nextNode
            if nextNode != None:
                nextNode = nextNode.next
        head = prev
        return head

mySolition = Solution()

head = LinkedNode(1)
head.next = LinkedNode(2)
# head.next.next = LinkedNode(3)
# head.next.next.next = LinkedNode(4)

cur = head
while cur != None:
    print(cur.val)
    cur = cur.next

print("reversed")
head = mySolition.reverseLinked(head)

cur = head
while cur != None:
    print(cur.val)
    cur = cur.next

