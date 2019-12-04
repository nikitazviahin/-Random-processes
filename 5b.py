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
while i < 12000:
    arr1.append(random.random())
    i+=1
i=0
while i < 12000:
    
    while j < 12:
        forarr += arr1[i]-1/2
        i += 1
        j += 1
        
    j=0    
    arrgauss.append(((12/12)**(1/2))*forarr)
    forarr = 0
    

result = stats.shapiro(arrgauss)              
print("Гіпотеза про нормальний розподіл при n = 12 виконується на рівні значущості ", result[1])

while i < 48000:
    arr1.append(random.random())
    i+=1
i=0
while i < 48000:
    
    while j < 48:
        forarr += arr1[i]-1/2
        i += 1
        j += 1
        
    j=0    
    arrgauss.append(((12/48)**(1/2))*forarr)
    forarr = 0
    

result = stats.shapiro(arrgauss)              
print("Гіпотеза про нормальний розподіл при n = 48 виконується на рівні значущості ", result[1])

while i < 3000:
    arr1.append(random.random())
    i+=1
i=0
while i < 3000:
    
    while j < 3:
        forarr += arr1[i]-1/2
        i += 1
        j += 1
        
    j=0    
    arrgauss.append(((12/3)**(1/2))*forarr)
    forarr = 0
    

result = stats.shapiro(arrgauss)              
print("Гіпотеза про нормальний розподіл при n = 3 виконується на рівні значущості ", result[1])

