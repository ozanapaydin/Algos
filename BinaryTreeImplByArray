from queue import Queue


class Node:
    def __init__(self, data, level):
        self.data = data
        self.level = level
        self.left = None
        self.right = None


def create_tree(indexes):
    root_queue = Queue()
    root_top = Node(indexes.pop(0), 1)
    root_queue.put(root_top)

    while len(indexes) > 0:
        left_data = indexes.pop(0)
        right_data = indexes.pop(0)
        root_current = root_queue.get()

        if left_data != -1:
            left_node = Node(left_data, root_current.level + 1)
            root_current.left = left_node
            root_queue.put(left_node)
        if right_data != -1:
            right_node = Node(right_data, root_current.level + 1)
            root_current.right = right_node
            root_queue.put(right_node)
    return root_top


if __name__ == '__main__':

    n = int(input())

    indexes = [1]

    for _ in range(n):
        n1, n2 = map(int, input().split())
        indexes.append(n1)
        indexes.append(n2)

    root_top = create_tree(indexes)
    print(root_top)
