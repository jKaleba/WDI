from random import randint


class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = None
from random import randint
from math import isqrt


class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = None


def reversedList(p: Node):
    q = p

    def reversedR(pointer: Node, previous=None):

        nonlocal q

        if pointer.next is not None:
            reversedR(pointer.next, pointer)

        if pointer.next is None and previous is not None:
            if q == p:
                q = pointer

            previous.next = None
            pointer.next = previous

    reversedR(p)

    return q


def repair(pointer: Node, divisor=1):
    beginning = pointer

    NWD = lambda a, b: NWD(b, a % b) if b else a
    quotient = pointer.next.val / pointer.val

    signChange = False

    while pointer.next is not None:

        currQ = pointer.next.val / pointer.val

        if 0 < currQ % 1 < 1:
            return repair(reversedList(pointer))

        quotient = NWD(quotient, currQ)

        if currQ < 0:
            signChange = True
            quotient = isqrt(quotient)

        pointer = pointer.next

    pointer = beginning
    newElements = 0

    while pointer.next is not None:
        if pointer.next.val // pointer.val != quotient:

            newNode = Node(int(pointer.val * quotient)) if quotient % 1 == 0 else Node(pointer.val * quotient)
            newNode.next, pointer.next = pointer.next, newNode
            newElements += 1

        else:
            pointer = pointer.next

    return newElements


if __name__ == '__main__':

    asd = 0

    randRange = (1, 5, 1)

    pt = Node(64)
    curr = pt

    new = Node(32)
    curr.next = new
    curr = curr.next

    new = Node(8)
    curr.next = new
    curr = curr.next

    new = Node(2)
    curr.next = new
    curr = curr.next

    curr = pt
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    elements = repair(pt)

    print(elements)


def reversedList(pointer: Node):
    return pointer


def repair(pointer: Node, divisor=1):
    beginning = pointer

    NWD = lambda a, b: NWD(b, a % b) if b else a
    quotient = pointer.next.val / pointer.val

    signChange = False

    while pointer.next is not None:

        currQ = pointer.next.val / pointer.val

        if 0 < currQ % 1 < 1:
            return repair(reversedList(pointer), 1 // currQ)

        quotient = NWD(quotient, currQ)

        if currQ < 0:
            signChange = True
            quotient = quotient // 2

        pointer = pointer.next

    pointer = beginning
    newElements = 0

    while pointer.next is not None:
        if pointer.next.val // pointer.val != quotient:

            newNode = Node(int(pointer.val * quotient)) if quotient % 1 == 0 else Node(pointer.val * quotient)
            newNode.next, pointer.next = pointer.next, newNode
            newElements += 1

        else:
            pointer = pointer.next

    return newElements


if __name__ == '__main__':

    asd = 0

    randRange = (1, 5, 1)

    pt = Node(1)
    curr = pt

    new = Node(2 ** 2)
    curr.next = new
    curr = curr.next

    new = Node(2 ** 3)
    curr.next = new
    curr = curr.next

    new = Node(2 ** 5)
    curr.next = new
    curr = curr.next

    new = Node(2 ** 6)
    curr.next = new
    curr = curr.next

    curr = pt
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    elements = repair(pt, True)

    curr = pt
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    print(elements)
