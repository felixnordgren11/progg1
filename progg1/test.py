import csv
import matplotlib.pyplot as plt
from math import *

L = 100
time = list(range(L))
vlts = [sin(2*pi*t/L) for t in time]

fig, ax = plt.subplots()
ax.plot(time, vlts)
ax.set(xlabel='time [s]', ylabel='vlts [mV]')
plt.show()