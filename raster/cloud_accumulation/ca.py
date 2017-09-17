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

cm_files = glob.glob(r"D:\Testing\sentinel\cloud_mask\33VUD\*33VUD*.tif")
outfile = r'D:\Testing\sentinel\cloud_mask\33VUD_cm_no_accum2.tif'

def cloud_count_owncloud(cm_files, cloud_count=False):
    """Counts pixels containing cloud and cloud shadow
        Assuming 0 for cloud and 1 for none cloud pixels

    Parameters
    ----------
    cm_files : list
        List containing sen2cor scl file pathes
    cloud_count : bool
        If True, number of occuring clouds is counted per pixel.
        If False, number of quality data (NO cloud) is counted per pixel.
    Returns
    -------
    numpy data array containing counts and rasterio meta
    array, meta
    """
    for i, mask in enumerate(cm_files):
        print(os.path.basename(mask))
        with rasterio.open(cm_files[i]) as scl:
            _data = scl.read(1)
            maxi = np.max(_data)
            mini = np.min(_data)
            if maxi > 1 or mini < 0:
                print('warning, skipping due to invalid data{}'.format(uni))
                continue
            if cloud_count:
                data = 1 - _data
            if not cloud_count:  # count good data
                data = _data
            print(np.min(data), np.max(data))
        if i == 0:
            meta = scl.meta.copy()
            data_accum = copy.copy(data)
        print(np.min(data_accum), np.max(data_accum))
        data_accum += data

    return data_accum, meta
accum, profile = cloud_count_owncloud(cm_files)
with rasterio.open(outfile, mode='w', **profile) as dst:
    dst.write(accum.astype(rasterio.int32), 1)
