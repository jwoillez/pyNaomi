import argparse
from astropy.io import fits
from matplotlib import pyplot as plt


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display a Fits image')
    parser.add_argument('filename', type=str, help='Fits file name.')
    
    args=parser.parse_args()
    
    with fits.open(args.filename) as hdulist:
        image = hdulist[0].data

    fig, axarr = plt.subplots(1, 1)
    axarr.imshow(image)
    plt.show()
