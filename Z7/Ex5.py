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

    def add(self, newValue, pointer=None):

        if pointer is None:
            pointer = self.pointer

        if pointer.next is None:
            q = Node(newValue)
            pointer.next = q
            return

        elif pointer.next.value >= newValue:
            q = Node(newValue, pointer.next)
            pointer.next = q
            return

        self.add(newValue, pointer.next)

    # removes and returns one node
    def pop(self, previous: Node):

        current = previous.next
        previous.next = previous.next.next
        current.next = None

        return current.value

    def attach(self, pointer: Node):

        pointer.next = self.pointer.next
        self.pointer.next = pointer
        return

    def insert(self, newValue):

        newNode = Node(newValue, self.pointer.next)
        self.pointer.next = newNode
        return

    def append(self, newValue, pointer=None):

        if pointer is None:
            pointer = self.pointer

        if pointer.next is None:
            newNode = Node(newValue)
            pointer.next = newNode
            return

        self.append(newValue, pointer.next)

    @staticmethod
    def merge(ll1, ll2):

        mergedList = LinkedList()
        mergedList.setGuardian(ll1.getGuardian())

        pointer1 = ll1.getGuardian()
        pointer2 = ll2.getGuardian().next

        while pointer1.next is not None:
            pointer1 = pointer1.next

        pointer1.next = pointer2

        return mergedList


freeLine = lambda: print("---")

if __name__ == '__main__':
    mList = LinkedList()
    for i in range(100):
        mList.insert(randint(0, 1000))

    mList.print()
    freeLine()

    div = [LinkedList() for _ in range(10)]

    g = mList.getGuardian()

    while g.next is not None:
        div[g.next.value % 10].insert(mList.pop(g))

    res = LinkedList()

    for i in range(len(div)):
        res = LinkedList.merge(res, div[i])

    res.print()
