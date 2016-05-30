#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import math
import contextlib
from Tkinter import *
from PyQt4 import QtCore, QtGui
from guiEQ1 import Eq_Form

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def eqRun(self):
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


    filePos = 0

    self.ui.Prompt.setText(_translate("MainWindow", "Filtr dolnoprzepustowy włączony", None))

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

                  co=int(Eq_Form.sliderAmp.text())

                  channels[0]*=co


                  filtered=channels[0]
                  self.filteredData = filtered.tobytes('C')
                  tempData = self.data

            else:
              print "Filtr dolnoprzepustowy wykonany!"
              self.filteredData = ''
              break
        else:
            break

