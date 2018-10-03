from astropy.io import fits


def load(path, filename):
    with fits.open(f'{path}/IMG_{filename}_DIT.fits') as hdulist:
        img = hdulist[0].data
    with fits.open(f'{path}/BCK_{filename}_DIT.fits') as hdulist:
        bck = hdulist[0].data
    return img - bck.mean(axis=0)
