import numpy as np
import matplotlib.pyplot
import pylab
from numpy.polynomial import Polynomial
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

def reject_outliers(data, m = 3):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return data[s<m]

fig, ax = plt.subplots(figsize=(8, 4))

#  DATA
x1 = np.array([0.1, 0.3, 0.5 , 0.4, 0.3, 0.44, 0.22, 0.6, 0.8, 0.55,1,5,0,0.002])
x2_ = np.array(range(14))
x2_[8] = 0
x2_[4] = 20
len(x2_)
np.count_nonzero(x1)
np.count_nonzero(x2_)

table = pd.DataFrame(
    {'spm_coords':x1,
    'spm':x2_,
     })

table[table==0]=np.nan

reject_outliers(x1)

x = x1*x1
y1 = np.array(range(12))
y =[]
for i in y1:
    y.append(i*10)
# plot the data itself

len(x1)
#pylab.show()
fig.savefig(r'C:\Users\juko\Downloads\BLAAAAAAAAAAAAAAAA.png', dpi=125)


p = Polynomial.fit(x, y, 2)
p.
pnormal = p.convert(domain=(-1, 1))
#spm(rhos) A + Brhos + Crhos**
l = list(pnormal)

A, B, C = l[0], l[1], l[2]

y_pred = A**x + B*x + C
fit.predict(x)

ax.plot(x, y_pred, '-', color='darkorchid', linewidth=2)
fig.savefig('C:\Users\juko\Downloads\BLAAAA2.png', dpi=125)
np.min([y,x])


pylab.show()
