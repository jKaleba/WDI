class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def removeNodes(pointer: Node, n=0, lvl=0):
    if pointer is None:
        return

    removeNodes(pointer.left, n, lvl + 1)
    removeNodes(pointer.right, n, lvl + 1)

    if lvl >= n:
        pointer.left = pointer.right = None


def expandTree(pointer: Node, n, i=1):
    if i > n // 2:
        return

    if pointer is not None:

        pointer.left = Node(2 * i)
        if 2 * i + 1 <= n:
            pointer.right = Node(2 * i + 1)

        expandTree(pointer.left, n, 2 * i)
        expandTree(pointer.right, n, 2 * i + 1)

    else:
        pointer = Node(1)
        expandTree(pointer, n)


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
    expandTree(root, 10)
    printTree(root)
    removeNodes(root, 2)

    print("---")

    printTree(root)