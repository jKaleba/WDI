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

        digit1 = number1.getGuardian().next
        digit2 = number2.getGuardian().next

        def addR(digitPointer1, digitPointer2):                    
            
            if digitPointer1.next is None and digitPointer2.next is None:
                newNumber = Number()
                newNumber.insert((digitPointer1.value + digitPointer2.value) % 10)

                rest = (digitPointer1.value + digitPointer2.value) // 10
                return newNumber, rest

            if digitPointer1.next is None:
                return addR(digitPointer1, digitPointer2.next)

            if digitPointer2.next is None:
                return addR(digitPointer1.next, digitPointer2)

            newNumber, currRest = addR(digitPointer1.next, digitPointer2.next)
            newNumber.insert((digitPointer1.value + digitPointer2.value + currRest) % 10)

            rest = (digitPointer1.value + digitPointer2.value + currRest) // 10
            return newNumber, rest

        numerList, y = addR(digit1, digit2)
        if y != 0:
            numerList.insert(y)
        
        if digit1 is None and digit2 is None:
            return numerList
        
        if digit1 is None:
            currGuard = numerList.getGuardian()
            numerList.setNextGuardian(digit2.next)
            
            while digit2.next is not None:
                digit2 = digit2.next
            
            digit2.next = currGuard        
        
        if digit2 is None:
            currGuard = numerList.getGuardian()
            numerList.setNextGuardian(digit1.next)
            
            while digit1.next is not None:
                digit1 = digit1.next
            
            digit1.next = currGuard
            
        
        return numerList


freeLine = lambda: print("---")

if __name__ == '__main__':

    num1, num2 = Number(), Number()

    for i in range(randint(3, 5)):
        num1.appendDigit(randint(1, 9))

    for i in range(randint(1, 3)):
        num2.appendDigit(randint(1, 9))

    mSum: Number = Number.add(num1, num2)

    num1.print("Number1: ")
    freeLine()
    num2.print("Number2: ")
    freeLine()

    mSum.print("Sum equals:")
