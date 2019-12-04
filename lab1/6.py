import numpy as np
import math
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import pylab as pl
TemporaryNormalArray = []
arrayofmaximums = []

i=0
k=0

while k < 1000:  #заповнимо массив максимумами інших масивів
    while i < 1000:
        TemporaryNormalArray.append(random.normalvariate(0,1))#знаходимо максимум кожного массиву
        i += 1        #та додаємо його у массив максимумів
    arrayofmaximums.append(max(TemporaryNormalArray))
    TemporaryNormalArray = []
    i = 0
    k += 1
arrayofmaximums.sort()

fit = stats.norm.pdf(arrayofmaximums, np.mean(arrayofmaximums), np.std(arrayofmaximums))
pl.plot(arrayofmaximums,fit,'-o')
pl.hist(arrayofmaximums,density=True)
pl.show()
