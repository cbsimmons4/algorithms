# Given two values represented as linked links in reverse order,
# add the values and return a new linked list in reverse order
# containing the sum

class Node:
    def __init__ (self, val):
        self.val = val
        self.next = None
       
def addLinkedLists(listOne, listTwo):

    curNode = listOne
    valOne = 0
    multiplier = 1
    while (curNode is not None):
        valOne += (curNode.val * multiplier)
        multiplier = multiplier*10
        curNode = curNode.next

    curNode = listTwo
    valTwo = 0
    multiplier = 1
    while (curNode is not None):
        valTwo += curNode.val * multiplier
        multiplier = multiplier*10
        curNode = curNode.next

    totalVal = valOne + valTwo
    headListHead = Node(int(totalVal % 10))
    curNode = headListHead
    totalVal = int(totalVal / 10)
    while (totalVal > 0):
        curNode.next = Node(int(totalVal % 10))
        totalVal = int(totalVal / 10)
        curNode = curNode.next
    
    return headListHead


listOne = Node(8)
listOne.next = Node(3)
listOne.next.next = Node(2)

listTwo = Node(1)
listTwo.next = Node(0)
listTwo.next.next = Node(5)

newLinkHead = addLinkedLists(listOne,listTwo)

curNode = newLinkHead
while(curNode is not None):
    print(curNode.val)
    curNode = curNode.next

