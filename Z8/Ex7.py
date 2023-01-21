
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def oneKiddo(pointer: Node):

    def kiddoR(p: Node):
        if p.left != p.right:
            if p.left is None:
                return 1 + oneKiddo(p.right)
            elif p.right is None:
                return 1 + oneKiddo(p.left)

            return oneKiddo(p.left) + oneKiddo(p.right)

        return 0

    if pointer is not None:
        return kiddoR(pointer)

    return 0


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


    print(oneKiddo(root))
