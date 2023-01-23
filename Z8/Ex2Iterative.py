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


def noneArray(arr: list):
    for i in range(len(arr)):
        if arr[i] is not None:
            return False
    return True


def find(pointer: Node, value):
    arr = [pointer]
    lv = 1

    while not noneArray(arr):

        new_arr = [None for i in range(2 ** lv)]
        for i in range(len(arr)):

            if arr[i] is None:
                continue

            if arr[i].val == value:
                return True

            new_arr[2 * i] = arr[i].left
            new_arr[2 * i + 1] = arr[i].right

        arr = new_arr
        lv += 1

    return False


if __name__ == '__main__':
    root = Node(1)
    expandTree(root, 16)


    print(find(root, 16))
