import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse 
from scipy import fftpack

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()

print("drawing plot for", args.filename)

samplerate, data = sio.wavfile.read(args.filename) 

fftsize = len(data) 
data_fft = fftpack.fft(data, fftsize)

Ts = 1/samplerate 
############################################
# WRITE DOWN YOUR FFT PLOT CODE HERE 
# X axis is Frequency, Y axis is Power
freq = np.fft.fftfreq(fftsize,Ts)
power = np.abs(data_fft)

plt.figure(figsize = (10,6))
plt.plot(freq[:fftsize//2], power[:fftsize//2])
plt.title('FFT Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.grid(True)
###########################################

plt.show()
