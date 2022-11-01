import math
import time


def fibonacci(range: int):
    a = 1
    b = 1

    while a < range:
        print(a)
        c = a + b
        a = b
        b = c


def fibonacciWithYear(year: int):
    a = 1
    b = 1

    while a < year / 2:
        c = a + b
        a = b
        b = c

    b = 1579 - (b - 2022)
    a = 2022


def prime(a: int):
    if a < 2:
        return False

    if a == 2:
        return True

    if a % 2 == 0:
        return False

    iterator = 3
    while iterator * iterator <= a:
        if a % iterator == 0:
            return False

        iterator += 2

    return True


def numbersSum(a: int):
    currentSum: int = 0
    while a > 0:
        currentSum += a % 10
        a = a // 10

    return currentSum


def primeWithSumOfNumbers101():
    startTime = time.time()

    iterator = 299_999_999_999
    currAdd = 9
    deficit = 1

    addAgain = False
    counter = 0

    while True:
        if numbersSum(iterator) == 101:
            print(iterator)
            if prime(iterator):
                counter += 1
                if counter == 2:
                    break

        if addAgain:
            for i in range(1, 10 - deficit):
                iterator += currAdd * (10 ** i)

            for i in range(9, 9 - deficit, -1):
                iterator += (currAdd - deficit + 1) * (10 ** i)

            addAgain = False

        if iterator % 100_000_000_000 == 1:
            print(iterator)

            for i in range(1, 11 - deficit):
                iterator += currAdd * (10 ** i)

            for i in range(10, 10 - deficit, -1):
                iterator += (currAdd - deficit) * (10 ** i)

            addAgain = True
            deficit += 1

        iterator += 2

    endTime = time.time()

    print(endTime - startTime)


def shit():
    a = 1
    b = 1
    year = 2022

    while a < year / 2:
        c = a + b
        a = b
        b = c

    b = year / 2 - (abs(a - year) / 2)
    a = year

    while True:
        print(a, b)
        c = a - b
        if c <= 0:
            break
        a = b
        b = c

    print(a, b)


def exSubsequenceWithSum(n: int):
    print("Ex3 z1")

    a = 1
    b = 1
    c = a + b
    sum = 0
    while sum < n:
        sum += a
        a = b
        b = c
        c = a + b

    a = 1
    b = 1
    c = a + b
    while sum > n:
        sum -= a
        a = b
        b = c
        c = a + b

    return sum == n


def subsequence(s: int):
    if s == 1:
        print(1)
        return

    a = 1
    b = 1

    while b < s:
        e = a
        f = b

        mySum = e + f
        while f < s and mySum < s:
            g = e + f
            e = f
            f = g
            mySum += g

        if mySum == s:
            print("Subsequence elements:")
            c = a + b
            while c < mySum:
                print(a)
                c = a + b
                a = b
                b = c
            return

        c = a + b
        a = b
        b = c

    print("No such a subsequence")


def fibonacciSum(elements: int):
    if elements == 1:
        return 1

    a = 1
    b = 1

    sum = a + b
    counter = 2

    while counter < elements:
        c = a + b
        a = b
        b = c

        sum += c
        counter += 1

    return sum


def NWD_2(a: int, b: int):
    while b != 0:
        c = a % b
        a = b
        b = c

    return a


def NWD_3(a: int, b: int, c: int):
    return NWD_2(a, NWD_2(b, c))


def NWW_3(a: int, b: int, c: int):
    return a * b * c / NWD_3(a, b, c)


def cosinus(x: float):
    result = 1.0
    denominator = 1
    sign = 1
    currX = 1

    for n in range(1, 10, 1):
        denominator *= 2 * n * ((2 * n) - 1)
        currX *= x * x
        print(result, n, denominator)

        sign *= (-1)
        result += sign * currX / denominator

    # NWW1 = a * b / NWD_2(a, b)
    # print(NWW1)
    # NWW2 = NWW1 * c / NWD_2(NWW1, c)
    # print(NWW2)

    return result


def definePi(iterations: int):
    x = (1 / 2) ** (1 / 2)
    product = x
    for i in range(iterations):
        x = ((1 / 2) + (1 / 2) * x) ** (1 / 2)
        product *= x

    #     product = 2 / pi

    return 2 / product


def steps(n: int):
    stepsCounter = 0
    while n != 1:
        n = (n % 2) * (3 * n + 1) + (1 - n % 2) * n / 2
        stepsCounter += 1

    return stepsCounter


def mostSteps(a, b):
    most = 0
    element = 0
    while a <= b:
        x = steps(a)

        if x > most:
            most = x
            element = a

        a += 1

    return element


def fibonacciWithInitials(range: int, a: int, b: int):
    while a < range:
        print(a)
        c = a + b
        a = b
        b = c

    print(a)


def fibonacciLimWithInitials(iterations: int, a: int, b: int):
    product = a * b
    for i in range(iterations):
        c = a + b
        a = b
        b = c
        product = a * b

    return product


def euler(iterations: int):
    e = 2
    denominator = 1
    for i in range(2, iterations):
        denominator *= i
        e += (1 / denominator)

    return e


def fiboYear(year: int):
    minA = 2222
    minB = 1111

    for a in range(1, int(year / 2)):

        for b in range(1, int(year / 2)):

            e = a
            f = b
            g = e + f
            while g <= year:
                g = e + f
                e = f
                f = g

            if e == year:
                if a + b < minA + minB:
                    minA = a
                    minB = b

    print(minA, minB)


if __name__ == '__main__':
    fibonacci(fibonacciSum(17))  # wynik wychodzi 2584

    print(fibonacciSum(16))  # wynik wychodzi 2583
    # sprawdza się dla każdej pary liczb różnej o 1
    # trzeba policzyć dlaczego

    # suma ciągu skróconego o dwa ostatnie elementy = ostatni element - 1


    primeWithSumOfNumbers101()
