import os
import glob
import rasterio

from . import raster

infolder = r"/home/jb/Downloads/s2"

scl_files = glob.glob(os.path.join(infolder,'*SCL*.jp2'))
with rasterio.open(scl_files[0]) as scl:
    meta = scl.meta.copy
    data = scl.read()
    data[data == 9] = 1

a=np.array(data)
np.ndarray(data)
