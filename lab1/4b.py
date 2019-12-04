import numpy as np
import math
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import pylab as pl

arr1 = []
arrgauss=[]
i=0
j=0
forarr=0
n = int(input("Enter n: "))
while i < n*1000:
    arr1.append(random.random())
    i+=1
i=0
while i < n*1000:
    
    while j < n:
        forarr += arr1[i]-1/2
        i += 1
        j += 1
        
    j=0    
    arrgauss.append(((12/n)**(1/2))*forarr)
    forarr = 0    

arrgauss = sorted(arrgauss)
fit = stats.norm.pdf(arrgauss, np.mean(arrgauss), np.std(arrgauss))
pl.plot(arrgauss,fit,'-o')
pl.hist(arrgauss,density=True)
pl.show()
print(arrgauss)
