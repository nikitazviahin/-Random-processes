import numpy as np
import random

def lawn_moving(mtrx, rn, res, st):
    for k in range(len(rn) - 1):
        if rn[k] < mtrx[st][0] and rn[k] > 0:
            res.append('State_0 => ')
            in_state = 0
        elif rn[k] > mtrx[st][0] and rn[k] <= (mtrx[st][0] + mtrx[st][1]):
            res.append('State_1 => ')
            in_state = 1
        else:
            res.append('State_2 => ')
            in_state = 2
   
    return res 


def usual_chain(in_state):
    modelled_way = []
    rn = np.random.uniform(0,1,size = 11)
    print("Значення альфа: ")
    for j in range(len(rn)):
        print(rn[j], end=' ')
        print()
    initial_vctr = [0.3, 0.5, 0.2]
    if in_state != -1:
        initial = 'State_' + str(in_state) + ' => '
        modelled_way.append(initial)
    else:
        if rn[0] < initial_vctr[0]:
            modelled_way.append('State_0 => ')
            in_state = 0
        elif rn[0] > initial_vctr[0] and rn[0] <= (initial_vctr[0] + initial_vctr[1]):
            modelled_way.append('State_1 => ')
            in_state = 1
        else:
            modelled_way.append('State_2 => ')
            in_state = 2
        

    prob_matrix = [[0.1,0.2,0.7],
                   [0.3,0.6,0.1],
                   [0.6,0.2,0.2]]
    
    final_result = lawn_moving(prob_matrix, rn, modelled_way, in_state)
    print('Початкові ймовірності: \n', initial_vctr)
    print('Матриця ймовірностей:')
    for i in range(len(prob_matrix)):
        for j in range(len(prob_matrix[i])):
            print(prob_matrix[i][j], end=' ')
        print()
    print('Змодельований ланцюг:', ''.join(modelled_way))


while(True):
        s = input('Обрати початковий стан?(y/n)')
        if s == 'y':
            in_state = int(input('Оберіть початковий стан(від 0 до 2):'))
            usual_chain(in_state)
        else:
            usual_chain(-1)
        answer = input('Повторити операцію?(y/n):')
        if answer == 'y':
            continue
        else:
            break
