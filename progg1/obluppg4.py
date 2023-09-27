import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from uppgift2 import Smooth


def load_csv(filename: str):
    with open(filename) as csvFile:
        reader = csv.reader(csvFile)
        rows = []
        for row in reader:
            rows.append(row)
    return rows

data = load_csv('CO2Emissions_filtered.csv')
edata = {v[1].lower(): [float(k) for k in v[3:]] for v in data}


#print(edata['country code'])
fig, ax = plt.subplots()
norden = {'dnk': ['r:','r-','r-.','Denmark'],
          'fin': ['b:','b-','b-.','Finland'],
          'isl': ['g:','g-','g-.','Iceland'],
          'nor': ['k:','k-','k-.','Norway'],
          'swe': ['y:','y-','y-.','Sweden']
          }

reduced_x = edata['country code'][5:-5]

for code in norden:
    smoothed_data = Smooth.smooth_a(edata[code].copy(), 5)
    ax.plot(edata['country code'], edata[code], norden[code][0])
    ax.plot(edata['country code'], Smooth.smooth_b(edata[code],5), norden[code][1], label=norden[code][3])
    ax.plot(edata['country code'], smoothed_data, norden[code][2])
    

#ax.grid(linestyle='-', linewidth=0.5)
ax.legend(loc = 'upper right', fontsize = 'small')
plt.xlabel('Year')
plt.ylabel('CO2 emissions [kt]')
plt.title('CO2 emissions for the nordic countries from 1960 to 2015')
plt.show()


#print(ccodes)

        
