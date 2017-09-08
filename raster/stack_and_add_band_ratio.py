import os
import numpy as np
import glob
import rasterio

from gis_utils.r import band_stacking as bs
from naer_tasks import rasterio_utils as ru

indir = r"C:\Users\juko\Downloads\tempp\align\*.tif"
outdir = r"C:\Users\juko\Downloads\tempp"
files = sorted(glob.glob(indir))
nr_bands = 6


infile_list = [files[0] , files[4]]
def add_difference_band(infile_list, outdir, creation_options={}):
    """Add a third band3=band1 - band2
    Parameters
    ----------
    infile : rasterio-readable
        input raster
    outfile : str
        path to output file
    creation_options : dict
        used to update profile
    """
    if len(infile_list) > 2:
        print('inputlist must be >2')


    with rasterio.open(files[0]) as src:
        profile = src.profile.copy()
        data1 = src.read()
    with rasterio.open(files[1]) as src:
        data2 = src.read()
    profile.update({'count': 6})
    profile.update(**creation_options)
    diff_b1 = data1[0].astype('f4') - data2[0].astype('f4')
    diff_b2 = data1[1].astype('f4') - data2[1].astype('f4')

    if np.issubdtype(data1.dtype, np.integer):
        diff_b1 = np.round(diff_b1)
    if np.issubdtype(data2.dtype, np.integer):
        diff_b2 = np.round(diff_b2)

    band3 = diff_b1.astype(data1.dtype)
    band6 = diff_b2.astype(data1.dtype)

    outfile = os.path.join(outdir, os.path.basename(infile_list[0])[:-4] +'_'+ os.path.basename(infile_list[1])[:-4]) + '.tif'
    print(outfile)
    with rasterio.open(outfile, 'w', **profile) as dst:

        dst.write_band(1, data1[0])  # 2015 B1
        dst.write_band(2, data1[1])  # 2015 B2
        dst.write_band(3, band3)
        dst.write_band(4, data2[0])  # 2017 B1
        dst.write_band(5, data2[1])  # 2017 B2
        dst.write_band(6, band6)
    print('done')


add_difference_band(infile_list, outdir)


infile_list = [files[0] , files[4]]
def add_difference_band(infile_list, outdir, creation_options={}):
    """Add a third band3=band1 - band2
    Parameters
    ----------
    infile : rasterio-readable
        input raster
    outfile : str
        path to output file
    creation_options : dict
        used to update profile
    """
    if len(infile_list) > 2:
        print('inputlist must be >2')


    with rasterio.open(files[0]) as src:
        profile = src.profile.copy()
        data1 = src.read()
    with rasterio.open(files[1]) as src:
        data2 = src.read()
    profile.update({'count': 3})
    profile.update(**creation_options)
    diff_b1 = data1[0].astype('f4') - data2[0].astype('f4')

    if np.issubdtype(data1.dtype, np.integer):
        diff_b1 = np.round(diff_b1)

    band3 = diff_b1.astype(data1.dtype)

    outfile = os.path.join(outdir, os.path.basename(infile_list[0])[:-4] +'_'+ os.path.basename(infile_list[1])[:-4]) + '.tif'
    print(outfile)
    with rasterio.open(outfile, 'w', **profile) as dst:

        dst.write_band(1, data1[0])  # 2015 B1
        dst.write_band(2, data2[0])  # 2015 B2
        dst.write_band(3, band3)

    print('done')


add_difference_band(infile_list, outdir)
