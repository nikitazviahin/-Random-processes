import seaborn as sns
from scipy import random
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import math as mt


def preciser(xi): #counting dispersion and expected value
    mat = []
    disp = []

    for i in range(len(xi)):
        mat.append(np.mean(xi[i])) 
        disp.append(np.var(xi[i]))

    return mat, disp


def formula(t, M):  #task function
    xi = 0
    for i in range(M):
        lmbd_i = mt.pi * i
        sgm = 1 / (1 + mt.pi * (i ** 2))
        eta = np.random.normal(0, sgm, 2)
        xi += mt.cos(lmbd_i * t) * eta[0] + \
              mt.sin(lmbd_i * t) * (eta[1])
    
    return xi


def sum_uniform(a, b, M, z):
    xi_vect_flex = []
    sg=[]
    t_flex = []
    for i in range(z):
        xi_vect = []
        t = np.arange(0, 1.01, 0.1)

        for i in range(len(t)):
            xi_vect.append(formula(t[i], M))

        t_flex.append(t)
        xi_vect_flex.append(xi_vect)

    mat, disp = preciser(xi_vect_flex)
    print('Значення мат. сподівання графіків:', mat,'\nЗначення дисперсії графіків:', disp)

    sns.set()
    plt.figure()
    for i in range(len(xi_vect_flex)):
        plt.plot(t_flex[i], xi_vect_flex[i], label='S0')
        plt.xlim(0, 1)

    plt.show()


if __name__ == "__main__":
    while(True):
        M = int(input('Введіть кількість точок:'))
        z = int(input('Введіть кількість графіків:'))
        a = 0
        b = 1
        sum_uniform(a, b, M, z)

        answer = input('Повторити?(y/n):')
        if answer == 'y':
            continue
        else:
            break
