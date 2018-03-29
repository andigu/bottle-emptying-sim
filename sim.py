from math import *

total_height = 0.5
g = 9.8
P_0 = 101325
water_density = 1000
air_density = 1.225


def next_height(old_height, r_ratio):
    b = P_0 + total_height * water_density * g * r_ratio
    return (b - sqrt(b * b - 4 * water_density * g * r_ratio * P_0 * old_height)) / (2 * water_density * g * r_ratio)


def period(old_height, new_height, r_ratio):
    return 2 * sqrt(3 * r_ratio * (old_height - new_height) / (2 * g)) + sqrt(
        2 * air_density / water_density * new_height)


def xrange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


matr = [[], [], [], []]
for ratio in range(10, 30, 5):
    for h_0 in xrange(0.1, 0.5, 0.01):
        h = h_0
        total_time = 0
        while h > 0.01:
            h_N = next_height(h, ratio)
            T = period(h, h_N, ratio)
            total_time += T

            h = h_N

        print(round(h_0, 2), total_time - 2 * ratio * h_0 / 5)
        matr[int((ratio - 10) / 5)].append(total_time - 2 * ratio * h_0 / 5)


def fout(x, n_digits):
    return format(round(x, n_digits), "." + str(n_digits) + "f")


for i in range(len(matr[0])):
    print(format(round(0.1 + i * 0.01, 2), ".2f"), fout(matr[0][i], 16), fout(matr[1][i], 16), fout(matr[2][i], 16),
          fout(matr[3][i], 16))
