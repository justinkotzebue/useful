import glob
import rasterio
from rasterio.enums import Resampling
from rasterio.vrt import WarpedVRT
import rasterio.coords
import rasterio.warp
import rasterio.merge
import rasterio.windows
import rasterio.mask
import rasterio.crs


infolder = r"\\ncr104\d$\NAER\S2\cloudmask_sept\final\*T3*20170910T104212*.tif"
outfile = r"C:\Users\juko\Downloads\temp\mosaic2.tif"
infiles = glob.glob(infolder)
infiles[-1]


reproject(infiles[-1], outfile, dst_crs={'init':'epsg:32632'}, resolution=20)




def reproject(infile, outfile, dst_crs, resolution=None):
    """Reproject a file to a new CRS
    Paremters
    ---------
    infile : str
        path to input file
    outfile : str
        path to output file
    dst_crs : dict or rasterio.crs.CRS
        destination CRS
    resolution : int, float, optional
        enforce resolution
    """
    with rasterio.open(infile) as src:
        transform, width, height = rasterio.warp.calculate_default_transform(
                src.crs, dst_crs, src.width, src.height,
                *src.bounds, resolution=resolution)
        profile = src.profile.copy()
        profile.update({
            'crs': dst_crs,
            'transform': transform,
            'width': width,
            'height': height})
        try:
            nodata = profile['nodata']
        except KeyError:
            profile['nodata'] = nodata = 0

        with rasterio.open(outfile, 'w', **profile) as dst:
            for b in range(1, src.count + 1):
                logger.info('Reprojecting band {} ...'.format(b))
                rasterio.warp.reproject(
                    source=rasterio.band(src, b),
                    destination=rasterio.band(dst, b),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_nodata=nodata,
                    resampling=rasterio.warp.Resampling.bilinear)
