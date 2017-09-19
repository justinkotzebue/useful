# rasterio read/write
# reclass
import os
import glob
import rasterio
import numpy as np

inpath= r"\\dkcph1-ncr630\e$\juko_acolite\Ceaseless\Denmark\Vadehavet\Acolite\results_masked\final_rhos_to_spm_without_cm"
intif = glob.glob(os.path.join(inpath,'*20170324*.tif'))[0]
outtif = os.path.join(r"D:\Projects\FangarBay", os.path.basename(intif))

with rasterio.open(intif) as src:
    meta = src.meta.copy()
    data = src.read(1)
data[data > 10000] = np.nan
data[data < 0] = np.nan
with rasterio.open(outtif, mode='w', **meta) as dst:
    dst.write(data.astype(rasterio.float32),1)
