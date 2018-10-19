from astropy.io import fits
import numpy as np


nZ = 14
nT = 500
freq = 30.0  # [Hz]
amplitude = 0.2  # [umRMS]

for iZ in range(nZ):
    disturb = np.zeros((nT, 14))
    disturb[:, iZ] = amplitude*np.sin(2*np.pi*freq*np.arange(nT)/nT)
    hdulist = fits.HDUList([fits.PrimaryHDU(disturb.astype(np.float32))])
    hdulist.writeto(f'./data/piston_modulation_Z{iZ+2}.fits', overwrite=True)
