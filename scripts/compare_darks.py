import argparse
from astrop.io import fits
import numpy as np


if __name__ == '__main__':

    # Parse input arguments
    parser = argparse.ArgumentParser(description="Compare two darks files.")
    parser.add_argument('dark1', type=str)
    parser.add_argument('dark2', type=str)
    args = parser.parse_args()

    # Read both darks
    with fits.open(args.dark1) as hdulist:
        dark1 = hdulist[0].data
    with fits.open(args.dark2) as hdulist:
        dark2 = hdulist[1].data

    # Compare both darks
    mean_diff = np.mean(dark1-dark2)
    var_diff = np.var(dark1-dark2)

    # Output results
    print('mean_diff: {0:.3f}'.format(mean_diff))
    print('var_diff: {0:.3f}'.format(var_diff))
