import argparse
from astrop.io import fits
import numpy as np


if __name__ == '__main__':

    # Parse input arguments
    parser = argparse.ArgumentParser(description="Compare two interaction matrix files.")
    parser.add_argument('im1', type=str)
    parser.add_argument('im2', type=str)
    args = parser.parse_args()

    # Read both interactions matrices
    with fits.open(args.im1) as hdulist:
        im1 = hdulist[0].data
    with fits.open(args.im2) as hdulist:
        im2 = hdulist[1].data

    # Compare the two IMs
    
