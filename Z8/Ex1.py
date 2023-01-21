
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def printTree(pointer: Node):


    def printR(p: Node):

        print(p.val)
        if p.left is not None:
            printR(p.left)

        if p.right is not None:
            printR(p.right)

    if pointer is not None:
        printR(pointer)


if __name__ == '__main__':

    root = Node(1)

    left = Node(2)
    right = Node(3)

    root.left = left
    root.right = right

    printTree(root)


