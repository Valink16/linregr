import pyfunc
from random import uniform

f = pyfunc.LinearFunction(-4.555, 56)
deviation = 0.05 # deviation from exact data(imitates measurement errors)
length = 50

n1, n2 = 1 - deviation, 1 + deviation
data = [(str(x * uniform(n1, n2)), str(f.image(x) * uniform(n1, n2))) for x in range(length)]

with open('data.txt', 'w') as f:
    data = [' '.join(d) + '\n' for d in data]
    f.writelines(data)