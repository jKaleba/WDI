from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def aBiggerThB(a, b, index=0):
    if index == len(a) == len(b):
        return False

    if index == len(a):
        return False

    if index == len(b):
        return True

    if a[index] > b[index]:
        return True

    elif a[index] < b[index]:
        return False

    else:
        return aBiggerThB(a, b, index + 1)


def add(pointer: Node, string):
    # pointer initially is guardian

    if pointer.next is None:
        pointer.next = Node(string)
        return True

    if pointer.next.value == string:
        return False

    elif aBiggerThB(pointer.next.value, string):
        pointer.next = Node(string, pointer.next)
        return True
    else:
        return add(pointer.next, string)


def generatedString(n):
    result = ""
    for i in range(n):
        result += chr(97 + randint(0, 25))
    return result


if __name__ == '__main__':

    guardian = Node("")

    for i in range(20):
        genStr = generatedString(randint(1, 50))
        add(guardian, genStr)

    current = guardian.next
    while current is not None:
        print(current.value)
        current = current.next
