import numpy as np
import math
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import pylab as pl
arrnormal = []
arrmax = []
i=0
j=0

while j < 100:
    while i < 10:
        arrnormal.append(random.random())
        i += 1
    arrmax.append(max(arrnormal))
    arrnormal = []
    i = 0
    j += 1

arrmax = sorted(arrmax)
fit = stats.norm.pdf(arrmax, np.mean(arrmax), np.std(arrmax))
pl.plot(arrmax,fit,'-o')
pl.hist(arrmax,density=True)
pl.show()

