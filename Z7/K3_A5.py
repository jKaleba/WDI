
def move(T, i, ifRow=True):

    n = len(T)

    copyT = []
    for k in range(n):
        copyT.append([])
        for j in range(n):
            copyT[k].append(T[k][j])

    if ifRow:
        last = copyT[i][n - 1]

        for j in range(n - 1, 0, -1):
            copyT[i][j] = copyT[i][j - 1]

        copyT[i][0] = last

    else:
        last = copyT[n - 1][i]

        for j in range(n - 1, 0, -1):
            copyT[j][i] = copyT[j - 1][i]

        copyT[0][i] = last

    return copyT


def equalSum(T):

    n = len(T)

    value = -1

    for i in range(n):

        rowSum, colSum = 0, 0
        for j in range(n):
            rowSum += T[i][j]
            colSum += T[j][i]

        if rowSum != colSum:
            return False

        if value == -1:
            value = rowSum
        elif value != rowSum:
            return False

    return True


def magic(T, n=0, used=[]):

    if equalSum(T) and n == 2:
        for a in T:
            print(a)
        print(n, used)
        print()
        print("Positive - row, negative - column.")

        return True

    if n == 2:
        return False

    for i in range(len(T)):

        if magic(move(T, i, True), n + 1, used + [i]) or magic(move(T, i, False), n + 1, used + [-i]):
            return True

    return False


if __name__ == '__main__':

    arr = [
        [3, 11, 14, 17],
        [6, 12, 7, 9],
        [10, 8, 16, 13],
        [5, 15, 4, 2]
        ]

    arr2 = arr[:]

    print(magic(arr2))

