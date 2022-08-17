class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# print(b)
#
# a =  Node(13)
# b = Node(15)
#
# a.next = b
#
# print(a.val)
# print(b.val)
# print(a.next.val)
# print(a)
# print(a.next)
# print(b.next.val)
def insert(head, i , data):
    count = 0
    prev = None
    tmp = head
    while count <= i:

        if count == i:
            newNode = Node(data)
            if prev == None:
                newNode.next = head
                head = newNode
            else:
                prev.next = newNode
                newNode.next = tmp
        prev = tmp
        tmp = tmp.next
        count += 1
    return head
def LengthLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def printIthNode(head, i):
    count = 0
    while head is not None:
        if count == i:
            print(head.val)
            break
        else:
            head = head.next
            count +=1

def printLL(head):
    temp = head
    while temp != None:
        print(str(temp.val) + "-->", end = "")
        temp = temp.next
    print(None)
def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    prev = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            prev = newNode

        else:
            prev.next = newNode
            prev = prev.next



    # else:
    #     curr = head
    #     while curr.next is not None:
    #         curr = curr.next
    #     curr.next = newNode
    return head


head = takeInput()
printLL(head)
head = insert(head, 10, 10)
printLL(head)
# printLL(head.next)1

# print(LengthLL(head))
# print(LengthLL(head.next))
# print(printIthNode(head, 5))
# print(printIthNode(head.next, 5))