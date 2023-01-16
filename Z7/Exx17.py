from random import randint


class Node:

    def __init__(self, key, previous=None, next=None):
        self.key = key
        self.previous = previous
        self.next = next


def onesInBinary(n):
    counter = 0
    while n > 0:
        if n % 2 == 1:
            counter += 1

        n //= 2

    return counter


def sieveListV4(pointer: Node) -> Node:

    while pointer is not None and onesInBinary(pointer.key) % 2 == 1:
        pointer = pointer.next
        pointer.previous = None

    current = pointer

    while current is not None:
        if onesInBinary(current.key) % 2 == 1:

            temporary = current
            current = current.next

            temporary.previous.next = temporary.next

            if temporary.next is not None:
                temporary.next.previous = temporary.previous

            temporary.previous = temporary.next = None

        else:
            current = current.next

    return pointer


if __name__ == '__main__':

    freeLine = lambda: print("---")

    pt = Node(randint(1, 10))
    curr = pt
    for i in range(100):
        curr.next = Node(randint(1, 10), curr)
        curr = curr.next

    curr = pt
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next
    print()
    freeLine()

    pt = sieveListV4(pt)

    curr = pt
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next
    print()
