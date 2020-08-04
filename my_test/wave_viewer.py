# thanks to https://www.youtube.com/watch?v=AShHJdSIxkY

import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure


# Settings for the audio plot:
# how much audio samples processed per frame
CHUNK = 1024 * 4
# sets the samples as 16bit integers
FORMAT = pyaudio.paInt16
# audio channels and hz
CHANNELS = 1
RATE = 16000

# Set an instance of the PyAudio class
p = pyaudio.PyAudio()

# stream will be an instance of 'open' using the settings given above
stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

# data will be a large amount of byte-formatted data (x00\xff\etc etc)
#       data = stream.read(CHUNK)

# this will convert the byte-data into integer data
# CHUNK will be half of the datastring size (because data is now returning bytes(8 bits)), so we need to double it
# the 'h' formats the characters as small integers 
# the structure needs to be restructured so it comes from the center out (like a spectrogram) instead of bottom-up
#       data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2]+127
# int data can be plotted with matplotlib

# to speed up and optimize matplotlib's ability to construct the plot, we will use the line method from 
# https://bastibe.de/2013-05-30-speeding-up-matplotlib.html
# we create a single line and update that instead of creating and flushing the entire graph everytime
# everything will be wrapped in a while loop
plt.ion()
fig, ax = plt.subplots()

# this provides an x-dimension for plotting
x = np.arange(0, 2 * CHUNK, 2)
data = stream.read(CHUNK)
data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2]+127
# This will start a line that will be rewritten almost immediately
line, = ax.plot(x, data_int)
ax.set_ylim([-2**15,(2**15)-1])
# ax.set_xlim(0, CHUNK)

# This will pick up audio to render the plot while the program runs
while True:
    data = struct.unpack(str(CHUNK) + 'h', stream.read(CHUNK))
    line.set_ydata(data)
    print(data)
    fig.canvas.draw()
    fig.canvas.flush_events()