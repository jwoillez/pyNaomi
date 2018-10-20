import argparse
from astropy.io import fits
import numpy as np
import os
import ccs


nZ = 14
nT = 500
freq = 30.0  # [Hz]
amplitude = 0.4  # [umRMS]

def disturbance(frequency, amplitude, mode):
    filename = '{0}/SYSTEM/SPARTA/RTCDATA/piston_modulation_Z{1}.fits'.format(os.environ["INS_ROOT"], mode)
    mod = np.zeros((500, 14), dtype=float)
    mod[:, mode-2] = amplitude*np.sin(2*np.pi*frequency*np.arange(500)/500)
    hdulist = fits.HDUList([fits.PrimaryHDU(mod.astype(np.float32))])
    hdulist.writeto(filename, overwrite=True)
    return filename


def msgSend(env, process, command, param):
    result = subprocess.run(['msgSend', env, process, command, param], stdout=subprocess.PIPE)


if __name__ == '__main__':
     parser = argparse.ArgumentParser(description='Inject a modal disturbance')
     parser.add_argument('frequency', type=float, help='Frequency [Hz]')
     parser.add_argument('amplitude', type=float, help='Amplitude [umRMS]')
     parser.add_argument('mode', type=int, help='Mode index Z=2..16')

     args=parser.parse_args()

     ccs.CcsInit('generate_model_disturbance.py')
     
     # Generate disturbance
     filename = disturbance(args.frequency, args.amplitude, args.mode)

     # Configure SPARTA
     ccs.SendCommand('wat{0}nao'.format(os.environ['TCSID']), 'spaccsServer', 'SETUP', 'ModalCtrDisturb.FILENAME {0}'.format(filename))
     ccs.SendCommand('wat{0}nao'.format(os.environ['TCSID']), 'spaccsServer', 'SETUP', 'ModalCtrDisturb.CYCLES 30')
     ccs.SendCommand('wat{0}nao'.format(os.environ['TCSID']), 'spaccsServer', 'EXEC', 'ModalCtrDisturb.run')


