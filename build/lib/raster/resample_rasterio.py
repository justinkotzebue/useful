"""
Create band stacks from multiple single-band files (bandfiles)
or multispectal files.
"""
import logging

import rasterio
import rasterio.warp

logger = logging.getLogger(__name__)


def stack_resample_bandfiles(bandfiles, outfile,
        template_idx=0, creation_options={}):
    """Stack bands from provided files
    Parameters
    ----------
    bandfiles : iterable of file names or urls
        band files in correct order
    outfile : str
        path to output file
    template_idx : int
        index of template file in bandfiles
    creation_options : dict
        update dst profile
    """
    with rasterio.open(bandfiles[template_idx]) as tmpl:
        profile = tmpl.profile.copy()

    profile.update(creation_options)

    profile['count'] = len(bandfiles)

    logger.info('Stacking %d bands ...', len(bandfiles))
    with rasterio.open(outfile, 'w', **profile) as dst:
        bdst = 0
        for bandfile in bandfiles:
            bdst += 1
            with rasterio.open(bandfile) as src:
                if src.crs != profile['crs']:
                    raise ValueError(
                            'Source and destination CRS must be identical. '
                            'Got {} and {}, respectively.'
                            ''.format(src.crs, profile['crs']))

                if src.transform != profile['transform']:
                    logger.info('Resampling band %d ...', bdst)
                    rasterio.warp.reproject(
                        source=rasterio.band(src, 1),
                        destination=rasterio.band(dst, bdst),
                        resampling=rasterio.warp.Resampling.bilinear)
                else:
                    dst.write_band(bdst, src.read(1))
logger.info('Done.')
