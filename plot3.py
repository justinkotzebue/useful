
import rasterio

import colors
import numpy as np
import matplotlib.pyplot as plt

tif = r"\\ncr640\d$\FangarBay\Maps\T31TCF_20170307T105021_20170307T105019_SPM_NECHAD2016_664_derived_from_RHOS.tif"
with rasterio.open(tif) as r:
    data = r.read(1)


data[data>60]=np.nan
levels = [0, 1, 2, 3, 4, 5, 6, 7, 8]
plt.imshow(data)
#ax.contourf(data, levels)
plt.colorbar()
help(ax.contourf)
help(plt.colorbar)
plt.show()


data = np.tile(np.arange(4), 2)
fig = plt.figure()
ax = fig.add_subplot(121)
cax = fig.add_subplot(122)
cmap = colors.ListedColormap(['b','g','y','r'])
bounds=[0,1,2,3,4]
norm = colors.BoundaryNorm(bounds, cmap.N)
im=ax.imshow(data[None], aspect='auto',cmap=cmap, norm=norm)
cbar = fig.colorbar(im, cax=cax, cmap=cmap, norm=norm, boundaries=bounds,
     ticks=[0.5,1.5,2.5,3.5],)
plt.show()
