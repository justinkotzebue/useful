import numpy as np
import rasterio
import spectral
#from spectral import *




def read_mask_transpose(instack):
    with rasterio.open(instack) as intif:
        stack = intif.read()
        land = stack[7, :, :] > 200
        np.count_nonzero(land)
        out_meta = intif.meta.copy()
        (stack[:,land]) = 0
        t_stack = np.transpose(stack, (1,2,0))
        return t_stack, out_meta


def denoise(data, num=None, snr=None):
    """
    Denoises nd array with the format n x p x b

    Parameters:
    -----------
    data : nd array
        3-d numpy array with b = band
    num : int
        number of bands used
    snr : int
        threshold
    Returns
    -------
    denoised array with same shape as data
    """
    signal = spectral.calc_stats(data)
    noise = spectral.noise_from_diffs(data)
    mnfr = spectral.mnf(signal, noise)
    if num:
        denoised, trans = mnfr.denoise(data, num=num)
        print(50*'_')
        print(trans.shape)
    elif snr:
        denoised = mnfr.denoise(data, snr=snr)
        print("--------------")
        print(mnfr.num_with_snr(snr=snr))
    else:
        raise ValueError('"snr" or "num" must be given!')
    return denoised, trans


def retranspose_write(data_denoised, outstack, out_meta):
    t_denoised = np.transpose(data_denoised, (2,0,1))
    out_meta['count']= t_denoised.shape[0]
    for i in range(0,out_meta['count']):
        with rasterio.open(outstack, "w", **out_meta) as dest:
            dest.write(t_denoised.astype(rasterio.uint16, i+1))


instack = r"/home/jb/Downloads/mosaic/mosaic.tif"
outstack = r"/home/jb/Downloads/mosaic/mosaic_out_test.tif"
trans_dir = r"/home/jb/Downloads/mosaic/mosaic_out_trans.tif"

t_stack, out_meta = read_mask_transpose(instack)
denoised, trans = denoise(t_stack, num=4)
retranspose_write(trans, trans_dir, out_meta)
