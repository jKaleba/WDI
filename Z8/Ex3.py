
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def size(p):

    if p is None:
        return 0

    return 1 + size(p.left) + size(p.right)


if __name__ == '__main__':

    root = Node(1)

    left = Node(2)
    right = Node(3)

    root.left = left
    root.right = right

    print(size(root))


