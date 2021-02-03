import sqlite3
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

conn = sqlite3.connect("covid.db")
cur = conn.cursor()
date = cur.execute("select strftime('%m', Date) from covid").fetchall()
deaths = cur.execute("select Deaths from covid").fetchall()
state = cur.execute("select State from covid").fetchall()
population = cur.execute("select Population from covid").fetchall()
county = cur.execute("select County from covid").fetchall()
confirmed = cur.execute("select Confirmed from covid").fetchall()




x = []
y = []
yy = []

for i in date:
    x.append(int(i[0]))

for i in confirmed:
    y.append(int(i[0]))

for i in deaths:
    yy.append(int(i[0]))

plt.plot(x,y)
plt.plot(x,yy)
plt.legend(['confirmed','deaths'])
plt.show()
