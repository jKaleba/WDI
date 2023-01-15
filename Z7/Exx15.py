from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def onesMoreThanTwos(n):
    counter1 = 0
    counter2 = 0
    while n > 0:

        if n % 3 == 1:
            counter1 += 1
        elif n % 3 == 2:
            counter2 += 1

        n /= 3

    return counter1 > counter2



def sieveListV3(pointer: Node) -> Node:

    while onesMoreThanTwos(pointer.value):
        pointer = pointer.next

    q = pointer

    while pointer is not None and pointer.next is not None:
        if onesMoreThanTwos(pointer.next.value):
            pointer.next = pointer.next.next

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

    pt = sieveListV3(pt)

    current = pt
    while current is not None:
        print(current.value, end=" ")
        current = current.next
    print()
