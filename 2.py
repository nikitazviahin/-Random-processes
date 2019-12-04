import random
import numpy
import math
arr1 = []
funcarr1 = []
i = 0
x = 0
while i<100000: #чим більше значення, тим більша точність
    arr1.append(random.random()) #заповнюємо массив випадковими числами з нашого проміжку [0,1]
    i += 1                       #для першого інтегралу       
i = 0
while i<100000:
    x = arr1[i]
    funcarr1.append(x**7+x**5+x**3) #рахуємо для кожного отриманого випадкового числа з проміжку значення функції
    i += 1
average = numpy.mean(funcarr1)  #рахуємо середнє з отриманих значень функції
result = (1-0)*average #множимо довжину відрізку на середнє значення функції
print("Значення першого інтегралу ",result)

arr1 = []
funcarr1 = []
i = 0
x = 0
while i<100000: 
    arr1.append(random.uniform(0,math.pi)) 
    i += 1                       #для другого інтегралу       
i = 0
while i<100000:
    x = arr1[i]
    funcarr1.append(2*math.sin(3*x)) 
    i += 1
average = numpy.mean(funcarr1)  
result = (math.pi - 0)*average 
print("Значення другого інтегралу ",result)


arr1 = []
funcarr1 = []
i = 0
x = 0
while i<1000000: 
    arr1.append(random.uniform(0.001,1000000)) 
    i += 1                       #для третього інтегралу
i=0
while i<1000000:
    x = arr1[i]
    funcarr1.append((1/((x+1)*(x**(1/2)))))
    i += 1
average = numpy.mean(funcarr1)  
result = (1000000)*average


print("Значення третього інтегралу ",result)








