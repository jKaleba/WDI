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


    def append(self, newValue, pointer=None):

        if pointer is None:
            pointer = self.pointer

        if pointer.next is None:
            newNode = Node(newValue)
            pointer.next = newNode
            return

        self.append(newValue, pointer.next)


    def sieve(self):
        curr = self.getGuardian()
        while curr.next is not None and curr.next.next is not None:
            curr.next = curr.next.next
            curr = curr.next



if __name__ == '__main__':
    mList = LinkedList()
    for i in range(10):
        mList.append(i)

    mList.print()

    mList.sieve()

    mList.print()
