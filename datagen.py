import pyfunc
from random import uniform

f = pyfunc.LinearFunction(42, -55)
deviation = 0 # deviation from exact data(imitates measurement errors)
length = 20

n1, n2 = 1 - deviation, 1 + deviation
data = [(str(x * uniform(n1, n2)), str(f.image(x) * uniform(n1, n2))) for x in range(length)]

with open('data.txt', 'w') as f:
    data = [' '.join(d) + '\n' for d in data]
    f.writelines(data)