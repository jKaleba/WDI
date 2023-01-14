import time
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


def add(p: Node, q: Node):
    p = reverse(p)
    q = reverse(q)

    guardian = Node(-1)
    current = guardian
    rest = 0
    while True:

        sum = Node(p.value + q.value + rest)
        rest = sum.value // 10
        sum.value %= 10

        current.next = sum
        current = current.next

        p = p.next
        q = q.next

        if p is None and q is None:
            break

        if p is None:
            p = Node(0)

        if q is None:
            q = Node(0)

    if rest > 0:
        sum = Node(rest)
        current.next = sum

    return reverse(guardian.next)


if __name__ == '__main__':

    freeLine = lambda: print("-----")

    first1 = Node(randint(1, 9))
    first2 = Node(randint(1, 9))
    current1 = first1
    current2 = first2
    for i in range(randint(5, 10)):
        next1 = Node(randint(0, 9))

        current1.next = next1
        current1 = current1.next

    for i in range(randint(5, 10)):
        next2 = Node(randint(0, 9))

        current2.next = next2
        current2 = current2.next

    current1 = first1
    current2 = first2
    while current1 is not None:
        print(current1.value, end=" ")
        current1 = current1.next
    print()

    while current2 is not None:
        print(current2.value, end=" ")
        current2 = current2.next
    print()

    freeLine()

    current3 = add(first1, first2)

    while current3 is not None:
        print(current3.value, end=" ")
        current3 = current3.next
    print()
