from random import randint
from math import log10


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(p):
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


def insert(p, n, rev=False):
    beginning = p

    while p.next.next is not None:

        if p.val % 10 == n // 10 ** (int(log10(n))):
            q = p.next.next.next
            counter = 2
            while q is not None:
                if n % 10 == q.val // 10 ** (int(log10(q.val))):
                    break
                counter += 1
                q = q.next

            new = Node(n)
            p.next, new.next = new, q
            return counter - 1
        else:
            p = p.next

    if not rev:
        return insert(reverse(beginning), n, True)

    return 0


if __name__ == '__main__':

    pt = Node(2023)

    curr = pt

    values = [31, 17, 703, 37, 707, 72, 29, 902]

    for i in values:
        curr.next = Node(i)
        curr = curr.next

    curr = pt
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    count = insert(pt, 303)

    curr = pt
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()
    print(count)
