import numpy as np


def load(filename):
    dt_in = [('s', int), ('us', int),
             ('Q1errX', float), ('Q1errY', float),
             ('Q1flux', float), ('Q1bkg', float),
             ('Q2errX', float), ('Q2errY', float),
             ('Q2flux', float), ('Q2bkg', float),
             ('Q3errX', float), ('Q3errY', float),
             ('Q3flux', float), ('Q3bkg', float),
             ('Q4errX', float), ('Q4errY', float),
             ('Q4flux', float), ('Q4bkg', float),
             ('flag', bool), ('chop', bool)]
    dt_out = [('t', 'M8[us]'),
              ('Q1errX', float), ('Q1errY', float),
              ('Q1flux', float), ('Q1bkg', float),
              ('Q2errX', float), ('Q2errY', float),
              ('Q2flux', float), ('Q2bkg', float),
              ('Q3errX', float), ('Q3errY', float),
              ('Q3flux', float), ('Q3bkg', float),
              ('Q4errX', float), ('Q4errY', float),
              ('Q4flux', float), ('Q4bkg', float),
              ('flag', bool), ('chop', bool)]
    usecols = (0, 1,
               2, 3, 8, 9,
               10, 11, 16, 17,
               18, 19, 24, 25,
               26, 27, 32, 33,
               34, 35)
    data_in = np.loadtxt(filename,
                         dtype=dt_in,
                         usecols=usecols,
                         skiprows=3)
    data_out = np.empty(data_in.shape, dtype=dt_out)
    data_out['t'] = data_in['s']*1000000 + data_in['us']
    for d in dt_out[1:]:
        data_out[d[0]] = data_in[d[0]]
    return data_out
