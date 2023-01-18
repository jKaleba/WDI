class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = None


def merge(p: Node, q: Node):

    return (min(p.val[0], q.val[0]), max(p.val[1], q.val[1])) if (p.val[0] <= q.val[1] and q.val[0] <= p.val[1]) else None


def reduce(p: Node):

    first = p

    while p.next is not None:

        prev = p
        q = p.next

        while q is not None:
            res = merge(p, q)
            if res is not None:
                p.val = res
                prev.next = q.next

                p = first

            prev = q
            q = q.next
            if res is not None:
                prev.next = None

        p = p.next


if __name__ == '__main__':

    pt = Node((15, 19))

    curr = pt

    curr.next = Node((2, 5))
    curr = curr.next

    curr.next = Node((7, 11))
    curr = curr.next

    curr.next = Node((8, 12))
    curr = curr.next

    curr.next = Node((5, 6))
    curr = curr.next

    curr.next = Node((13, 17))
    curr = curr.next

    curr = pt
    while curr is not None:
        print("[", curr.val[0], ",", curr.val[1], "]", end=" -> ")
        curr = curr.next
        if curr is None:
            print("None")

    reduce(pt)

    curr = pt
    while curr is not None:
        print("[", curr.val[0], ",", curr.val[1], "]", end=" -> ")
        curr = curr.next
        if curr is None:
            print("None")
