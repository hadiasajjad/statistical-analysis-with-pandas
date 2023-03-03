#Three lines to make our compiler able to draw:
import sys
import matplotlib
import pandas as pd

import matplotlib.pyplot as plt
from scipy import stats
df = pd.read_csv('HR.csv');
x = df["lead_time"]
y = df["avg_price_per_room"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel, color=  "red")
plt.show()




