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

    if pointer.next.value == newValue:
        return

    elif pointer.next.value > newValue:
        q = Node(newValue, pointer.next)
        pointer.next = q
        return

    add(pointer.next, newValue)


def isIn(g, value):

    if g.next is None:
        return False

    if g.next.value == value:
        return True

    elif g.next.value > value:
        return False

    return isIn(g.next, value)


def delete(g, value):

    if g.next is None:
        return

    if g.next.value == value:
        g.next = g.next.next

    elif g.next.value < value:
        delete(g.next, value)


def printList(g):

    while g is not None:
        print(g.value)
        g = g.next


if __name__ == '__main__':

    guardian = Node(0)
    for i in range(randint(5, 50)):

        newValue = randint(1, 100)
        add(guardian, newValue)

    printList(guardian)
    print("--")

    for i in range(randint(5, 20)):

        guess = randint(1, 100)
        if isIn(guardian, guess):
            print("Found in: ", guess)
            delete(guardian, guess)

    printList(guardian)
