import os
import glob
import gdal
import shutil
import tempfile

import gdal_utils.gdal_utils as gu

# infiles = r"\\dkcph1-ncr630\e$\juko_acolite\SeaStatus\RoskildeFjord\Acolite\results_raw\*20170301*RHOS_664.tif"
# glob.glob(infiles)
def mosaic_reproject_subset(infiles, outfile, prescale=None, maskfunc=None,
                            tr=None, extent=None, outsize=None):
    """Mosaic, reproject, and subset the infiles and save as .tif
    Parameters
    ----------
    infiles : list of str
        list of input files (can be GDAL strings)
    outfile : str
        path to output netCDF file
    prescale : str
        pre-scale the input data to reduce file sizes
        e.g. '50%'
    maskfunc : function
        mask values in input files with this function
        see `mask_values` function docs for details
    tr : float, int
        target resolution
    extent : list of float or comma-separated string
        exent to subset image to
        xmin, xmax, ymin, ymax
    outsize : [str, str]
        down-scale the final (mosaiced, reprojected) image
        e.g. ['50%', '0%'] for 50% down-scaling
    """
    tempdir = tempfile.mkdtemp()

        # Mosaic input files to VRT
    print("Mosaicing...")
    tempfile_mosaic = os.path.join(tempdir, 'mosaic.vrt')
    gu.buildvrt(infiles_tif_masked, tempfile_mosaic)

    # Reproject to WGS84
    print("Reprojecting to geographic coordinates ...")

    tempfile_reproj = os.path.join(tempdir, 'mosaic_WGS84.vrt')
    gu.warp(tempfile_mosaic, outfile=tempfile_reproj,
            t_srs='EPSG:4326', r='bilinear')

    # Subset to given extent and save as NetCDF
    print("Subsetting ...")

    if not extent or extent == _global_extent:
        bufferedExtent = _global_extent
    else:
        # buffer extent
        with gu.gdal_open(tempfile_reproj) as fp:
            geotransform = fp.GetGeoTransform()
        bufferedExtent = gu.buffer_extent(extent, geotransform)

    extra = []
    if tr:
        extra = ['-tr'] + [str(tr)]*2
    gu.translate(tempfile_reproj, outfile=outfile, of='GTiff',
            extent=bufferedExtent, outsize=outsize, extra=extra)
    try:
        shutil.rmtree(tempdir)
    except OSError:
        print('Unable to delete temporary directory \'{}\'. Please remove manually.'.format(tempdir))

    return outfile
