# import math
# from math import sqrt, floor
# from random import uniform, getrandbits
# from scipy.special import comb
# from numpy import array
# c = 0
# cs = []
# total = []

# sigma = 0.16
# mi = 3

# f_inverse = lambda: sigma * sqrt(3) * (2 * uniform(0, 1) - 1) + mi
# for i in range(1000):  # ilosc przedmiotow pakowanych
#     hits = 0
#     for itr in range(100):  # powtorzenia losowania
#         total_wage = sum([f_inverse() for _ in range(i)])
#         hits += 1 if total_wage <= 300 else 0  # suma < plecak
#     cmb = comb(1000, i, exact=True)
#     #FIXME: i monte carlo tutaj
#     calc = hits / 1000 * cmb  # ilosc trafien/proby * (ilosc kombinacji)

#     cs.append(calc)
#     total.append(cmb)
#     c += calc
# # print([x[0] / x[1] for x in zip(cs, total)])
# # print(cs)
# # print(sum(total))
# print(c)




















import math
import random
from scipy.special import comb


def generuj(sigma = 0.16, mi = 3):
    mi = 3
    return sigma * math.sqrt(3) * (2 * random.uniform(0, 1) - 1) + mi


def solutions():
    counter = 0
    weight_boundry = 300
    cs = []
    total = []
    for i in range(1000):  # dla >110 przedmiotow 0%
        correct = 0
        for _ in range(1000):  # powtorzenia losowania
            total_waga = sum([generuj() for _ in range(i)])
            if total_waga <= weight_boundry:
                correct += 1
        combinations = comb(1000, i, exact=True)
        calc = (correct/1000) * combinations  # ilosc trafien/proby * (ilosc kombinacji)

        cs.append(calc)
        total.append(combinations)
        counter += calc

    print(f'2^{math.log(counter, 2)}')
    print('lub')
    print(counter)

solutions()






























































# import math
# import random
# from scipy.special import comb


# def uniform_dist():
#     sigma = 0.16
#     mi = 3
#     return sigma * math.sqrt(3) * (2 * random.uniform(0, 1) - 1) + mi


# def z1():
#     # N = 1000
#     b = 300
#     c = 0
#     cs = []
#     total = []
#     for i in range(111):  # dla >110 przedmiotow 0%
#         hits = 0
#         for itr in range(100):  # powtorzenia losowania
#             total_wage = sum([uniform_dist() for _ in range(i)])
#             hits += 1 if total_wage <= b else 0  # suma < plecak
#         cmb = comb(1000, i, exact=True)
#         calc = hits / 100 * cmb  # ilosc trafien/proby * (ilosc kombinacji)

#         cs.append(calc)
#         total.append(cmb)
#         c += calc

#     # print([x[0] / x[1] for x in zip(cs, total)])
#     # print(cs)
#     # print(total)
#     print('z1')
#     print(f'średnia ilośc rozwiązań: 2^{math.log(c, 2)}')

# z1()