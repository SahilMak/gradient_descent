import math


def main():
    dataset = [
        [2, 5],
        [4, 7],
        [6, 14],
        [7, 14],
        [8, 17],
        [10, 19]
    ]
    w0 = 0.1
    w1 = 0.2
    a = 0.5
    # max = 1000000
    batch(w0, w1, a, dataset)
    stochastic(w0, w1, a, dataset)


def batch(t0, t1, a, data):
    t01 = t0
    t11 = t1
    count = 0
    while count < 3:
        print("t0: " + str(t0) + ", t01: " + str(t01))
        t01 = t01 + a * (summation(t01, t11, 1, data, 0))
        t11 = t11 + a * (summation(t01, t11, 1, data, 1))
        count += 1
        print("t0: " + str(t01) + ", t1: " + str(t11) + ", " + str(count))
        if (abs(t0 - t01) < 10**-10) and (abs(t1 - t11) < 10**-10):
            print("Weight 1: " + str(t01) + "\nWeight 2: " + str(t11))
            break
        if math.isinf(t01) or math.isinf(t11) or math.isnan(t01) or math.isnan(t11):
            print("Breaks at epoch " + str(count))
            break


def stochastic(t0, t1, a, data):
    t01 = t0
    t11 = t1
    count = 0
    while count < 1000000:
        # print("t0: " + str(t01) + ", t1: " + str(t11) + ", " + str(count))
        t01 = summation(t01, t11, a, data, 0)
        t11 = summation(t11, t11, a, data, 1)
        count += 1
        if (abs(t0 - t01) < 10**-10) and (abs(t1 - t11) < 10**-10):
            print("Weight 1: " + str(t01) + "\nWeight 2: " + str(t11))
            break
        if math.isinf(t01) or math.isinf(t11) or math.isnan(t01) or math.isnan(t11):
            print("Breaks at epoch " + str(count))
            break


def summation(t0, t1, a, data, num):
    total = 0
    if num == 0:
        for i in range(len(data)):
            total += a * (data[i][1] - hw(t0, t1, data[i][0]))
    else:
        for i in range(len(data)):
            total += a * (data[i][1] - hw(t0, t1, data[i][0])) * data[i][0]
    return total


def hw(t0, t1, x):
    return t0 + t1 * x

main()
