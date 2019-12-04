import math
import random
import matplotlib.pyplot as plt

values = []
N = 150

for value in range(N):
    function = 0
    for i in range(value):
        tetaFirst = random.randint(0, 1)
        tetaSecond = 1 /((1 + math.pi * (i**2))**5)
        function += (math.cos(i * math.pi ) * tetaFirst + math.sin(i * math.pi)*tetaSecond)
    values.append(function)
plt.hist(values,density=True)
plt.show()