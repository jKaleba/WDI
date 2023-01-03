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


    def pop(self):

        current = self.getGuardian()
        while current.next.next is not None:
            current = current.next

        val = current.next.value
        current.next = None

        return val


if __name__ == '__main__':
    mList = LinkedList()
    for i in range(10):
        mList.append(i)

    mList.print()

    print(mList.pop())

    mList.print()
