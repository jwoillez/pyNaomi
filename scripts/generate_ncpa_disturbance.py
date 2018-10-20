from astropy.io import fits
from matplotlib import pyplot as plt
from scipy import linalg as la
import numpy as np


#%% Simulation parameters

f = 500  # [Hz]
period = 4000
margin = 500
f_fast = 25  # [Hz]
amplitude = 0.15  # [um]

#%% Load interaction matrix (S2M matrix)

with fits.open("./data/RTC.S2M.fits") as hdulist:
    S2M = hdulist[0].data

#%% Create fundamental modulation

modulation = amplitude*np.sin(2.0*np.pi*np.arange(period)/(period/2)) + \
             amplitude*np.sin(2.0*np.pi*np.arange(period)/f*f_fast)

#%% Display modulation

fig, axarr = plt.subplots(1, 1, figsize=(14, 4))
axarr.plot(modulation)
plt.show()

#%% Populate Zernikes

Z = np.zeros(((period+margin)*12, 14))
for iZ in range(2, 14):
    Z[(iZ-2)*(period+margin):(iZ-2)*(period+margin)+period, iZ] = modulation

#%%

fig, axarr = plt.subplots(1, 1)
axarr.imshow(Z, aspect='auto')
plt.show()

#%% Convert to slopes

S = (la.pinv(S2M) @ Z.T).T

print(S.max())

#%%

hdulist = fits.HDUList([fits.PrimaryHDU(S.astype(np.float32))])
hdulist.writeto('./data/NcpaModulation.fits', overwrite=True)

#%%
