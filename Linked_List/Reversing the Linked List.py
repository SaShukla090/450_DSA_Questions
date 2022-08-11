class Node:
    #FUNCTION to inialize node object
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class Linkedlist:
    #Fucntion to Initialize the Linked
    #List object
    def __init__(self):
        self.head = None

    #Function to print contents of linked list
    # starting from head

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def ReverseList(self):
        prev = None
        current = self.head
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev




# Code Exectution starts here
if __name__ == "__main__":
    llist = Linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    four = Node(4)

    llist.head.next = second
    second.next = third
    third.next = four

    llist.printList()

    llist.ReverseList()
    llist.printList()