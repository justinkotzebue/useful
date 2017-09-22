from satmeta.s2 import meta as s2meta
import os
import glob
import re

pathSAFE = r"D:\ExampleData\Sentinel\Sentinel2\S2A_OPER_PRD_MSIL1C_PDMC_20160724T182306_R108_V20160724T103229_20160724T103229.SAFE"
path = r"D:\ExampleData\Sentinel\Sentinel2\S2B_MSIL1C_20170727T104019_N0205_R008_T32VMJ_20170727T104022.SAFE"
m = s2meta.find_parse_metadata(path)
'tile_name' in m

g = s2meta.find_parse_granule_metadata(path)

gg['tile_id']
b = s2meta.converters

t = s2meta.find_tile_name(path)
help(s2meta)

p = s2meta.sensor_ID_from_spacecraft_name(path)
def return_granule_list(pathSAFE):
    granule = os.path.join(pathSAFE, "GRANULE")
    granule_pattern = os.path.join(granule, '*')
    granule_list = glob.glob(granule_pattern)
    if not granule_list:
        raise ValueError('No granule[s] found in {}'.format(granule))
    return granule_list

def final_product_exists(pathSAFE, pixel_size, path_output):
    granules = return_granule_list(pathSAFE)
    for i in granules:
        tile_id = s2meta.find_tile_name(i)
        date = re.search(8*'\d' + '\D' + 6*'\d', os.path.basename(i)).group(0)
        pattern = '*' + tile_id + '*' + date + '*' + pixel_size + '*' + '.tif'
        search = os.path.join(path_output, pattern)
        exists = glob.glob(search)

        if exists:
            return True
        if not exists:
            return False




final_product_exists(path)
