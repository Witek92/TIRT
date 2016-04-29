from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt


def plotSpectru(y,Fs):
    n = len(y) # lungime semnal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range

    Y = fft(y)/n # fft computing and normalization
    Y = Y[range(n/2)]


    plt.plot(frq,abs(Y),'r') # plotting the spectrum
    plt.xlabel('Czestotliwosc (Hz)')
    plt.ylabel('|Y(freq)|')

def run():
    Fs = 44100;  # sampling rate

    rate1,data1=read('file.wav')
    y1=data1
    lungime1=len(y1)
    timp1=len(y1)/44100.
    t1=linspace(0,timp1,len(y1))

    plt.subplot(2,2,1)
    plt.plot(t1,y1)
    plt.xlabel('Czas')
    plt.ylabel('Amplituda')
    plt.title('Plik przed wyslaniem.')

    plt.subplot(2,2,3)
    plotSpectru(y1,Fs)


    rate2,data2=read('file2.wav')
    #y=data[:,1]
    y2=data2
    lungime2=len(y2)
    timp2=len(y2)/44100.
    t2=linspace(0,timp2,len(y2))

    plt.subplot(2,2,2)


    plt.plot(t2,y2)
    plt.xlabel('Czas')
    plt.ylabel('Amplituda')
    plt.title('Plik po odebraniu.')
    plt.subplot(2,2,4)
    plotSpectru(y2,Fs)

    show()



