import os
import re
import glob
import copy
import rasterio
import numpy as np

from raster import unique_values as uv


# Cloud cover [%] on:
# - land
# - water

def chain_count(mask_list, outfolder, start_time, end_time):
    time_list = filter_list_by_time_window(mask_list, start_time, end_time)
    unique_tiles = get_unique_tiles_from_list(time_list)
    print('processing {} files'.format(len(unique_tiles)))
    for tile_id in unique_tiles:
        regex = re.compile(".*("+ tile_id +").*")
        tile_filtered = [m.group() for l in time_list for m in [regex.search(l)] if m]

        outfile = os.path.join(outfolder, tile_id + '_' + str(start_time) + '_' + str(end_time) + '.tif')
        print(outfile)
        accum, profile = cloud_count_owncloud(tile_filtered)
        with rasterio.open(outfile, mode='w', **profile) as dst:
            dst.write(accum.astype(rasterio.int32), 1)


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




def filter_list_by_time_window(listscenes, start_time=None, end_time=None):
    """Filters list by start and end date, which must be part of the list

    Parameters
    ----------
    list : list
        list to be filtered by date
    start_time : int
        e.g. 20170808
    end_date : int
        e.g. 20170809
    Returns
    -------
    filtered list

    """

    if start_time > end_time:
        raise ValueError('sart time must be before end time!')
    if start_time:
        listscenes = [x for x in listscenes if int(re.search(8*'\d', os.path.basename(x)).group(0)) >= start_time]
    if end_time:
        listscenes = [x for x in listscenes if int(re.search(8*'\d', os.path.basename(x)).group(0)) <= end_time]

    return listscenes


def get_unique_tiles_from_list(cm_list):
    tiles = []
    for i in cm_list:
        pathSAFE = os.path.basename(i)
        tile = re.search('\D\d\d\D\D\D', pathSAFE).group(0)
        tiles.append(tile)

    return np.unique(tiles)


def tci_cloud_count_sen2cor(scl_list):
    """Counts pixels from TCI product in sen2cor folder
    containing cloud and cloud shadow

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



infolder = r"\\ncr104\d$\NAER\S2\cloudmask_sept\final"
# outfile = r"/home/jb/Downloads/s2/out.tif"
mask_list = glob.glob(os.path.join(infolder,'*.tif'))
outfolder = r"D:\Testing\cloud_count"

chain_count(mask_list, outfolder, start_time=20170912, end_time=20171005)
