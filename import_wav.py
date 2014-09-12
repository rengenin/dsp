import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

#You don't know y(t) has a frequency of 45Hz
#Trying to recover this frequency with FFT
wavfile = read('test.wav')
y = wavfile[1]#time domain function
sr = wavfile[0]#sampling rate from the wave file

#plot wave profile
plt.subplot(211)
plt.plot(y)

#FFT of y
ft = np.fft.fft(y)
mag = np.abs(ft)

#plot FFT
plt.subplot(212)
plt.plot(mag)

plt.show()
