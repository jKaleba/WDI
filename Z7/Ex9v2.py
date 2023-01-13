from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(p: Node):
    q = p

    def reverseR(pointer: Node, previous=None):

        nonlocal q

        if pointer.next is not None:
            reverseR(pointer.next, pointer)

        if pointer.next is None and previous is not None:

            if q == p:
                q = pointer

            previous.next = None
            pointer.next = previous

    reverseR(p)
    return q


def increment(pointer: Node):
    pointer = reverse(pointer)

    rest = 1
    current = pointer

    previous: Node

    while current is not None and rest == 1:
        current.value += 1
        rest = current.value // 10
        current.value %= 10

        previous = current
        current = current.next

    if rest == 1:
        new = Node(1)
        previous.next = new

    return reverse(pointer)


freeLine = lambda: print("-----")

if __name__ == '__main__':

    first = Node(1)
    current = first
    for i in range(20):
        next = Node(randint(0, 100))
        current.next = next
        current = current.next

    current = first

    while current is not None:
        print(current.value, end=" ")
        current = current.next
    print()

    freeLine()

    current = reverse(first)
    while current is not None:
        print(current.value, end=" ")
        current = current.next
