import time
from random import randint
from math import log, log2, isqrt


def showArray(data: list):
    for row in data:
        for element in row:
            print(element, end='\t')

        print()
    print()


# DONE
def ex1Spiral(n: int):
    naturals = [[None for _ in range(n)] for __ in range(n)]

    i = -1
    j = 0
    currNumber = 1

    d = n - 1  # down
    r = n - 1  # right
    u = 0  # up
    l = 1  # left

    for k in range((2 * n - 1) // 4 + 1):

        while i < d:
            i += 1
            naturals[i][j] = currNumber
            currNumber += 1

        while j < r:
            j += 1
            naturals[i][j] = currNumber
            currNumber += 1

        while i > u:
            i -= 1
            naturals[i][j] = currNumber
            currNumber += 1

        while j > l:
            j -= 1
            naturals[i][j] = currNumber
            currNumber += 1

        d, r, u, l = d - 1, r - 1, u + 1, l + 1

    showArray(naturals)


# DONE
def ex1SpiralClass(n: int):
    a = 0
    b = n - 1
    currNumber = 1

    spiral = [[None for _ in range(n)] for __ in range(n)]

    while a <= b:

        for i in range(a, b + 1):
            spiral[a][i] = currNumber
            currNumber += 1

        for j in range(a + 1, b):
            spiral[j][b] = currNumber
            currNumber += 1

        for k in range(b, a, -1):
            spiral[b][k] = currNumber
            currNumber += 1

        for l in range(b, a, -1):
            spiral[l][a] = currNumber
            currNumber += 1

        a, b = a + 1, b - 1

    showArray(spiral)


# DONE
def ex2AtLeastOneOddDigitNumber(data: list) -> bool:
    n = len(data)
    allOdds: bool

    for i in range(n):

        for j in range(n):

            allOdds = True
            while data[i][j] > 0:
                digit = data[i][j] % 10
                data[i][j] //= 10

                if digit % 2 == 0:
                    allOdds = False
                    break

            if allOdds:
                return True

    return False


# DONE
def ex3RowWhereEachNumberContainsAtLeast1EvenDigit(data: list) -> bool:
    n = len(data)

    for i in range(n):

        row = True
        for j in range(n):

            even = False
            while data[i][j] > 0:
                digit = data[i][j] % 10
                data[i][j] //= 10

                if digit % 2 == 0:
                    even = True

            if not even:
                row = False
        if row:
            return True

    return False


# DONE
def ex4MaxQuotient(data: list[list]) -> (int, int):
    n = len(data)

    sums = [[None for _ in range(n)] for __ in range(2)]

    for row in range(n):

        rowSum = 0
        colSum = 0

        for column in range(n):
            rowSum += data[row][column]
            colSum += data[column][row]

        sums[0][row] = rowSum
        sums[1][row] = colSum

    mX, mY = 0, 1

    x = 0
    y = 0
    for i in range(n):
        for j in range(n):
            if sums[0][i] * mY > sums[1][j] * mX:
                mX, mY = sums[0][i], sums[1][j]
                x = j
                y = i

    return x + 1, y + 1


# DONE
def ex6SingletonsAscending(T1: list[list[int]]):
    n = len(T1)
    m = n * n

    T2 = [0 for _ in range(m)]

    indexesSum = 0  # licznik wartosci minimalnych
    indexes = [0 for _ in range(n)]

    lastT2Index = -1

    while indexesSum != n * n:

        mini = 100
        miniRow = 0
        throwOut = False

        for row in range(n):
            if indexes[row] < n and T1[row][indexes[row]] < mini:

                if indexes[row] < n and T1[row][indexes[row]] == T2[lastT2Index]:
                    indexes[row] += 1
                    indexesSum += 1
                    throwOut = True

                else:
                    mini = T1[row][indexes[row]]
                    miniRow = row

        if throwOut:
            continue

        lastT2Index += 1
        T2[lastT2Index] = mini
        indexesSum += 1
        indexes[miniRow] += 1

    return T2


# DONE
def ex7SingletonsNonDescending(T1: list[list[int]]):
    n = len(T1)
    m = n * n

    T2 = [0 for _ in range(m)]

    indexesSum = 0  # licznik wartosci minimalnych
    indexes = [0 for _ in range(n)]

    lastT2Index = -1

    while indexesSum != n * n:

        mini = 100
        miniRow = 0
        throwOut = False

        for row in range(n):
            if indexes[row] < n and T1[row][indexes[row]] < mini:
                mini = T1[row][indexes[row]]
                miniRow = row

        lastT2Index += 1
        T2[lastT2Index] = mini
        indexesSum += 1
        indexes[miniRow] += 1

    return T2


# DONE
def ex8diagonalGeometricsSequence(data: list[list[int]]) -> (bool, int):
    n = len(data)
    if n < 3:
        return False, 0

    gap = n + 1
    maxSeqLen = 0
    currLen = 2
    for i in range(2, n):
        if data[i][i] * data[i - 2][i - 2] == data[i - 1][i - 1] ** 2:
            currLen += 1
        elif currLen > maxSeqLen:
            maxSeqLen = currLen
            currLen = 2

    if currLen > maxSeqLen:
        maxSeqLen = currLen

    for i in range(1, n - 2):
        rightLen = 2
        leftLen = 2
        for j in range(2, n - i):
            if data[j][j + i] * data[j - 2][j + i - 2] == data[j - 1][j + i - 1] ** 2:
                rightLen += 1
            elif rightLen > maxSeqLen:
                maxSeqLen = rightLen
                rightLen = 2

            if data[j + i][j] * data[j + i - 2][j - 2] == data[j + i - 1][j - 1] ** 2:
                leftLen += 1
            elif leftLen > maxSeqLen:
                maxSeqLen = leftLen
                leftLen = 2

        if rightLen > maxSeqLen:
            maxSeqLen = rightLen
        if leftLen > maxSeqLen:
            maxSeqLen = leftLen

    return maxSeqLen != 2, maxSeqLen


def clear(data: list[list[int]]):
    n = len(data)
    for i in range(n):
        for j in range(n):
            data[i][j] = 0


# DONE
def ex9Square(data: list[list[int]], k: int) -> (bool, int, int):
    n = len(data)

    for i in range(3, n, 2):

        for j in range(0, n - i):

            for l in range(0, n - i):

                a, b, c, d = data[j][l], data[j + i][l], data[j][l + i], data[j + i][l + i]
                if a * b * c * d == k:
                    clear(data)
                    data[j][l], data[j + i][l], data[j][l + i], data[j + i][l + i] = a, b, c, d
                    for row in data:
                        for element in row:
                            print(element, end="\t")
                        print()

                    return True, l + i / 2, j + i / 2

    return False, -1, -1


# DONE
def ex10AtLeast1Zero(data: list[list[int]]) -> bool:
    n = len(data)

    for row in range(n):

        inRow = False
        inColumn = False

        for column in range(n):

            if data[row][column] == 0:
                inRow = True

            if data[column][row] == 0:
                inColumn = True

        if not inRow or not inColumn:
            return False

    return True


def psiapsi(data: list[int]) -> bool:
    n = len(data)

    digits = [0 for _ in range(10)]
    distinguishable = 0
    while data[0] > 0:

        if not digits[data[0] % 10]:
            digits[data[0] % 10] += 1
            data[0] //= 10
            distinguishable += 1

    for i in range(1, n):

        currDisting = 0

        while data[i] > 0:

            if digits[data[i] % 10] and digits[data[i] % 10] <= 1 + i:
                currDisting += 1
                digits[data[i] % 10] += 1

            elif not digits[data[i] % 10]:
                return False

            data[i] //= 10

        if currDisting != distinguishable:
            return False

    return True


# TODO BETTER
def ex11PsiapsiNeighboursCounter(data: list[list[int]]) -> int:
    n = len(data)

    counter = 0

    if psiapsi([data[0][0], data[1][0], data[0][1], data[1][1]]):
        counter += 1

    if psiapsi([data[n - 1][0], data[n - 1 - 1][0], data[n - 1][1], data[n - 1 - 1][1]]):
        counter += 1

    if psiapsi([data[0][n - 1], data[0][n - 2], data[1][n - 1], data[1][n - 2]]):
        counter += 1

    if psiapsi([data[n - 1][n - 1], data[n - 1][n - 2], data[n - 2][n - 1], data[n - 2][n - 2]]):
        counter += 1

    for i in range(1, n - 1):

        if psiapsi([data[0][i], data[0][i - 1], data[0][i + 1],
                    data[1][i], data[1][i - 1], data[1][i + 1]]):
            counter += 1

        if psiapsi([data[i][0], data[i - 1][0], data[i + 1][0],
                    data[i][1], data[i - 1][1], data[i + 1][1]]):
            counter += 1

        if psiapsi([data[i][n - 1], data[i - 1][n - 1], data[i + 1][n - 1],
                    data[i][n - 2], data[i - 1][n - 2], data[i + 1][n - 2]]):
            counter += 1

        if psiapsi([data[n - 1][i], data[n - 1][i - 1], data[n - 1][i + 1],
                    data[n - 2][i], data[n - 2][i - 1], data[n - 2][i + 1]]):
            counter += 1

    for i in range(1, n - 1):

        for j in range(1, n - 1):

            if psiapsi([data[i][j], data[i][j - 1], data[i][j + 1],
                        data[i - 1][j], data[i - 1][j - 1], data[i - 1][j + 1],
                        data[i + 1][j], data[i + 1][j - 1], data[i + 1][j + 1]]):
                counter += 1

    return counter


def prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False

    return True


# TODO BETTER
def ex12(cube: list[list[list[int]]]) -> bool:
    n = len(cube)

    previousLvlCounter = 10 ** 10

    for level in range(n):
        counter = 0
        for row in range(1, n - 1):

            for el in range(1, n - 1):
                primeCounter = 0
                for i in range(-1, 0, 2):
                    for j in range(-1, 0, 2):
                        if not prime(cube[level][row + i][el + j]):
                            primeCounter += 1

                if not prime(cube[level][row][el]):
                    primeCounter -= 1

                if primeCounter == 6:
                    counter += 1

        if previousLvlCounter != counter and previousLvlCounter != 10 ** 10:
            return False

        previousLvlCounter = counter

    return True


def binary(n: int) -> list[int]:
    resultLen = int(log2(n)) + 1
    result = [0 for _ in range(resultLen)]
    print(resultLen)

    for i in range(resultLen - 1, -1, -1):
        result[i] += n % 2
        n //= 2

    return result


def ones(n: list[int]) -> int:
    counter = 0
    for i in range(len(n)):
        if n[i] == 1:
            counter += 1

    return counter


def onesInQuadruple(n: int):
    onesCounter = 0
    while n > 0:
        if n % 4 == 1:
            onesCounter += 1
        n //= 4


# DONE
def ex14CompatibleNumbers(T1: list[list[int]], T2: list[list[int]]) -> bool:
    n = len(T1)
    m = len(T2)

    if n > m:
        return False

    for moveDown in range(0, m - n + 1):

        for moveRight in range(0, m - n + 1):

            counter = 0
            for row in range(0, n):

                for col in range(0, n):

                    if onesInQuadruple(T2[row][col]) == onesInQuadruple(T1[row + moveDown][col + moveRight]):
                        counter += 1

            if counter * 3 >= n * n:
                return True

    return False


# DONE
def ex15AnyRowWithPrimeDigitNumber(data: list[list[int]]) -> bool:
    n = len(data)

    for row in range(n):

        eachInRowContains = True
        for column in range(n):
            occurs = False
            while data[row][column] > 0:

                digit = data[row][column] % 10
                if digit == 2 or digit == 3 or digit == 5 or digit == 7:
                    occurs = True

                data[row][column] //= 10

            if not occurs:
                eachInRowContains = False
                break

        if eachInRowContains:
            return True

    return False


# DONE
def ex16EveryRowWithAllPrimeDigitsNumber(data: list[list[int]]) -> bool:
    n = len(data)

    primes = [2, 3, 5, 7]

    for row in range(n):

        exists = False
        for column in range(n):
            allPrime = True
            while data[row][column] > 0:

                digit = data[row][column] % 10
                if not (digit == 2 or digit == 3 or digit == 5 or digit == 7):
                    allPrime = False

                data[row][column] //= 10

            if allPrime:
                exists = True
                break

        if not exists:
            return False

    return True


# DONE
def ex17ElementWithBiggestSumAround(data: list[list[int]]) -> (int, int):
    n = len(data)

    left = 0
    right = 0

    maxSum = 0
    x = 0
    y = 0

    for i in range(1, n - 1):

        left = data[i][0] + data[i - 1][0] + data[i + 1][0]
        middle = data[i][1] + data[i - 1][1] + data[i + 1][1]
        right = data[i][2] + data[i - 1][2] + data[i + 1][2]

        for j in range(1, n - 1):
            currSum = left + middle + right - data[i][j]

            if currSum > maxSum:
                maxSum = currSum
                x = j
                y = i

            middle = right
            left = middle
            right = data[i][j + 2] + data[i - 1][j + 2] + data[i + 1][j + 2]

    return x, y


# DONE
def ex18ConsistentSubsequence(data: list[list[int]]) -> int:
    n = len(data)

    m = min(n, 10)

    maxHorizontalSum = 0
    maxVerticalSum = 0

    horizontalSeq = [0 for _ in range(m)]
    verticalSeq = [0 for _ in range(m)]

    for i in range(n):

        horizontalSum = 0
        verticalSum = 0

        oldestHor = 0
        oldestVer = 0

        for k in range(m):
            horizontalSum += data[i][k]
            horizontalSeq[k] = data[i][k]

            verticalSum += data[k][i]
            verticalSeq[k] = data[k][i]

        if horizontalSum > maxHorizontalSum:
            maxHorizontalSum = horizontalSum

        if verticalSum > maxVerticalSum:
            maxVerticalSum = verticalSum

        # print(horizontalSeq, verticalSeq)
        # time.sleep(1)

        for j in range(m, n):
            horizontalSum += data[i][j]
            horizontalSum -= horizontalSeq[oldestHor]
            horizontalSeq[oldestHor] = data[i][j]
            oldestHor = (oldestHor + 1) % m

            verticalSum += data[j][i]
            verticalSum -= verticalSeq[oldestVer]
            verticalSeq[oldestVer] = data[j][i]
            oldestVer = (oldestVer + 1) % m

            # print(horizontalSeq, verticalSeq)
            # time.sleep(1)

            if horizontalSum > maxHorizontalSum:
                maxHorizontalSum = horizontalSum

            if verticalSum > maxVerticalSum:
                maxVerticalSum = verticalSum

    return max(maxVerticalSum, maxHorizontalSum)


# DONE
def ex19KnightProduct(data: list[list[int]], k: int) -> int:
    n = len(data)

    pairCounter = 0

    for i in range(n - 2):

        for j in range(n - 1):

            # horizontal
            if data[i][j] * data[i + 2][j + 1] == k:
                pairCounter += 1

            if data[i + 2][j] * data[i][j + 1] == k:
                pairCounter += 1

            # vertical
            if data[j][i] * data[j + 1][i + 2] == k:
                pairCounter += 1

            if data[j + 1][i] * data[j][i + 2] == k:
                pairCounter += 1

    return pairCounter


# TODO
def ex20Chess(board: list[list]):

    n = len(board)

    sw = [0 for _ in range(n)]
    sk = [0 for _ in range(n)]
    maxSum = 0

    for row in range(n):
        rowSum = 0
        colSum = 0
        for col in range(n):
            rowSum += board[row][col]
            colSum += board[col][row]

        sw[row] = rowSum
        sk[row] = colSum

    firstKnight = (0, 0)
    secondKnight = (0, 0)

    for i in range(n * n - 1):

        w1, k1 = i // n, i % n

        for j in range(i + 1, n * n):

            w2, k2 = j // n, j % n

            if w1 == w2:
                sum = sw[w1] + sk[k1] + sk[k2] - 2 * board[w1][k1] - 2 * board[w2][k2]

            elif k1 == k2:
                sum = sk[k1] + sw[w1] + sw[w2] - 2 * board[w1][k1] - 2 * board[w2][k2]

            else:
                sum = sw[w1] + sw[w2] + sk[k1] + sk[k2] - \
                      2 * board[w1][k1] - 2 * board[w2][k2] - board[w1][k2] - board[w2][k1]

            if sum > maxSum:
                maxSum = sum
                firstKnight = (w1, k1)
                secondKnight = (w2, k2)

    return firstKnight, secondKnight


def twoDiffFactors(n):

    counter = 0
    if n % 4 == 0:
        return False

    if n % 2 == 0:
        counter += 1

    for i in range(3, isqrt(n) + 1, 2):

        if n % i == 0:

            if n % (i * i) == 0:
                return False
            else:
                counter += 1

        if counter > 2:
            return False

    return True


if __name__ == '__main__':
    print()
    ex1Spiral(10)
    ex1SpiralClass(10)

    a = [[i + j * 15 for i in range(10)] for j in range(10)]

    b, c, d = ex9Square(a, 10206000)
    print(b, c, d)

    trial = [[1, 1, 1, 1], [1, 2, 1, 1], [1, 2, 1, 1], [2, 1, 1, 2]]
    for row in trial:
        print(row)
    print(ex11PsiapsiNeighboursCounter(trial))

    print(binary(11))

    ex14CompatibleNumbers(trial, a)

    k = 15

    m = min(10, k)

    pls = [[i + k * j for i in range(k)] for j in range(k)]
    for row in pls:
        print(row)

    print()
    print(ex18ConsistentSubsequence(pls))
    print(sum([pls[k - 1][i] for i in range(k - 1, k - m - 1, -1)]))

    ex19Data = [[randint(1, 2) for _ in range(5)] for __ in range(5)]
    for row in ex19Data:
        print(row)

    print(ex19KnightProduct(ex19Data, 1))

    k = 10
    ex6Data = [[i + k * j for i in range(k)] for j in range(k)]
    ex7Data = ex6Data[:]

    ex6Data[0] = [i for i in range(10, 20)]
    ex7Data[0] = [1 for _ in range(10)]

    for i in range(len(ex6Data)):
        print(ex6Data[i], "\t", ex7Data[i])
    print()

    ex6Result = ex6SingletonsAscending(ex6Data)
    print(ex6Result)

    ex7Result = ex7SingletonsNonDescending(ex7Data)
    print(ex7Result)

    print()
    n = 567

    for i in range(int(log(n, 10)) + 1):

        print(n // (10 ** i) % 10)


    firstAr = [1 for _ in range(5)]

    secondAr = firstAr[:]

    thirdAr = firstAr

    print(id(firstAr), id(secondAr), id(thirdAr))
    print(firstAr, secondAr, thirdAr)
