
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def leaves(p: Node):

    if p is None:
        return 0

    currLeaves = leaves(p.left) + leaves(p.right)
    return currLeaves if currLeaves > 0 else 1


if __name__ == '__main__':

    root = Node(1)

    left = Node(2)
    right = Node(3)

    root.left = left
    root.right = right

    print(leaves(root))


