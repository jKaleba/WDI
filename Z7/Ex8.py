import time
from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    pointer: Node

    def __init__(self):
        self.pointer = Node(None)

    def getGuardian(self):
        return self.pointer

    def setGuardian(self, guardian):
        self.pointer = guardian

    def print(self):
        g = self.pointer.next if self.pointer.value is None else self.pointer
        print("Guardian -> ", end="")
        while g is not None:
            print(g.value, end=" -> ")
            g = g.next
        print(g)

    # in case of speeding it up, return Node, which can then be used in order to immediately append next elements
    def append(self, newValue, pointer=None) -> Node:

        if pointer is None:
            pointer = self.pointer

        if pointer.next is None:
            newNode = Node(newValue)
            pointer.next = newNode
            return newNode

        return self.append(newValue, pointer.next)

    def sieve(self):
        curr = self.getGuardian()
        while curr.next is not None and curr.next.next is not None:
            curr.next = curr.next.next
            curr = curr.next


if __name__ == '__main__':
    startTime = time.time()
    mList = LinkedList()
    last = mList.append(0)
    for i in range(1, 2000):
        newLast = mList.append(i, last)
        last = newLast

    mList.print()

    mList.sieve()

    mList.print()

    print(time.time() - startTime)
