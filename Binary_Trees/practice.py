class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)
btn4 = BinaryTreeNode(4)
btn5 = BinaryTreeNode(5)

btn1.left = btn2
btn1.right = btn3

btn2.left = btn4
btn2.right = btn5
# #
# print(btn1.left)
# print(btn1.right)

############ Printing the Tree ############

def printTree(root):
    if root == None:
        return
    print(root.data)

    ### check if root is leaf or not

    printTree(root.left)
    printTree(root.right)

# printTree(btn1)

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, end= ":")
    if root.left == None:
        print("L", None, end = ',')
    else:
        print("L", root.left.data, end = ',')

    if root.right == None:
        print("R", None)
    else:
        print("R", root.right.data)
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


# printTreeDetailed(btn1)

def height(root):
    if root == None:
        return 0
    hr = 1 + height(root.right)
    hl = 1 + height(root.left)
    if hr > hl:
        return hr
    else:
        return hl

print(height(btn1))