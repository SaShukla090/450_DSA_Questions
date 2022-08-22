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
def delete(head, i ):
    prev = None
    tmp = head
    count = 0
    while count<=i:
        if count == i:
            if prev == None:
                head = tmp.next
            elif tmp.next == None:
                prev.next = None
            else:
                prev.next = tmp.next
        prev = tmp
        tmp = tmp.next
        count +=1
    return head




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



    # else:q
    #     curr = head
    #     while curr.next is not None:
    #         curr = curr.next
    #     curr.next = newNode
    return head

def reverse(head, k):
    if k == 1:
        return head
    count = 0
    prev = None
    curr = head
    next = curr.next
    while True:
        if count<k and next is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        elif count == k:
            if next is not None:

                newHead = reverse(next, k)
                head.next = newHead
                return prev
                # break
            else:
                head.next = None
                return prev
            # count = 0

        else:
            head.next = None
            return prev





        # elif curr == None:
        #     return prev




################################# recusrive solutions ################

def insertR(head, i , data):
    if i == 0:
        new = Node(data)
        new.next = head
        return new
    if i<0:
        return head
    if head is None:
        return None
    # if head.next == None and (i-1) == 0:
    #     new = Node(data)
    #     head.next = new
    #     return new

    new = insertR(head.next, i -1, data)
    head.next = new

    return head




head = takeInput()
printLL(head)
# head = insert(head, 10, 10)
# head = delete(head, 5)
# insertR(head, 5, 100)
head = reverse(head, 6)
printLL(head)
# printLL(head.next)1

# print(LengthLL(head))
# print(LengthLL(head.next))
# print(printIthNode(head, 5))
# print(printIthNode(head.next, 5))