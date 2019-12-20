import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random


def puass(rn, st):  
    return - (1/3)*np.log(np.array(rn[:st]))


def absorb_stats(mx, vr, rn, st, fst, scd):
    i_mx = np.array([[1, 0], [0, 1]])  
    q_mx = np.array([[mx[0][0], mx[0][1]], [mx[1][0], mx[1][1]]])  
    m_mx = np.linalg.inv(i_mx - q_mx) 
    r_mx = np.array([[mx[0][2]], [mx[1][2]]])  
    print(r_mx)
    xi_v = np.array([[1], [1]]) 
    zeta = np.dot(m_mx, xi_v) 
    print('\nФундаментальна матриця:')
    for i in range(len(m_mx)):
            for j in range(len(m_mx[i])):
                print(m_mx[i][j], end=' ')
            print('\n')
    full_time = np.sum(puass(rn, st-1))  
    full_fst = np.sum(puass(fst, st)) 
    full_scd = np.sum(puass(scd, st)) 
    print('\nЕкспериментальний час для стану 1 = {}'.format(full_fst),'\nЕкспериментальний час для стану 2 = {}'.format(full_scd),
          '\nТеоритичний час для стану 1 = {}'.format(m_mx[0][0]),'\nТеоритичний час для стану 2 = {}'.format(m_mx[1][1]),
          '\nЕкспериментальний час поглинання = {}'.format(full_time),'\nТеоретичний час поглинання = {}'.format(np.amin(zeta)))
          
    
   


def lawn_moving(mtrx, rn, res, st, fst, scd):
    k = 0
    z = 2
    while st != 2:
        if rn[k] < mtrx[st][0] and rn[k+1] > 0:
            res.append('State_0 =>')
            fst.append(rn[k+1])
            in_state = 0
        elif rn[k] > mtrx[st][0] and rn[k+1] <= (mtrx[st][0] + mtrx[st][1]):
            res.append('State_1 =>')
            scd.append(rn[k+1])
            in_state = 1
        else:
            res.append('State_2 =>')
            in_state = 2
            
            break
        z += 1
        k += 1
    res.append(' stop')

    return res, z, fst, scd


def absorbing_chain(in_state):
    modelled_way = []
    fst = []
    scd = []
    rn = np.random.uniform(0,1,size = 10000)
    initial_vector = [0.3, 0.5, 0.2]
    if in_state != -1:
        semi = 'S' + str(in_state) + ' -> '
        modelled_way.append(semi)
        if in_state == 0 or in_state == 1:
            fst.append(rn[0])
    else:
        if rn[0] < initial_vector[0] and rn[0] >= 0:
            modelled_way.append('State_0 =>')
            fst.append(rn[0])
            in_state = 0
        elif rn[0] > initial_vector[0] and rn[0] <= (initial_vector[0] + initial_vector[1]):
            modelled_way.append('State_1 =>')
            scd.append(rn[0])
            in_state = 1
        else:
            modelled_way.append('State_2 =>')
            in_state = 2

    prob_matrix = [[0.39, 0.32, 0.29],
                   [0, 0.34, 0.66   ],
                   [0, 0, 1         ]]
    if in_state == 2:
        print('Початкові ймовірності: ', initial_vector,)
        print('Матриця ймовірностей:')
        for i in range(len(prob_matrix)):
            for j in range(len(prob_matrix[i])):
                print(prob_matrix[i][j], end=' ')
        print()
        print('Змодельований ланцюг:', ''.join(modelled_way))
        step = 1
        print('\nПотрапляння в поглинаючий стан!\n')
    else:
        final_modelled_way, step, fst, scd = lawn_moving(prob_matrix, rn, modelled_way, in_state, fst, scd)
        print('Початкові ймовірності: ', initial_vector,)
        print('Матриця ймовірностей:')
        for i in range(len(prob_matrix)):
            for j in range(len(prob_matrix[i])):
                print(prob_matrix[i][j], end=' ')
            print('\n')
        print()
        print('Змодельований ланцюг:', ''.join(modelled_way))
        print('\nПотрапляння в поглинаючий стан!\n')
    y = input('Знайти характеристи поглинаючого ланцюга?(y|n):')
    if y == 'y':
        absorb_stats(prob_matrix, initial_vector, rn, step, fst, scd)



while(True):
    s = input('Обрати початковий стан?(y|n)')
    if s == 'y':
        in_state = int(input('Оберіть початковий стан(від 0 до 2):'))
        absorbing_chain(in_state - 1)
    else:
        absorbing_chain(-1)
    answer = input('Повторити операцію?(y/n):')
    if answer == 'y':
        continue
    else:
        break
