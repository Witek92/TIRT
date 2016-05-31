import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import math
import contextlib
from Tkinter import *
from scipy.signal import butter, lfilter
import scipy


def highPassRun(self):

    def butter_bandpass(lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a


    def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
        b, a = butter_bandpass(lowcut, highcut, fs, order=order)
        y = lfilter(b, a, data)
        return y


    # from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean
    def running_mean(x, windowSize):
      cumsum = np.cumsum(np.insert(x, 0, 0))
      return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize

    # from http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174
    def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):

        if sample_width == 1:
            dtype = np.uint8 # unsigned char
        elif sample_width == 2:
            dtype = np.int16 # signed 2-byte short
        else:
            raise ValueError("Only supports 8 and 16 bit audio formats.")

        channels = np.fromstring(raw_bytes, dtype=dtype)

        if interleaved:
            # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data
            channels.shape = (n_frames, n_channels)
            channels = channels.T
        else:
            # channels are not interleaved. All samples from channel M occur before all samples from channel M-1
            channels.shape = (n_channels, n_frames)

        return channels

    fname = 'temp.wav'

    cutOffFrequencyHigh=float(self.ui.cutFreqHigh.text())
    cutOffFrequencyLow=float(self.ui.cutFreq.text())


    filePos = 0

    self.ui.Prompt.setText("Filtr gornoprzepustowy dziala")

    tempData = ''
    while True:
        if self.filterRunningAllowed:
            if self.recor.flagR:
              if self.data != tempData:
                  try:
                      spf = wave.open(fname,'rb')
                  except EOFError:
                      break

                  sampleRate = spf.getframerate()
                  ampWidth = spf.getsampwidth()
                  nChannels = spf.getnchannels()
                  nFrames = 512

                  spf.setpos(filePos)
                  # Extract Raw Audio from multi-channel Wav File
                  signal = spf.readframes(nFrames*nChannels)
                  spf.close()
                  filePos += nFrames
                  channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)

                  y = butter_bandpass_filter(channels[0], cutOffFrequencyLow, cutOffFrequencyHigh, sampleRate, order=6)

                  #from http://dsp.stackexchange.com/questions/9966/what-is-the-cut-off-frequency-of-a-moving-average-filter
                  freqRatio = (cutOffFrequencyHigh/sampleRate)
                  N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)

                  # Use moving average (only on first channel)
                  filtered = running_mean(y, N).astype(channels.dtype)


                  self.filteredData = filtered.tobytes('C')
                  tempData = self.data

            else:
              print "Filtr gornoprzepustowy wykonany!"
              self.filteredData = ''
              break
        else:
            break






