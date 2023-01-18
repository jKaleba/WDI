from random import randint


class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = None


def seqReducto(p: Node):

    currLen = 1
    maxLen = 1
    beginPointer = None
    finalBeginPointer = None


    prev = p
    current = p.next

    while current is not None:

        if current.val > prev.val and current.next is not None:

            if currLen == 1:
                beginPointer = prev

            currLen += 1

        elif current.val > prev.val and current.next is None:
            if currLen == 1:
                beginPointer = prev

            currLen += 1
            if currLen > maxLen:
                maxLen = currLen
                finalBeginPointer = beginPointer

        else:
            if currLen > maxLen:
                maxLen = currLen
                finalBeginPointer = beginPointer
            elif currLen == maxLen:
                finalBeginPointer = None

            currLen = 1

        prev = current
        current = current.next

    if finalBeginPointer is None:
        return p

    if p != finalBeginPointer:

        current = p
        while current.next != finalBeginPointer:
            current = current.next

        last = finalBeginPointer
        while last.next is not None and last.next.val > last.val:
            last = last.next

        current.next = last.next

        return p

    else:

        q = p
        while q.next.val is not None and q.next.val > q.val:
            q = q.next

        p = q.next
        return p


if __name__ == '__main__':

    pt = Node(randint(0, 50))

    curr = pt
    for i in range(20):
        curr.next = Node(randint(0, 50))
        curr = curr.next


    curr = pt
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

    pt = seqReducto(pt)

    curr = pt
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()
