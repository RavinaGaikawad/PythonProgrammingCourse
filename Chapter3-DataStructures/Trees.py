class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def PreorderTraversal(root):
    res = []
    if root:
        res.append(root.val)
        res = res + PreorderTraversal(root.left)
        res = res + PreorderTraversal(root.right)
    return res

def inorderTraversal(root):
    res = []
    if root:
        res = inorderTraversal(root.left)
        res.append(root.val)
        res = res + inorderTraversal(root.right)
    return res

def PostorderTraversal(root):
    res = []
    if root:
        res = PostorderTraversal(root.left)
        res = res + PostorderTraversal(root.right)
        res.append(root.val)
    return res


root = Node(10)
root.left = Node(5)
root.right = Node(15)

print('PreorderTraversal', PreorderTraversal(root))
print('InorderTraversal', inorderTraversal(root))
print('PostorderTraversal', PostorderTraversal(root))

