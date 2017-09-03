import numpy as np
import rasterio
import spectral
#from spectral import *
from spectral.algorithms import GaussianStats as stats




def read_mask_transpose(instack):
    with rasterio.open(instack) as intif:
        stack = intif.read()
        land = stack[7, :, :] > 500
        np.count_nonzero(land)
        out_meta = intif.meta.copy()
        (stack[:,land]) = 0
        t_stack = np.transpose(stack, (1,2,0))
        return t_stack, out_meta


def denoise(data, num=None, snr=None):
    """
    Denoises nd array with the format n x p x b
    """
    signal = spectral.calc_stats(data)
    noise = spectral.noise_from_diffs(data)
    mnfr = spectral.mnf(signal, noise)
    if num:
        denoised = mnfr.denoise(data, num=num)
    elif snr:
        denoised = mnfr.denoise(data, snr=snr)
    else:
        raise ValueError('"snr" or "num" must be given!')
    return denoised


def retranspose_write(data_denoised, outstack, out_meta):
    t_denoised = np.transpose(data_denoised, (2,0,1))
    out_meta['count']= t_denoised.shape[0]
    for i in range(0,out_meta['count']):
        with rasterio.open(outstack, "w", **out_meta) as dest:
            dest.write(t_denoised.astype(rasterio.uint16, i+1))


instack = r"/media/jb/INTENSO/GIS/Sentinel_data/resampled_S2A_MSIL1C_20161224T104442_N0204_R008_T32UPF_20161224T104438.SAFE/stack.tif"
outstack = r"/home/jb/Downloads/stack_denoisedsnr300.tif"
t_stack, out_meta = read_mask_transpose(instack)
denoised = denoise(t_stack)
retranspose_write(denoised, outstack, out_meta)
