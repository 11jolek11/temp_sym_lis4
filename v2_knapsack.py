import math
from math import sqrt, floor
from random import uniform, getrandbits
from scipy.special import comb
from numpy import array



import math
from math import sqrt, floor
from scipy.special import comb
import numpy as np


max_w = 300
a=2.30718
b=3.69282
sigma = 0.16
mi = 3

a = mi - sqrt(3)*sigma
b = mi + sqrt(3)*sigma

f_inverse = lambda: sigma * sqrt(3) * (2 * uniform(0, 1) - 1) + mi

total = []
for x in range(1000):
    positive = 0
    for n in range(1000):
        # generujemy n razy x wag
        # temp = np.random.uniform(a, b, x+1)


        # temp = np.random.uniform(a, b, x)


        temp = [f_inverse() for _ in range(x)]
        # sprawdzamy warunek
        if sum(temp) <= max_w:
            positive += 1
    # ilosc_mozliwosci_wyboru = math.comb(1000, x+1)
    ilosc_mozliwosci_wyboru = comb(1000, x, exact=True)
    # monte caro tutaj:
    part = (positive/1000)*ilosc_mozliwosci_wyboru
    total.append(part)
print(sum(total))