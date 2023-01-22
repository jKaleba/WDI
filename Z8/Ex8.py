class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def removeNodes(pointer: Node):

    def removeR(p: Node):
        if p is None:
            return

        removeNodes(p.left)
        removeNodes(p.right)

        p.left = p.right = None
        return

    if pointer is not None:
        removeR(pointer)

    # I have no idea whether the root should have been left or not, so I just assume it should




if __name__ == '__main__':

    root = Node(1)

    left = Node(2)
    right = Node(3)
    root.left = left
    root.right = right

    left = root.left
    right = root.right

    left.left = Node(4)
    right.right = Node(5)

    left = left.left
    right = right.right

    left.left = Node(6)
    right.right = Node(7)

    removeNodes(root)

    print(root)
