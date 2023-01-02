from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def add(pointer: Node, newValue):

    if pointer.next is None:
        q = Node(newValue)
        pointer.next = q
        return

    elif pointer.next.value >= newValue:
        q = Node(newValue, pointer.next)
        pointer.next = q
        return

    add(pointer.next, newValue)


def printList(g):

    g = g.next if g.value is None else g

    while g is not None:
        print(g.value)
        g = g.next


def reversed(pointer):

    if pointer.next is None:
        return pointer

    previous = reversed(pointer.next)
    q = previous
    while q.next is not None:
        q = q.next

    q.next = pointer
    pointer.next = None

    return previous


if __name__ == '__main__':

    g = Node(None)

    length = 10
    for i in range(length):
        add(g, randint(1, length))

    printList(g)
    print("---")

    g = Node(None, reversed(g.next))

    printList(g.next)

