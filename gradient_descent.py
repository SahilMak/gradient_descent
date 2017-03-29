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
    batch(w0, w1, a, dataset)
    stochastic(w0, w1, a, dataset)


def batch(w0, w1, a, data):
    old0 = w0
    old1 = w1
    count = 0
    while count < 1000000:
        new0 = old0 + a * (summation(old0, old1, 1, data, 0))
        new1 = old1 + a * (summation(old0, old1, 1, data, 1))
        old0 = new0
        old1 = new1
        count += 1
        if (abs(w0 - new0) < 10**(-10)) and (abs(w1 - new1) < 10**(-10)):
            print("Weight 1: " + str(new0) + "\nWeight 2: " + str(new1))
            break
        if math.isinf(new0) or math.isinf(new1) or math.isnan(new0) or math.isnan(new1):
            print("Breaks at epoch " + str(count))
            break


def stochastic(w0, w1, a, data):
    old0 = w0
    old1 = w1
    count = 0
    while count < 1000000:
        new0 = summation(old0, old1, a, data, 0)
        new1 = summation(old1, old1, a, data, 1)
        old0 = new0
        old1 = new1
        count += 1
        if (abs(w0 - new0) < 10**-10) and (abs(w1 - new1) < 10**-10):
            print("Weight 1: " + str(new1) + "\nWeight 2: " + str(new1))
            break
        if math.isinf(new0) or math.isinf(new1) or math.isnan(new0) or math.isnan(new1):
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
