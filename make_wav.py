import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

'''Creating a wave file to play with later'''

t = np.linspace(0, 1, 1001)
#signal is a pure tone of 45 Hz
y = np.sin(2*np.pi*45*t)
#scaled up so it actual is audible
scaled = np.int16(y/np.max(np.abs(y))*32767)

write('test.wav', 44100, scaled)


plt.plot(y)
plt.show()
