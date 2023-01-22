class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


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


def nodes(pointer: Node, lv, n=1):
    if pointer is None:
        return 0

    if n == lv:
        return 1

    return nodes(pointer.left, lv, n + 1) + nodes(pointer.right, lv, n + 1)


if __name__ == '__main__':

    root = Node(1)
    expandTree(root, 16)

    for i in range(1, 6):
        print(nodes(root, i))
