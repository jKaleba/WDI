from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def fivesInOctal(n):
    counter = 0
    while n > 0:
        if n % 8 == 5:
            counter += 1

        n //= 8

    return counter


def sieveListV3(pointer: Node) -> Node:
    beginning = pointer

    while pointer is not None and fivesInOctal(pointer.value) % 2 == 0:
        pointer = pointer.next

    while pointer is not None and pointer.next is not None:
        if fivesInOctal(pointer.next.value) % 2 == 0:
            temporary = pointer.next.next
            newBeginning = pointer.next
            pointer.next.next = beginning
            pointer.next = temporary
            beginning = newBeginning

        pointer = pointer.next

    return beginning


if __name__ == '__main__':

    freeLine = lambda: print("---")

    pt = Node(randint(1, 200))
    current = pt
    for i in range(100):
        current.next = Node(randint(1, 200))
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
