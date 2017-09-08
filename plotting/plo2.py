import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pylab


#x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
#y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])

x1 = np.array([0.1, 0.3, 0.55 , 0.55, 0.3, 0.44, 0.22, 0.6, 0.8, 0.55]).reshape(2,5)

t1 = x1==0.55
t2 = ~t1
t2.astype(int)
t2 * 1

x = x1*x1
y1 = np.array(range(10))
y =[]
for i in y1:
    y.append(i*10)


def plot_poly_fit(x, y, poly_fit=3, title=[""], save_path=[]):
    p30 = np.poly1d(np.polyfit(x, y, poly_fit))
    p = np.poly1d(p30)
    l = p.coeffs

    coefficient_of_dermination = r2_score(y, p(x))
    l_x = np.max(x)
    xp = np.linspace(0, l_x, 10)

    p.

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.scatter(x, y, alpha=0.5, color='orchid')
    #fig.suptitle(title + ' poly=' + str(poly_fit) + ' Rsq=' + str(round(coefficient_of_dermination,3)))

    fig.tight_layout(pad=2);
    ax.grid(True)

    ax.plot(x, y, '.', xp, p30(xp), '--', color='darkorchid', linewidth=2)
    if save_path:
        fig.savefig(save_path[0], dpi=125)

    pylab.show()

    return l, coefficient_of_dermination

plot_poly_fit(x, y, poly_fit=3, save_path=[r'C:\Users\juko\Downloads\1a.png'])
