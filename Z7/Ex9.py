class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Number:
    pointer: Node

    def __init__(self):
        self.pointer = Node(None)

    def getGuardian(self):
        return self.pointer

    def setGuardianNext(self, next):
        self.pointer = next


    def appendDigit(self, newValue, pointer=None):

        if pointer is None:
            pointer = self.pointer

        if pointer.next is None:
            newNode = Node(newValue)
            pointer.next = newNode
            return

        self.appendDigit(newValue, pointer.next)

    def print(self):
        g = self.pointer.next if self.pointer.value is None else self.pointer
        print("Guardian -> ", end="")
        while g is not None:
            print(g.value, end=" -> ")
            g = g.next
        print(g)

    def increment(self):

        digit = self.getGuardian().next

        def incrementR(pointer: Node) -> int:

            if pointer.next is None:

                x = (pointer.value + 1) // 10
                pointer.value = (pointer.value + 1) % 10
                return x

            pointer.value += incrementR(pointer.next)
            x = pointer.value // 10
            pointer.value %= 10
            return x

        leftValue = incrementR(digit)

        if leftValue != 0:
            newNode = Node(leftValue, self.getGuardian().next)
            self.setGuardianNext(newNode)



if __name__ == '__main__':

    number = Number()

    for i in range(1, 10):
        number.appendDigit(9)

    number.print()

    number.increment()

    number.print()