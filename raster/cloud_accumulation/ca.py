import os
import glob
import copy
import rasterio
import numpy as np

from raster import unique_values as uv

infolder = r"/home/jb/Downloads/s2"
outfile = r"/home/jb/Downloads/s2/out.tif"
scl_files = glob.glob(os.path.join(infolder,'*SCL*.jp2'))


def cloud_count_sen2cor(scl_list):
    """Counts pixels containing cloud and cloud shadow

    Parameters
    ----------
    scl_files : list
        List containing sen2cor scl file pathes
    Returns
    -------
    numpy data array containing counts and rasterio meta
    array, meta
    """
    for i, mask in enumerate(scl_files):
        print(os.path.basename(mask))
        with rasterio.open(scl_files[i]) as scl:
            meta = scl.meta.copy()
            data = scl.read(1)
        if i == 0:
            data_accum = copy.copy(data)
            data_accum[data_accum > -5] = 0
        data[data < 3] = 0
        data[data == 3] = 1
        data[data == 8] = 1
        data[data == 9] = 1
        data[data > 1] = 0
        data_accum += data

    return data_accum, meta

d, profile = cloud_count_sen2cor(scl_files)
uv.print_number_of_unique_pixels(d)

with rasterio.open(outfile, mode='w', **meta) as dst:
    dst.write(data_accum.astype(rasterio.uint8), 1)
