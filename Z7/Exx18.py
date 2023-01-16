from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def onesInBinary(n):
    counter = 0
    while n > 0:
        if n % 2 == 1:
            counter += 1

        n //= 2

    return counter


def sieveListV5(pointer: Node):

    current = pointer
    while current is not None:

        q = current.next
        previous = current
        while q is not None:
            if q.value == current.value:
                previous.next = q.next
                q.next = None
                q = previous.next

            else:
                previous = q
                q = q.next

        current = current.next


if __name__ == '__main__':

    freeLine = lambda: print("---")

    randRange = (1, 10)

    pt = Node(randint(randRange[0], randRange[1]))
    curr = pt
    for i in range(100):
        curr.next = Node(randint(randRange[0], randRange[1]))
        curr = curr.next

    curr = pt
    while curr is not None:
        print(curr.value, end=" ")
        curr = curr.next
    print()
    freeLine()

    sieveListV5(pt)

    curr = pt
    while curr is not None:
        print(curr.value, end=" ")
        curr = curr.next
    print()
