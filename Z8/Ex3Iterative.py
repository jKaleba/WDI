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


def arrSize(arr: list):

    i = 0
    while i < len(arr) and arr[i] is not None:
        i += 1

    return i - 1


def size(pointer: Node):

    arr = [pointer]
    entireSize = 1
    index = 1 if arr[0] is not None else 0

    while index != 0:

        new_arr = [None for _ in range(2 * index)]
        index = 0
        for i in range(len(arr)):
            if arr[i] is None:
                break

            if arr[i].left is not None:
                new_arr[index] = arr[i].left
                index += 1

            if arr[i].right is not None:
                new_arr[index] = arr[i].right
                index += 1

        entireSize += index
        arr = new_arr

    return entireSize


if __name__ == '__main__':
    root = Node(1)
    expandTree(root, 16)

    root.right.left = None

    print(size(root))
