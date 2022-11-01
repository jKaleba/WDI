from time import time
from math import log, isqrt
from random import randint


def ex1BaseChange(n: int, base: int) -> ():
    print("Ex1")

    result = [None for _ in range(int(log(n, base)) + 1)]

    for i in range(int(log(n, base)), -1, -1):
        result[i] = n % base
        n //= base

    for i in result:
        print('0123456789ABCDEF'[i], end="")

    print()


def ex2SameDigits(a: int, b: int):
    print("Ex2")

    if log(a, 10) != log(b, 10):
        return False

    counters = [0 for _ in range(20)]

    while a > 0:
        counters[a % 10] += 1
        a //= 10
        counters[b % 10 + 10] += 1
        b //= 10

    for i in range(10):
        if counters[i] != counters[i + 10]:
            return False

    return True


def ex3Sieve(n: int):
    print("Ex3")

    sieve = [True for _ in range(n)]
    sieve[0] = sieve[1] = False

    for i in range(2, n):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False

    for i in range(n):
        if sieve[i]:
            print(i, end=" ")


def ex3SieveFaster(n: int):
    print("Ex3")

    sieve = [True for _ in range(n)]
    sieve[0] = sieve[1] = False

    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False

    for i in range(n):
        if sieve[i]:
            print(i, end=" ")


# TODO
def ex4EulerWithArr(n: int):
    return


# TODO better
def ex5_10thValue() -> int:
    print("Ex5")

    data = [0 for _ in range(10)]
    taken = 0

    while True:
        value = int(input())
        if value == 0:
            break

        for i in range(10):
            if value >= data[i]:
                for j in range(9, i - 1, -1):
                    data[j] = data[j - 1]

                data[i] = value
                taken += 1
                break

        print(data)

    return data[9]


def ex6OddCheck(n: int) -> bool:
    print("Ex6")

    data = [randint(1, 1000) for _ in range(n)]

    for i in range(n):

        k = data[i]
        while k > 0 and (k % 10) % 2 == 0:
            k //= 10

        if k == 0:
            return False

    return True


def ex7OddCheckv2(n: int) -> bool:
    print("Ex7")

    data = [randint(1, 1000) for _ in range(n)]

    for i in range(n):

        k = data[i]
        while k > 0 and (k % 10) % 2 == 1:
            k //= 10

        if k == 0:
            return True

    return False


# TODO
def ex8Skipping(n: int) -> bool:
    # data = [randint(1, 10) for _ in range(n)]
    data = [10, 1, 3, 4, 8, 2, 9, 5, 9, 4, 1]

    index = 0
    left = 11 - index - 1

    while index < n:
        print(data)
        print("Here stack", index, left)

    return True


def ex9RisingSubsequenceLength(n: int, data: list) -> int:
    print("Ex9")

    maxLen = 0
    currLen = 1
    for i in range(1, n):

        if data[i] > data[i - 1]:
            currLen += 1
        else:
            if currLen > maxLen:
                maxLen = currLen
            currLen = 1

    if currLen > maxLen:
        maxLen = currLen

    return maxLen


def ex10MaxArithmeticSubsequenceLength(n: int, data: list) -> int:
    print("Ex10")

    maxLen = 0
    currLen = 2
    for i in range(2, n):

        if data[i] - data[i - 1] == data[i - 1] - data[i - 2]:
            if data[i] != data[i - 1]:
                currLen += 1
            else:
                currLen = 1

        else:
            if currLen > maxLen:
                maxLen = currLen
            currLen = 2

    if currLen > maxLen:
        maxLen = currLen

    return maxLen


def ex11MaxGeometricSubsequenceLength(n: int, data: list) -> int:
    print("Ex11")

    maxLen = 0
    currLen = 2
    for i in range(2, n):

        if data[i] * data[i - 2] == data[i - 1] ** 2:
            if data[i] != data[i - 1]:
                currLen += 1
            else:
                currLen = 1

        else:
            if currLen > maxLen:
                maxLen = currLen
            currLen = 2

    if currLen > maxLen:
        maxLen = currLen

    return maxLen


# TODO
def ex12SequencesEvenMore(n: int) -> int:
    print("Ex12")

    data = [randint(0, 49) * 2 + 1 for _ in range(n)]

    print(data)
    maxLenASC = 0
    maxLenDESC = 0
    currSequenceLength = 2

    gap = data[1] - data[0]
    for i in range(2, n):
        if data[i] - data[i - 1] == gap and gap != 0:
            currSequenceLength += 1
        else:
            if gap > 0 and currSequenceLength > maxLenASC:
                maxLenASC = currSequenceLength
                print(data[i - currSequenceLength: i])
            elif gap < 0 and currSequenceLength > maxLenDESC:
                maxLenDESC = currSequenceLength
                print(data[i - currSequenceLength: i])

            gap = data[i] - data[i - 1]
            currSequenceLength = 2

    if gap > 0 and currSequenceLength > maxLenASC:
        maxLenASC = currSequenceLength
    elif gap < 0 and currSequenceLength > maxLenDESC:
        maxLenDESC = currSequenceLength

    return abs(maxLenASC - maxLenDESC)


# TODO
def ex13SubsequenceWithReversion(n: int) -> int:
    # data = [randint(100, 999) for _ in range(n)]

    data = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]

    beginIndex = 0
    endIndex = n - 1

    return 0


def ex14SameBirthDayProbability(n: int) -> float:
    # print("Ex14")

    counter = 0
    k = 5000
    for i in range(k):
        birthdays = [randint(1, 365) for _ in range(n)]

        for i in range(n):

            multiple = False
            for j in range(i + 1, n):

                if birthdays[i] == birthdays[j]:
                    multiple = True
                    break

            if multiple:
                counter += 1
                break

    return counter / k


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


def ex15SomeConditions(n: int, data: list) -> bool:
    print("Ex15")

    index = 1
    nextIndex = 1

    while index < n:

        if prime(data[index] or data[index] < 1):
            return False

        data[index] = 0

        temporary = index + nextIndex
        index = nextIndex
        nextIndex = temporary

    for i in range(n):
        if data[i] != 0 and prime(data[i]):
            return True

    return False


def ex16LittleAndBigger(n: int, data: list) -> bool:
    print("Ex16")

    maxEl = 0
    minEl = 0

    for i in range(n):

        if data[i] > maxEl:
            maxEl = data[i]

        if data[i] < maxEl:
            minEl = data[i]

    for i in range(n):
        if data[i] == min or data[i] == max:
            return False

    return True


# TODO
def ex17ProperSum(n: int, firstArr: list, secondArr: list) -> int:
    for i in range(n):

        for j in range(n):
            break


def ex18PaliOddSubsequenceLen(n: int, data: list) -> int:
    index = 0
    maxLen = 0
    while index < n:

        end = index + 1
        if data[index] % 2 == 1:

            while end < n and data[end] % 2 == 1:
                end += 1

            for i in range(index, (end - index) // 2):
                if data[index + i] != data[end - 1 - i]:
                    break
            else:
                currLen = end - index
                if currLen > maxLen:
                    maxLen = currLen

        index = end

    return maxLen


# TODO
def ex19RisingSubsequenceWithSumEqualToSumOfItsIndexes(n: int, data: list) -> int:
    print("Ex19")

    maxLen = 0
    currLen = 1
    seqSum = data[0]
    indSum = 0

    for i in range(n):

        seqSum = data[i]
        indSum = i
        currLen = 1

        for j in range(i + 1, n):

            if data[j] > data[j - 1]:
                currLen += 1
                seqSum += data[j]
                indSum += j

                if currLen > maxLen and seqSum == indSum:
                    maxLen = currLen

            else:
                break

    return maxLen


def repetitiveFactors(n: int) -> bool:
    counter = 0
    while n % 2 == 0:
        counter += 1
        n //= 2

    if counter > 1:
        return True

    for i in range(3, isqrt(n) + 1, 2):
        counter = 0
        while n % i == 0:
            counter += 1
            n //= i

        if counter > 1:
            return True

    return False


def NWD(a: int, b: int) -> int:

    while b != 0:
        c = a % b
        a = b
        b = c

    return a


def ex20ProductSeqLen(n: int, data: list) -> int:
    print("Ex20")

    maxLen = 0
    for i in range(n):

        currLen = 0

        product = 1
        for j in range(i, n):
            product *= data[j]

            if not repetitiveFactors(product):
                currLen += 1
            else:
                break

        if currLen > maxLen:
            maxLen = currLen

    return maxLen



def ex21threes(n: int, data: list) -> int:
    print("Ex21")

    counter = 0

    for i in range(n - 4):

        for j in range(1, 3):

            for k in range(1, 3):

                if NWD(data[i], data[i + j]) and NWD(NWD(data[i], data[i + j]), data[i + j + k]):
                    counter += 1

                print(data[i], data[i + j], data[i + j + k])

    return counter


if __name__ == '__main__':
    # probabilities = [ex14SameBirthDayProbability(n) for n in range(20, 40)]
    # print(probabilities)

    # data = [3, 4, 4, 4, 3, 4, 3, 3, 4]
    # print(data)
    # print(ex15SomeConditions(9, data))
    # print(data)

    print(ex18PaliOddSubsequenceLen(10, [1 for _ in range(10)]))
    print(ex19RisingSubsequenceWithSumEqualToSumOfItsIndexes(7, [0, 1, 7, 2, 3, 5, 6]))
    #                                                            0  1  2  3  4  5  6

    t20 = [7, 5, 11, 4, 13, 2, 23, 33, 35, 7, 4, 6, 22]
    print(ex20ProductSeqLen(len(t20), t20))

    t21 = [i for i in range(30)]
    print(ex21threes(len(t21), t21))
