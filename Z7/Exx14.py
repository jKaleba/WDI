from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def sieveListV2(pointer: Node) -> Node:
    q = pointer

    while pointer is not None and pointer.next is not None and pointer.next.value % pointer.value == 0:
        q = pointer
        pointer = pointer.next
        q.next = None

    while pointer is not None and pointer.next and pointer.next.next is not None:
        if pointer.next.next.value % pointer.next.value == 0:
            pointer.next = pointer.next.next
            sieveListV2(q)
        else:
            pointer = pointer.next

    return q


if __name__ == '__main__':

    freeLine = lambda: print("---")

    pt = Node(randint(1, 10))
    current = pt
    for i in range(100):
        current.next = Node(randint(1, 10))
        current = current.next

    current = pt
    while current is not None:
        print(current.value, end=" ")
        current = current.next
    print()
    freeLine()

    pt = sieveListV2(pt)

    current = pt
    while current is not None:
        print(current.value, end=" ")
        current = current.next
    print()
