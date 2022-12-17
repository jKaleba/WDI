import math
import random
import time
from math import isqrt, log, sqrt


def prime(n: int):
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


def reverse():
    return 0


def liczba(n):
    if not prime(n):
        ex1()


def ex1(n: int, kopia, w=0):
    # pomijamy ograniczenia zadania

    w = 0  # w = wynik

    if n == 0:

        w = reverse(w)
        if w >= 10 and w != kopia and prime(w):
            print(w)

    else:
        ex1(n // 10, w * 10 + n % 10)
        ex1(n // 10, w)


# TODO
def waga(n):
    return 0


def podzialR(T: list, a=0, b=0, c=0, p=0) -> bool:
    # kartkówkowe

    if p == len(T):
        return a == b == c

        return podzialR(T, a + waga(T[p]), b, c, p + 1) or \
               podzialR(T, a, b + waga(T[p]), c, p + 1) or \
               podzialR(T, a, b, c + waga(T[p]), p + 1)


def ex2Podzial(T):
    for i in range(len(T)): T[i] = waga(T[i])

    return sum(T) % 3 == 0 and podzialR(T)


def ex3KrolR(T: list[list], k, w=0, koszt=0):
    global kosztMin

    if w == 8:  # zeby liczylo ostatnie pole, bo dla warunku w == 7 by je pomijało
        kosztMin = min(kosztMin, koszt)

    else:
        if k > 0:
            ex3KrolR(T, k - 1, w + 1, koszt + T[w][k])

        if k < 7:
            ex3KrolR(T, k + 1, w + 1, koszt + T[w][k])

        ex3KrolR(T, k, w + 1, koszt + T[w][k])


def Krol(T: list[list]):
    global kosztMin

    kosztMin = 10 ** 5
    ex3KrolR(T, 7)

    return kosztMin


def koszt(T, w, k):
    if k == -1:
        return 10 ** 5

    if k == 8:
        return 10 ** 5

    if w == 8:
        return 10 ** 5

    if w == 8:
        return 0

    return min(koszt(T, w + 1, k - 1), koszt(T, w + 1, k), koszt(T, w + 1, k + 1), )


def permute(row: int, column: int):
    return [
        [row - 1, column - 2],
        [row - 2, column - 1],
        [row - 2, column + 1],
        [row - 1, column + 2],
        [row + 1, column + 2],
        [row + 2, column + 1],
        [row + 2, column - 1],
        [row + 1, column - 2],
    ]


def moveKnight(board: list, row, column, counter):
    n = len(board)

    time.sleep(0.01)

    for line in board:
        print(line)

    if counter == n * n:
        return
    if row >= n or column >= n or row < 0 or column < 0:
        return
    if board[row][column]:
        return

    board[row][column] = True
    counter += 1

    for coordinates in permute(row, column):
        moveKnight(board, coordinates[0], coordinates[1], counter)

    print()


def ex4KnightProblem(n: int, startRow, startCol):
    board = [[0 for _ in range(n)] for __ in range(n)]

    counter = 0
    moveKnight(board, startRow, startCol, counter)


def wypisz(board):
    for row in board:
        print(row)
    print()


def mozliwe(board, row, col, i):
    n = len(board)

    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    newRow, newCol = row + dy[i], col + dx[i]

    if 0 <= newRow < n and 0 <= newCol < n and board[newRow][newCol] == 0:
        return newRow, newCol

    return


stop = False


def skoczek(board, n=1, row=0, col=0):
    global stop
    board[row][col] = n

    if n == len(board) ** 2:
        wypisz(board)
        stop = True

    else:
        for i in range(8):
            if stop:
                break

            result = mozliwe(board, row, col, i)

            if result:
                skoczek(board, n + 1, result[0], result[1])

    board[row][col] = 0


# solve sudoku

def nextMove(board, row, col):
    if row + col == 16:
        return 0, 0

    while True:
        row = row + (col + 1) // 9
        col = (col + 1) % 9

        if row >= 9:
            return 0, 0

        if board[row][col] == 0:
            break

    return row, col


def solveSudoku(board):
    i = 0

    while board[i // 9][i % 9] != 0:
        i += 1

    elements = 0
    for row in board:
        for element in row:
            if element != 0:
                elements += 1

    sudoku(board, elements, i // 9, i % 9)


def possibilities(board, row, col):
    default = [True for _ in range(10)]

    for a in range(9):
        default[board[row][a]] = False
        default[board[a][col]] = False

    startRow = row // 3 * 3
    startCol = col // 3 * 3

    for i in range(startRow, startRow + 3):

        for j in range(startCol, startCol + 3):
            default[board[i][j]] = False

    return default


def showBoard(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            print(board[i][j], board[i][j + 1], board[i][j + 2], end="\t")
        print()

        for j in range(0, 9, 3):
            print(board[i + 1][j], board[i + 1][j + 1], board[i + 1][j + 2], end="\t")
        print()

        for j in range(0, 9, 3):
            print(board[i + 2][j], board[i + 2][j + 1], board[i + 2][j + 2], end="\t")

        print()
        print()

    print("\n\n")


stopSudoku = False


def sudoku(board: list[list[int]], n, row, col):
    global stopSudoku

    if n == len(board) ** 2:
        stopSudoku = True
        showBoard(board)
        return

    else:

        values = possibilities(board, row, col)
        for i in range(1, 10):

            if stopSudoku:
                break

            if values[i]:
                board[row][col] = i

                free = nextMove(board, row, col)

                if free:
                    sudoku(board, n + 1, free[0], free[1])

    board[row][col] = 0


def ex5SequenceCut(sequence: list[int]):
    if len(sequence) == 0:
        return True

    if len(sequence) == 1:
        return False

    power = 0
    value = 0
    i = len(sequence) - 1

    while i >= 0:

        value += sequence[i] * (2 ** power)
        if prime(value):

            if ex5SequenceCut(sequence[0:i]):
                return True

        power += 1
        i -= 1

    return False


def ex6SmallestSubset(collection: list[int]) -> int:
    subset = [(False, 0, 0) for _ in range(2 ** len(collection))]

    subsetR(collection, subset)

    currMin = 10 ** 5
    minIndex = 0

    for i in range(len(subset)):
        if subset[i][0]:

            if subset[i][1] < currMin or subset[i][1] == currMin and subset[i][2] < subset[minIndex][2]:
                currMin = subset[i][1]
                minIndex = i

    return subset[minIndex][2]


subsetIndex = 0


def subsetR(collection: list[int], subset: list[(bool, int, int)], index=0, n=0, indexSum=0, elSum=0):
    global subsetIndex

    if index == len(collection):
        subset[subsetIndex] = (elSum == indexSum != 0, n, elSum)
        subsetIndex += 1
        return

    subsetR(collection, subset, index + 1, n + 1, indexSum + index, elSum + collection[index])
    subsetR(collection, subset, index + 1, n, indexSum, elSum)


def ex6Faster(collection: list[int]) -> int:
    return ex6FasterR(collection)[1]


def myMin(a: (int, int), b: (int, int)) -> (int, int):
    if a[0] < b[0]:
        return a

    elif a[0] == b[0]:
        return a if a[1] <= b[1] else b

    else:
        return b


def ex6FasterR(collection: list[int], index=0, n=0, indexSum=0, elSum=0) -> (int, int):
    if indexSum == elSum != 0:
        return n, elSum

    if index == len(collection):
        return math.inf, elSum

    return myMin(ex6FasterR(collection, index + 1, n + 1, indexSum + index, elSum + collection[index]),
                 ex6FasterR(collection, index + 1, n, indexSum, elSum))


def ex7Weight(n: int, weights: list[int], index=0) -> bool:
    if n == 0:
        return True

    if index == len(weights):
        return False

    return ex7Weight(n - weights[index], weights, index + 1) or ex7Weight(n, weights, index + 1)


def ex8WeightOnBothSides(n: int, weights: list[int], index=0):
    if n == 0:
        return True

    if index == len(weights):
        return False

    return ex8WeightOnBothSides(n - weights[index], weights, index + 1) \
           or ex8WeightOnBothSides(n, weights, index + 1) \
           or ex8WeightOnBothSides(n + weights[index], weights, index + 1)


def ex9WeightWithPrint(n: int, weights: list[int], index=0, result=[]):
    if n == 0:
        print(result)
        return True

    if index == len(weights):
        return False

    return ex9WeightWithPrint(n - weights[index], weights, index + 1, result + [weights[index]]) \
           or ex9WeightWithPrint(n, weights, index + 1, result) \
           or ex9WeightWithPrint(n + weights[index], weights, index + 1, result + [-weights[index]])


def ex10MatrixDeterminant(matrix: list[list[int]], depth=0) -> int:
    n = len(matrix)

    if n == 1 and depth == len(matrix[0]) - 1:
        return matrix[0][depth]

    stageSum = 0
    for i in range(n):

        stageSum += matrix[i][depth] * (-1) ** (i + 2 * depth) * ex10MatrixDeterminant(matrix[:i] + matrix[i + 1:], depth + 1)
                                                  # added 2 times depth, because although I added + depth for column,
                                                  # since there are deleted rows, must also add + depth for them

    return stageSum


def ex11NNumbersWithGivenProduct(numbers: list[int], product, N, index=0):

    if N == 1:
        n1Sum = 0
        for i in range(index, len(numbers)):
            if product == numbers[i]:
                n1Sum += 1

        return n1Sum

    nSum = 0
    for i in range(index, len(numbers) - N + 1):
        if product % numbers[i] == 0:

            nSum += ex11NNumbersWithGivenProduct(numbers, product // numbers[i], N - 1, index + 1)

    return nSum


def ex12NNumbersWithGivenProduct(numbers: list[int], product, N, index=0, result=[]):

    if N == 1:
        for i in range(index, len(numbers)):
            if product == numbers[i]:
                print(result + [numbers[i]])

    else:
        for i in range(index, len(numbers) - N + 1):
            if product % numbers[i] == 0:
                ex12NNumbersWithGivenProduct(numbers, product // numbers[i], N - 1, index + 1, result + [numbers[i]])


def ex13NumberDivision(n: int, start=1, result=[], min=-1):
    if len(result):
        min = result[-2]
        print(result)

    if n == 1 or start == n:
        return

    for i in range(1, n // 2 + 1, 1):

        if i >= min:
            ex13NumberDivision(n - i, i, result[0: len(result) - 1] + [i, n - i])


def ex14Hanoi(n: int):
    A = [1] + [i for i in range(1, n + 1)]
    B = [n + 1] + [0 for _ in range(1, n + 1)]
    C = [n + 1] + [0 for _ in range(1, n + 1)]

    for i in range(1, len(A)):
        print(A[i], B[i], C[i], sep="\t")

    print("---------")
    print()

    rHanoi(n, A, B, C)

    for i in range(1, len(A)):
        print(A[i], B[i], C[i], sep="\t")

    print("---------")


def rHanoi(n: int, A: list, B: list, C: list):
    if n > 0:
        rHanoi(n - 1, A, C, B)

        C[C[0] - 1], A[A[0]] = A[A[0]], 0
        C[0] = C[0] - 1
        A[0] = A[0] + 1

        rHanoi(n - 1, B, A, C)


def ex16SameWeightWords(s1, s2):
    vow = vowels()

    weight = 0
    vowCounter = 0
    for char in s1:
        if vowel(char, vow):
            vowCounter += 1
        weight += ord(char)

    print(vowCounter, weight)

    s2Weight = 0

    return wyrazR(weight, s2, vow, vowCounter)


def wyrazR(weight, s2, vow, vowCounter, index=0):
    if weight == 0 and vowCounter == 0:
        return True
    elif weight < 0 or index == len(s2):
        return False

    return wyrazR(weight - ord(s2[index]), s2, vow, vowCounter - vowel(s2[index], vow), index + 1) \
           or wyrazR(weight, s2, vow, vowCounter, index + 1)


def vowels() -> list:
    letters = [False for _ in range(26)]
    letters[0] = letters[4] = letters[8] = letters[15] = letters[20] = True

    return letters


def vowel(character, vow) -> bool:
    return vow[ord(character) - 97]


counter = 0


def ex17BuildingNumber(n1: int, n2: int, res=0):
    global counter

    if n1 == 0 and n2 == 0 and prime(res):
        print(res)
        counter += 1

    if n1 > 0:
        ex17BuildingNumber(divN(n1), n2, result(res, nextDigit(n1)))

    if n2 > 0:
        ex17BuildingNumber(n1, divN(n2), result(res, nextDigit(n2)))


def nextDigit(n: int):
    return n // (10 ** (int(log(n, 10))))


def result(currResult, nextDig):
    return currResult * 10 + nextDig


def divN(n: int):
    return n % (10 ** (int(log(n, 10))))


def ex18King(row, col):
    board = [[random.randint(50, 52) for _ in range(8)] for _ in range(8)]
    for line in board:
        print(line)

    return kingR(board, row, col)


def kingR(board, row, col):
    if row == 7 and col == 7:
        return True

    further = False
    for i in range(3):
        move = possibleMoves(board, row, col, i)
        if move:
            further = kingR(board, move[0], move[1])

    return further


def possibleMoves(board, currRow: int, currCol: int, index: int) -> (int, int):
    dx = [1, 0, 1]
    dy = [1, 1, 0]

    newRow = currRow + dx[index]
    newCol = currCol + dy[index]

    if newRow < 8 and newCol < 8 and (
            board[currRow][currCol] % 10 < board[newRow][newCol] // (10 ** int(log(board[newRow][newCol], 10)))):
        return currRow + dx[index], currCol + dy[index]
    else:
        return False


def ex19KingAnyCorner(row, col):
    board = [[random.randint(50, 52) for _ in range(8)] for _ in range(8)]
    for line in board:
        print(line)

    return kingAnyR(board, row, col, (1, 1)) or kingAnyR(board, row, col, (1, -1)) or \
           kingAnyR(board, row, col, (-1, -1)) or kingAnyR(board, row, col, (-1, -1))


def kingAnyR(board, row, col, direction):
    if row == 0 or row == 7 and col == 0 or col == 7:
        return True

    further = False
    for i in range(3):
        move = possibleMovesAny(board, row, col, i, direction)
        if move:
            further = kingR(board, move[0], move[1])

    return further


def possibleMovesAny(board, currRow: int, currCol: int, index: int, direction: (int, int)) -> (int, int):
    dx = [1, 0, 1]
    dy = [1, 1, 0]

    newRow = currRow + dx[index] * direction[0]
    newCol = currCol + dy[index] * direction[1]

    if 0 <= newRow < 8 and 0 <= newCol < 8 and (
            board[currRow][currCol] % 10 < board[newRow][newCol] // (10 ** int(log(board[newRow][newCol], 10)))):
        return newRow, newCol
    else:
        return False


def ex21NonemptySubset(board: list, givenSum: int, row=0, col=0, result=[]) -> bool:
    n = len(board)

    if givenSum == 0:
        print(result)
        return True

    if givenSum < 0 or row == 8:
        return False

    return ex21NonemptySubset(board, givenSum - board[row][col], row + (col + 1) // n, (col + 1) % n,
                              result + [board[row][col]]) or \
           ex21NonemptySubset(board, givenSum, row + (col + 1) // n, (col + 1) % n, result)


def ex22Passage(data: list, index=0, jumps=0) -> int:
    if index == len(data) - 1:
        return jumps

    if index >= len(data):
        return -1

    temporary: int
    for i in range(data[index], 1, -1):

        if data[index] % i == 0:
            if prime(i):
                temporary = ex22Passage(data, index + i, jumps + 1)
                if temporary != -1:
                    return temporary

    return -1


def ex23Triplet(resistors: list[int], resistance, index=0, n=3) -> bool:
    if index == len(resistors) - n + 1:
        return False

    if n == 1:
        for i in range(index, len(resistors)):
            if resistors[i] == resistance:
                return True
    else:
        return ex23Triplet(resistors, resistance - resistors[index], index + 1, n - 1) or \
               ex23Triplet(resistors, resistance, index + 1, n)


def ex24TheLowestDistance(points: list[(int, int)], n) -> float:
    mass = [0 for _ in range(2 ** n)]
    massCentrePoints(points)

    minDistance = 10 ** 5
    for i in range(len(mass) - 1):

        for j in range(i + 1, len(mass)):

            currDistance = abs(mass[i] - mass[j])

            if currDistance < minDistance:
                minDistance = currDistance

    return minDistance


nextFreeIndex = 0


def massCentrePoints(points: list[(int, int)], index=0, sumx=0, sumy=0, n=0):
    global nextFreeIndex

    if index == len(points):
        points[nextFreeIndex] = sumx / n, sumy / n
        nextFreeIndex += 1
        return

    massCentrePoints(points, index + 1, sumx + points[index], sumy + points[index], n + 1)
    massCentrePoints(points, index + 1, sumx, sumy, n)


def ex26PossibleBuiltNumbers(A: int, B: int, result=[1]) -> int:
    nCounter = 0

    if A == 1 and B == 0:
        if result[-1] == 0:
            return 1
        elif result[-1] == 1:
            n = 0
            for i in range(len(result)):
                n += result[len(result) - i - 1] * (2 ** i)
            return not prime(n)
    else:
        if A > 1:
            nCounter += ex26PossibleBuiltNumbers(A - 1, B, result + [1])
        if B > 0:
            nCounter += ex26PossibleBuiltNumbers(A, B - 1, result + [0])

    return nCounter


def overlapping(square: tuple, otherSquares: list[tuple]):
    for otherSquare in otherSquares:
        if square[1] < otherSquare[0] or square[0] > otherSquare[1] or square[4] < otherSquare[3] or square[3] > \
                otherSquare[4]:
            continue
        else:
            return False

    return True


def ex27NonOverlappingSquares(squares: list[tuple[int]], index=0, result=[], n=13, areaSum=2012):
    if n == 1:
        for i in range(index, len(squares)):
            if not overlapping(list[i], result) and areaSum - area(squares[i]) == 0:
                return True
    else:
        for i in range(index, len(squares) - n + 1):
            if not overlapping(squares[i], result) and areaSum - area(squares[i]) > 0:
                temporary = ex27NonOverlappingSquares(squares, i, result + [squares[i]], n - 1)
                if temporary:
                    return True

    return False


def area(square: tuple) -> int:
    return (square[1] - square[0]) ** 2


def binaryR(n: int):
    if n > 0:
        binaryR(n // 2)
        print(n % 2, end="")


def binaryRR(n: int) -> int:
    if n > 0:
        return 10 * binaryRR(n // 2) + n % 2
    else:
        return 0


def onesB(binary: int):
    c = 0
    while binary > 0:
        c += binary % 10
        binary //= 10

    return c


def ones(n: int):
    binary = binaryRR(n)
    return onesB(binary)


def countOnes(binaries: list[int]):
    return sum(ones(binaries[i]) for i in range(len(binaries)))


def ex28CollectionDivision(collection: list[int], n1=0, n2=0, n3=0, index=0, r1=[], r2=[], r3=[]) -> bool:
    if index == len(collection):

        # return n1 == n2 == n3

        if n1 == n2 == n3:
            print(r1, r2, r3)
            return True
        else:
            return False

    return ex28CollectionDivision(collection, n1 + ones(collection[index]), n2, n3, index + 1, r1 + [collection[index]],
                                  r2, r3) or \
           ex28CollectionDivision(collection, n1, n2 + ones(collection[index]), n3, index + 1, r1,
                                  r2 + [collection[index]], r3) or \
           ex28CollectionDivision(collection, n1, n2, n3 + ones(collection[index]), index + 1, r1, r2,
                                  r3 + [collection[index]])


def ex29SubsetInDistance(coordinates: list[tuple], r, index=0, sumx=0, sumy=0, sumz=0, n=0) -> bool:
    if n >= 3 and pointsDistance(massCentre(sumx, sumy, sumz, n), (0, 0)) <= r:
        return True

    if index == len(coordinates) - n + 1:
        return False

    return ex29SubsetInDistance(coordinates, r, index + 1, sumx + coordinates[index][0], sumy + coordinates[index][1],
                                sumz + coordinates[index][3], n + 1) or \
           ex29SubsetInDistance(coordinates, r, index + 1, sumx, sumy, sumz, n)


def massCentre(x, y, z, n):
    return x / n, y / n, z / n


def pointsDistance(A, B) -> float:
    return sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2 + (A[2] - B[2]) ** 2)


def ex31NonemptySubsetsOfDivisors(n: int) -> int:
    divs = primeDivisors(n)

    return subsetsR(divs)


def subsetsR(divisors: list, index=0, product=1, n=3) -> int:
    if index == len(divisors):
        if product == 1:
            return 0
        else:
            return product

    return subsetsR(divisors, index + 1, product, n - 1) + subsetsR(divisors, index + 1, product * divisors[index],
                                                                    n - 1)


def primeDivisors(n: int):
    divisors = []

    if n % 2 == 0:
        divisors = [2]

    for i in range(3, isqrt(n) + 1, 2):

        if n % i == 0:
            primeDiv = True
            for j in range(3, isqrt(i) + 1, 2):

                if i % j == 0:
                    primeDiv = False
                    break

            if primeDiv:
                divisors += [i]

    return divisors


def ex32SameSumSubsets(data: list, k, index=0, s1=0, s2=0, n1=0, n2=0) -> bool:
    if n1 + n2 == k and s1 == s2:
        return True
    if index == len(data):
        return False

    return ex32SameSumSubsets(data, k, index + 1, s1 + data[index], s2, n1 + 1, n2) or \
           ex32SameSumSubsets(data, k, index + 1, s1, s2 + data[index], n1, n2 + 1) or \
           ex32SameSumSubsets(data, k, index + 1, s1, s2, n1, n2)


if __name__ == '__main__':

    asd = [1, 1, 1, 1, 1, 1, 1, 1, 8, 9]

    print(ex11NNumbersWithGivenProduct(asd, 72, 2)) # 1
    print(ex11NNumbersWithGivenProduct(asd, 72, 3)) # 8
    print(ex11NNumbersWithGivenProduct(asd, 72, 4)) # 49
    print()

    ex12NNumbersWithGivenProduct(asd, 72, 2) # [8, 9]
    print()
    ex12NNumbersWithGivenProduct(asd, 72, 3)
    # [1, 8, 9]
    # [1, 8, 9]
    # [1, 8, 9]
    # [1, 8, 9]
    # [1, 8, 9]
    # [1, 8, 9]
    # [1, 8, 9]
    # [1, 8, 9]
