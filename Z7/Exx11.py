from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def check(pointer: Node, keyValue):

    q = pointer
    previous: Node

    while q.next is not None and q.next.value != keyValue:
        previous = q
        q = q.next

    if q.next is None:
        q.next = Node(keyValue)
    else:
        q.next = q.next.next


if __name__ == '__main__':

    freeLine = lambda: print("-----")

    elements = [i for i in range(100)]
    n = 99
    k = n

    idx = randint(0, n)
    first = Node(elements[idx])
    elements[n], elements[idx] = elements[idx], elements[n]
    n -= 1

    current = first
    for i in range(1, 100):
        idx = randint(0, n)
        next = Node(elements[idx])

        elements[n], elements[idx] = elements[idx], elements[n]
        n -= 1

        current.next = next
        current = current.next

    n = k
    while n >= 0:
        check(first, randint(0, n))
        current = first
        n -= 1
        i = 0
        while current is not None:
            print(current.value, end=" ")
            current = current.next
            i += 1
        print(" ->> i =", i)







