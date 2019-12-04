import numpy as np
import math
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import pylab as pl
arr1 = []
arr2 = []
arrgauss=[]
i=0
j=0
while i < 1000:
    arr1.append(random.random())
    i+=1
while j < 1000:
    arr2.append(random.random())
    j+=1
i=0
j=0
while i < 1000 and j < 1000:
    arrgauss.append(((math.log1p(arr1[i]))**(1/2))*(math.cos(2*math.pi*arr2[j])))
    i+=1
    j+=1

arrgauss = sorted(arrgauss)
fit = stats.norm.pdf(arrgauss, np.mean(arrgauss), np.std(arrgauss))
pl.plot(arrgauss,fit,'-o')
pl.hist(arrgauss,density=True)
pl.show()
print(arrgauss)

    
    
    
