from random import randint


class Node:

    def __init__(self, index, value, next=None):
        self.index = index
        self.value = value
        self.next = next


def initialize(array: list):
    guardian = Node(None, None)
    currNode = guardian

    for i in range(len(array)):
        if array[i]:
            currNode.next = Node(i, array[i])
            currNode = currNode.next

    return guardian


def at(pointer: Node, index: int):

    curr = pointer.next if pointer.value is None else pointer
    while curr is not None:
        if curr.index == index:
            return curr.value


def set(pointer: Node, index, value):

    if pointer.next is None:
        q = Node(index, value)
        pointer.next = q
        return

    if pointer.next.index == index:
        pointer.next.value = value
        return

    elif pointer.next.index > index:
        q = Node(index, value, pointer.next)
        pointer.next = q
        return

    set(pointer.next, index, value)


def printList(g):

    g = g.next if g.value is None else g

    while g is not None:
        print(g.index, g.value)
        g = g.next


if __name__ == '__main__':

    mList = [None if randint(1, 100) % randint(1, 10) < 4 else randint(1, 100) for i in range(100)]

    print(mList)

    mGuard = initialize(mList)

    printList(mGuard)
    print("---")

    set(mGuard, 4, 4)
    printList(mGuard)
    print("---")

    set(mGuard, 0, 1)
    printList(mGuard)
