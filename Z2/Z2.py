import time
from math import sqrt, log, e


def ex1MultiplicationOfAny2FiboElements(result: int):
    print("Ex1")

    if result == 1:
        return True

    a = 1
    b = 1
    c = a + b

    while b <= sqrt(result):
        a = b
        b = c
        c = a + b

        if result % a == 0:
            e = b
            f = c
            g = e + f

            while f <= result // a:
                e = f
                f = g
                g = e + f

                if result == e * a:
                    print(a, e)
                    return True

    return False


def ex2FractionExpansion(a: int, b: int, n: int):
    print("Ex2")

    print(str(a // b) + ",", end="")
    for i in range(n):
        a = a % b
        a *= 10
        print(str(a // b), end="")

    a = a % b
    a *= 10
    print(round(a / b))
    return


def length(n: int) -> int:
    if n == 0:
        return 1

    return int(log(n, 10)) + 1


def pali(n: int):
    nLength = length(n)

    for i in range(nLength // 2):

        if n // (10 ** (nLength - i - 1)) % 10 != (n % (10 ** (i + 1))) // (10 ** i):
            return False

    return True


def binary(n: int) -> int:
    result = 0

    i = 0
    while n > 0:
        result = result + (n % 2 * (10 ** i))
        n = n // 2
        i += 1

    return result


def ex3(n: int):
    if pali(n) and pali(binary(n)):
        print("Pali both")
    elif pali(n):
        print("Pali n")
    elif pali(binary(n)):
        print("Pali binary n")


def ex4Double_Three_FiveNumbersCounter(n: int):
    print("Ex4")

    if n == 0:
        return 0

    sum = 0
    d = 1

    # d -> dwójki, t -> trójki, f -> piątki

    while d <= n:

        t = d
        while t <= n:

            f = t
            while f <= n:
                sum += 1
                f *= 5

            t *= 3
        d *= 2

    return sum


def ex5SubNumbersCounter(n: int, divisor: int):
    print("Ex5")

    nLen = length(n)
    conditional = 0
    for i in range(nLen):
        conditional = 10 * conditional + 2

    print(n, conditional)

    mask = 0
    while mask != conditional:
        mask = 0
        for i in range(nLen):
            break

        break


#     nie wiem czy mogę to zrobic bez stringow


def ex6MinDifference(n: int):
    print("Ex6")

    iterator = int(sqrt(n))
    while iterator >= 1:
        if n % iterator == 0:
            print(iterator, n // iterator)
            return

        iterator -= 1


def ex7SequenceMultiplicity(n: int):
    print("Ex7")

    a = 1
    i = 1
    while a <= sqrt(n):
        a = i * i + i + 1
        if n % a == 0:
            return True

        i += 1

    for i in range(1, int(sqrt(n))):
        a = i * i + i + 1
        if n % a == 0:
            return True

    for i in range(int(sqrt(n)) - 1, 1, -1):
        a = i * i + i + 1
        if n % a == 0:
            return True

    return False


def ex8NoFiboSum(n: int):
    #     a(n+2) = suma(a1 -> an) + b
    # n=5 -> wynik = 9

    a = 1
    b = 1
    c = a + b
    sum = 0
    while a <= n:
        sum += a
        a = b
        b = c
        c = a + b

    a = b
    b = c
    c = a + b
    # a = a(n+2) w tym momencie

    print(a)

    d = a
    # wrocetu


def ex9Area(k: int):
    print("Ex9")

    p = 1
    n = 100 * k
    dx = (k - p) / n
    S = 0
    while p < k:
        p += dx
        S += dx * 1 / p

    return S


def ex10SequenceMultiplicity(n: int) -> bool:
    print("Ex10")

    a = 2
    while a <= sqrt(n):
        if n % a == 0:
            return True

        a = 3 * a + 1

    return False


def ex11RisingDigits(n: int) -> bool:
    print("Ex11")

    a = 10
    while n > 0:
        if n % 10 >= a:
            return False

        a = n % 10
        n = n // 10

    return True


def ex12ContainsEquivalence(n: int) -> bool:
    print("Ex12")

    nLen = length(n)

    if nLen > 9:
        return False

    while n > 0:
        if n % 10 == nLen:
            return True

        n = n // 10

    return False


def ex13UniqueDigit(n: int) -> bool:
    print("Ex13")

    nLen = length(n)
    last = n % 10
    for i in range(1, nLen):
        if n // (10 ** i) % 10 == last:
            return False

    return True


def ex14PrimeBuild(a: int, b: int) -> int:
    counter = 0

    return counter


def ex15N_digital(n: int) -> ():
    print("Ex15")
    rangeEnd = 0
    for i in range(n):
        rangeEnd += 9 * 10 ** i

    for number in range(10 ** (n - 1), rangeEnd):
        dSum = 0
        i = 0
        while i < length(number) and dSum <= number:
            dSum += (number // (10 ** i) % 10) ** n
            i += 1

        if dSum == number:
            print(number)


def prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def ex16SmithNumbers(n: int) -> ():
    print("Ex16")

    for k in range(2, n):
        sum1 = 0
        nLen = length(n)
        for l in range(nLen):
            sum1 += (k // (10 ** l)) % 10

        sum2 = 0
        for i in range(2, k + 1):

            if k % i == 0 and prime(i):
                number = k
                while number % i == 0:
                    j = i
                    while j > 0:
                        sum2 += j % 10
                        j //= 10

                    number //= i

        if sum1 == sum2:
            print(k, sum1, sum2)


def ex17tangentialMethodX_X(n: float) -> float:
    print("Ex17")

    eps = 0.000000001
    a = 0.0
    b = 10
    while abs(a - b) > eps:
        print(a, b)

        if ((a + b) / 2) ** ((a + b) / 2) <= n:
            a = (a + b) / 2

        if ((a + b) / 2) ** ((a + b) / 2) > n:
            b = (a + b) / 2

    return (a + b) / 2


def ex18ABSequences() -> ():
    print("Ex18")

    a0 = 0
    a1 = 1
    b0 = 2
    b1 = b0 + (2 * a0)

    while True:
        print("a0 =", a0)
        print("a1 =", a1)
        print("b0 = ", b0)
        print("b1 = ", b1)
        a2 = int(input("An = a(n-1) - b(n-1) * a(n-2)\n"))
        if a2 != a1 - b1 * a0:
            print("Actual An =", a1 - b1 * a0)
            break

        b1 = b1 + (2 * a1)
        a0 = a1
        a1 = a2
        print(b1)


def ex19FractionExpansion(a: int, b: int) -> ():
    print("Ex19")
    # działa tylko dla a i b w stosunku nie mniejszym niz 1 do 10

    # print(str(a // b) + ".", end="")
    # s = a * 10
    # while s // b == 0:
    #     print("0", end="")
    #     s *= 10
    #
    # entirePeriod = 0
    #
    # while True:
    #     period = 0
    #     a = a % b
    #     first = a
    #
    #     while True:
    #         copy = a
    #         a *= 10
    #         period = 10 * period + a // b
    #         a = a % b
    #
    #         if first == a or copy == a:
    #             break
    #
    #     entirePeriod = entirePeriod * (10 ** length(period)) + period
    #     if period != entirePeriod and entirePeriod % (10 ** length(period)) == period:
    #         finalPeriod = period
    #
    #         while entirePeriod % (10 ** length(period)) == period:
    #             entirePeriod //= 10 ** length(period)
    #
    #         if entirePeriod != finalPeriod and entirePeriod != 0:
    #             print(entirePeriod, end="")
    #
    #         break
    #
    # print("(" + str(finalPeriod) + ")")


def checkInSys(a: int, b: int, base: int):
    # nie posiadają żadnej wspólnej liczby, ŻADNEJ !!!

    while a > 0:
        digitA = a % base
        a //= base

        b2 = b
        while b2 > 0:
            digitB = b2 % base
            b2 //= base

            if digitA == digitB:
                return False

    return True


def ex20Systems(a: int, b: int):
    print("Ex20")

    i = 2
    while i <= 16:
        if checkInSys(a, b, i):
            return i
        i += 1

    return -1


if __name__ == '__main__':
    ex5SubNumbersCounter(2315, 7)
