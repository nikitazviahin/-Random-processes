from scipy.stats import chisquare #імпортуємо тест Пірсона
import random as rd
testarr = []
i=0
while i<25: #заповнюємо массив псевдовипадковими числами
    testarr.append(rd.random())
    i += 1
                     
result = chisquare(testarr)   #другий елемент result буде рівень значущості на якому виконується наша гіпотеза                 
print("Гіпотеза про рівномірний розподіл виконується на рівні значущості ", result[1])
print(testarr)




