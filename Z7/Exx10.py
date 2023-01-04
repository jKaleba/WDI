from random import randint


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

    def print(self, message=None):

        print(message, end="\t")

        g = self.pointer.next if self.pointer.value is None else self.pointer
        print("Guardian -> ", end="")
        while g is not None:
            print(g.value, end=" -> ")
            g = g.next
        print(g)

    def appendDigit(self, newValue, pointer=None):

        if pointer is None:
            pointer = self.pointer

        if pointer.next is None:
            newNode = Node(newValue)
            pointer.next = newNode
            return

        self.appendDigit(newValue, pointer.next)

    def insert(self, newValue):

        newNode = Node(newValue, self.pointer.next)
        self.pointer.next = newNode
        return

    @staticmethod
    def add(number1, number2):

        digit1 = number1.getGuardian()
        digit2 = number2.getGuardian()

        def addR(digitPointer1, digitPointer2):
            return
        
        
            


freeLine = lambda: print("---")

if __name__ == '__main__':

    num1, num2 = Number(), Number()
    

    for i in range(randint(3, 5)):
        num1.appendDigit(randint(1, 9))

    for i in range(randint(1, 3)):
        num2.appendDigit(randint(1, 9))

    mSum: Number = Number.add(num1, num2)


    mSum.print("Sum equals:")
