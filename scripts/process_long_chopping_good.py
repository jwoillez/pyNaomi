import numpy as np
from matplotlib import pyplot as plt

from naomi.iris import irisErrVec
from naomi import dropbox

t0 = np.datetime64('2018-10-03T03:21:17')

timestamps = ['2018-10-03T03.22.48',
              '2018-10-03T03.53.30']

freq = 1.3  # [Hz]
period = int(1e4/freq)*1e-4  # [s]

fig, axarr = plt.subplots(2, 1, sharex=True, figsize=(10,4))
for i, timestamp in enumerate(timestamps):
    data = irisErrVec.load(dropbox + f'naomi-comm/2018-10-02/irisErrVec.{timestamp}.txt')
    axarr[0].plot(((data['t']-t0).astype(float)/1e6/period)%1.0, data['chop']+i/10, '.')
    axarr[1].plot(((data['t']-t0).astype(float)/1e6/period)%1.0, data['Q3flux'], '.')
axarr[1].plot([0.5,0.5],[0,data['Q3flux'].max()], 'k')
axarr[0].set_xlim(0.45,0.55)
plt.show()
