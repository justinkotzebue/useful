import numpy as np
import rasterio
import spectral
#from spectral import *



#instack = r"/media/jb/INTENSO/GIS/Sentinel_data/resampled_S2A_MSIL1C_20161224T104442_N0204_R008_T32UPF_20161224T104438.SAFE/stack.tif"
instack = r"/home/jb/Downloads/stack_masked.tif"
outstack = r"/home/jb/Downloads/stack_denoised5.tif"

with rasterio.open(instack) as intif:
    stack = intif.read()
    land = stack[7, :, :] > 500
    np.count_nonzero(land)
    out_meta = intif.meta.copy()
    (stack[:,land]) = 0
    t_stack = np.transpose(stack, (1,2,0))
help(spectral.calc_stats)
ss = stack.shape[0]
print(t_stack.shape)
# help(spectral.calc_stats)
#view =imshow(t_stack,(8,3,2))
signal = spectral.calc_stats(t_stack)
noise = spectral.noise_from_diffs(t_stack)
mnfr = spectral.mnf(signal, noise)
t_denoised = mnfr.denoise(t_stack, num=5)
t_reduced = mnfr.reduce(t_stack, num=5)
t_reduced.shape
t_denoised.shape
tt_denoised = np.transpose(t_denoised, (2,0,1))
tt_reduced = np.transpose(t_reduced, (2, 0, 1))
tt_stack = np.transpose(t_stack, (2, 0, 1))
tt_reduced.shape
out_meta['count']=13
tt_denoised.shape
tt_denoised.shape
np.max(tt_denoised[2:,])
np.min(tt_denoised[1:,])
view =spectral.imshow(t_denoised,(1,3,2))
for i in range(0,out_meta['count']):
    with rasterio.open(outstack, "w", **out_meta) as dest:
        dest.write(tt_denoised.astype(rasterio.uint16, i+1))
