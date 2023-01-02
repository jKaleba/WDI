
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
    add(guardian, 7)

    printList(guardian)
    print("--")

    add(guardian, 3)
    printList(guardian)

    print(isIn(guardian, 5))

    delete(guardian, 7)
    printList(guardian)