from random import randint


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def add(pointer: Node, newValue):

    if pointer.next is None:
        q = Node(newValue)
        pointer.next = q
        return

    elif pointer.next.value >= newValue:
        q = Node(newValue, pointer.next)
        pointer.next = q
        return

    add(pointer.next, newValue)


def printList(g):

    g = g.next if g.value is None else g

    while g is not None:
        print(g.value)
        g = g.next


def mergeR(p: Node, q: Node):

    if p is None:
        return q
    if q is None:
        return p

    if p.value <= q.value:
        p.next = mergeR(p.next, q)
        return p
    else:
        q.next = mergeR(p, q.next)
        return q


def mergeI(p: Node, q: Node):
    g = Node(None)
    gPrim = g

    while p is not None and q is not None:
        if p.value <= q.value:
            g.next = p
            p = p.next
            g = g.next
        else:
            g.next = q
            q = q.next
            g = g.next

    if p is not None:
        g.next = p
    elif q is not None:
        g.next = q

    return gPrim


if __name__ == '__main__':

    data = [randint(1, 10) for _ in range(10)]

    a = Node(None)
    b = Node(None)
    for i in range(0, len(data) // 2 * 2, 2):
        add(a, data[i])
        add(b, data[i + 1])

    g = Node(None)
    g.next = mergeI(a.next, b.next)
    printList(g.next)
    print("---")

    a = Node(None)
    b = Node(None)
    for i in range(0, len(data) // 2 * 2, 2):
        add(a, data[i])
        add(b, data[i + 1])

    g = Node(None)
    g.next = mergeR(a.next, b.next)
    printList(g.next)



