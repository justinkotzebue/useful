import os
import glob
import rasterio
import gdal_utils.gdal_binaries as gbin


# Read metadata of first file
def stack(filelist, outfile):
    with rasterio.open(filelist[0]) as src0:
        meta = src0.meta

    # Update meta to reflect the number of layers
    meta.update(count = len(filelist))

    # Read each layer and write it to stack
    with rasterio.open(outfile, 'w', **meta) as dst:
        for id, layer in enumerate(filelist):
            with rasterio.open(layer) as src1:
                dst.write_band(id + 1, src1.read(1))



res = str(30)
p = r"\\ncr104\d$\NAER\training_data_optical\l7"
folders = glob.glob(os.path.join(p, '*.tar'))
for folder in folders:
    vrtfile = os.path.join(folder, os.path.basename(folder) + '.vrt')
    bandfiles = glob.glob(os.path.join(folder, '*B[1-4]*'))
    print(bandfiles)
    #print(folder)
    vrt = gbin.buildvrt(infiles=bandfiles, outfile=vrtfile, separate=True,
                  resolution = 'user', extra=['-tr',res, res])


def vrt_to_tif(path,output_path,resolution, bandpatterns=[]):
    name = os.path.splitext(os.path.basename(path))[0]
    outnametranslate = os.path.join(output_path,name + ".tif")
    vrtfile = vrt(path,output_path,resolution,name,bandpatterns)
    gbin.translate(infile=vrtfile,outfile=outnametranslate, of= 'GTiff')
