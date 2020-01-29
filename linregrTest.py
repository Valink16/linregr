from random import uniform
import matplotlib.pyplot as plt
import linregr
import pyfunc

xdata = []
ydata = []
with open('data.txt', 'r') as f:
    for l in f.readlines():
        l = l.split(' ')
        xdata.append(float(l[0]))
        ydata.append(float(l[1]))

plt.axis('equal')
for x,y in zip(xdata, ydata):
    plt.scatter(x, y)

r = linregr.Regressor(xdata, ydata)
print(r.regress())
plt.show()

