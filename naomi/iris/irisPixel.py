import numpy as np
import re


def load(filename):

    with open(filename) as f:
        firstline = f.readline()
    flux = np.loadtxt(filename, skiprows=2, dtype=float,
                      usecols=(2+3*i for i in range(30)))
    x = np.loadtxt(filename, skiprows=2, dtype=int,
                   usecols=(3+3*i for i in range(30)))
    y = np.loadtxt(filename, skiprows=2, dtype=int,
                   usecols=(4+3*i for i in range(30)))

    res = re.search('nx\: (\d+) +ny\: (\d+)', firstline)
    nx = int(res.group(1))
    ny = int(res.group(2))
    nz = len(flux)

    data = np.zeros((nz, nx, ny), dtype=int)

    for i in range(30):
        data[range(nz), x[:, i], y[:, i]] = flux[:, i]

    return data
