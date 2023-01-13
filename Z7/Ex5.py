from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def sortByLastDigit(pointer: Node) -> Node:
    beginning = [None for _ in range(10)]
    end = [None for _ in range(10)]

    while pointer is not None:

        last = pointer.value % 10

        if beginning[last] is None:

            beginning[last] = pointer
            end[last] = pointer

        else:

            end[last].next = pointer
            end[last] = pointer

        pointer = pointer.next
        # end[last].next = None

    result = None
    for i in range(9, -1, -1):
        if beginning[i] is not None:
            end[i].next = result
            result = beginning[i]

    return result


if __name__ == '__main__':

    first = Node(1)
    current = first
    for i in range(100):
        next = Node(randint(0, 100))
        current.next = next
        current = current.next

    first = sortByLastDigit(first)
    current = first

    while current is not None:

        print(current.value)
        current = current.next
    
