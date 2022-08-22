#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None

'''
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        temp = head
        slow_p = temp
        fast_p = temp
        while (slow_p.next and fast_p.next and fast_p.next.next):

            # if ():
            #     return False
            # elif fast_p.next == None:
            #     return False
            # fast_p.next.next == None:
            #     return False
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False


        #code here


#{
# Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    #connects last node to node at position pos from begining.
    def loopHere(self,pos):
        if pos==0:
            return

        walk = self.head
        for i in range(1,pos):
            walk = walk.next

        self.tail.next = walk

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loopHere(int(input()))

        print(Solution().detectLoop(LL.head))
# } Driver Code Ends