from random import randint


class Node:

    def __init__(self, key, next=None):
        self.key = key
        self.next = next


def sieveListV6(pointer: Node):
    removedElements = 0

    while pointer is not None:
        q = pointer.next

        while q is not None and q.key == pointer.key:
            temporary = q.next
            q.next = None
            q = temporary

        pointer.next = q
        pointer = pointer.next


if __name__ == '__main__':

    freeLine = lambda: print("---")

    randRange = (1, 10)

    pt = Node(0)
    curr = pt
    for i in range(100):
        curr.next = Node(i)
        curr = curr.next
        curr.next = Node(i)
        curr = curr.next

    curr = pt
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next
    print()
    freeLine()

    sieveListV6(pt)

    curr = pt
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next
    print()
