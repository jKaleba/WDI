from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def sieveList(pointer: Node):

    while pointer is not None and pointer.next is not None:
        if pointer.next.value < pointer.value:
            pointer.next = pointer.next.next

        else:
            pointer = pointer.next


if __name__ == '__main__':

    pt = Node(randint(0, 100))
    current = pt
    for i in range(100):
        current.next = Node(randint(0, 100))
        current = current.next

    current = pt
    while current is not None:
        print(current.value, end=" ")
        current = current.next
    print()

    sieveList(pt)

    current = pt
    while current is not None:
        print(current.value, end=" ")
        current = current.next
    print()
