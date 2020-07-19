# Python3 program to construct binary
# tree from given array in level
# order fashion Tree Node

# Helper function that allocates a
# new node
class Node:
    def __init__(self, data, level):
        self.data = data
        self.level = level
        self.left = self.right = None


def insertLevelOrder(arr, root, level, i, n):
    # Base case for recursion
    if i < n:
        temp = Node(arr[i],level)
        root = temp

        root.left = insertLevelOrder(arr, root.left, root.level + 1, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right, root.level + 1, 2 * i + 2, n)
        
    return root


def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 1, 0, n)
    inOrder(root)

