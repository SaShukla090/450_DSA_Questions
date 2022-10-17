#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def reverse(self, head):
        prev = None
        tmp = head
        while True:
            next = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = next
            if tmp == None:
                return prev

    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):

        first = self.reverse(first)
        second = self.reverse(second)
        N1 = 0
        prev_f = None
        tmp_f = first
        cf=0
        while True:
            next = tmp_f.next
            N1 = N1 + tmp_f.data
            cf += 1

            prev_f = tmp_f
            tmp_f = next

            if tmp_f == None:
                break

        prev_s = None
        tmp_s = second
        cs=0
        N2 = 0
        while True:
            next = tmp_s.next
            N2 = N2 + tmp_s.data
            cs += 1

            prev_s = tmp_s
            tmp_s = next

            if tmp_s == None:
                break

        ANS = N1 + N2

        if N1>N2:
            head = first
        else:
            head = second

        prev = None
        tmp = head

        while True:
            next = tmp.next
            if next == None:
                tmp.data = ANS
                break

            else:
                d = ANS%10
                # print(d)
                ANS = ANS//10
                tmp.data = d

        head = self.reverse(head)
        return head





















        # prev_f = None
        # prev_s = None
        # tmp_f = first
        # tmp_s = second
        # ans = []
        # carry = 0
        # while True:
        #     next_f = tmp_f.next
        #     next_s = tmp_s.next

        #     A = tmp_f.data + tmp_s.data + carry
        #     if next_f == None and next_s == None:
        #         ans.append(A)
        #     else:
        #         ans.append(A%10)
        #         carry = A//10

        #     prev_f = tmp_f
        #     prev_s = tmp_s
        #     tmp_f = next_f
        #     tmp_s = next_s
        #     if tmp_s or tmp_f:
        #         break

        # if tmp_s is not None:
        #     while True:
        #         next_s = tmp_s.next
        #         A = tmp_s.data + carry
        #         if next_f == None:
        #             ans.append(A)
        #         else:
        #             ans.append(A%10)
        #             carry = A//10
        #         prev_s = tmp_s
        #         tmp_s = next_s
        #         if tmp_s:
        #             head = second
        #             break

        # if tmp_f is not None:
        #     while True:
        #         next_f = tmp_f.next
        #         A = tmp_f.data + carry
        #         if next_f == None:
        #             ans.append(A)
        #         else:
        #             ans.append(A%10)
        #             carry = A//10
        #         prev_s = tmp_s
        #         tmp_s = next_s
        #         if tmp_f:
        #             head = first
        #             break
        # prev = None
        # tmp = head
        # count = 0
        # while True:

        #     next = tmp.next
        #     tmp.data = ans[count]
        #     count += 1
        #     prev = tmp
        #     tmp = next
        #     if tmp == None:
        #         break
        # head = self.reverse(head)
        # return head
















        # code here
        # return head of sum list


#{
# Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
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

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):

        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)

        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)

        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends