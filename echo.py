import numpy as np
import wave
import math
from scipy.io.wavfile import *



def echoR(self):


    def time_delay(x, r):
        y=np.zeros(len(x)+r)
        y[r:len(y)-1]=x[0:len(x)-1]
        return y

    def nFunc(n1,n2):
        n=[]
        a=min(n1)
        b=min(n2)
        c=max(n1)
        d=max(n2)
        e=min(a,b)
        f=max(c,d)
        for i in range(e,f):
            n.append(i)
        return n

    def sigadd(x1,x2,n1,n2):
        n=nFunc(n1,n2)
        y1=np.zeros(len(n))
        y2=y1
        y1[np.where((n>=min(n1))&(n<=max(n1)) ==1)]=x1
        y2[np.where((n>=min(n2))&(n<=max(n2)) ==1)]=x2
        y=y1+y2
        return y

    def running_mean(x, windowSize):
      cumsum = np.cumsum(np.insert(x, 0, 0))
      return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize



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

    self.ui.Prompt.setText("Dodawanie echa dziala")



    tempData = ''
    while True:
        if self.filterRunningAllowed:
            if self.recor.flagR:
              if self.data != tempData:

                  try:
                      spf = wave.open(fname,'rb')
                  except EOFError:
                      break

                  n,tab=read(fname)

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

                  n1=[]
                  n2=[]
                  for i in range(0,len(channels[0])-1):
                      n1.append(i)
                  y=time_delay(channels[0],50000)

                  for i in range(0,len(y)-1):
                      n2.append(i)
                  filtered=sigadd(channels[0],y,n1,n2)


                  self.filteredData = filtered.tobytes('C')
                  tempData = self.data

            else:
              print "Echo wykonane!"
              self.filteredData = ''
              break
        else:
            break