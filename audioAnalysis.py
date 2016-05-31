from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt

def plotSpectru(y,Fs,s):
    n = len(y) # lungime semnal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range

    Y = fft(y)/n # fft computing and normalization
    Y = Y[range(n/2)]

    s.plot(frq,abs(Y),'b') # plotting the spectrum
    plt.xlabel('Czestotliwosc (Hz)')
    plt.ylabel('|Y(freq)|')

    #s.suptitle('Plik po odebraniu.');

def run():
    Fs = 44100;  # sampling rate

    rate1,data1=read('file.wav')
    y1=data1
    lungime1=len(y1)
    timp1=len(y1)/44100.
    t1=linspace(0,timp1,len(y1))
     
    fig = plt.figure()
    fig.clf()
    s1 = fig.add_subplot(221)
    s2 = fig.add_subplot(222)
    s3 = fig.add_subplot(223)
    s4 = fig.add_subplot(224)
    s1.plot(t1, y1, 'r-') # Returns a tuple of line objects, thus the comma
        
    fig.suptitle('Plik przed wyslaniem.          Plik po odebraniu.')
    plt.xlabel('Czas')
    plt.ylabel('Amplituda')



    plotSpectru(y1,Fs,s3)


    fig.show()
    
    rate2,data2=read('temp.wav')
    rate1,data1=read('file.wav')


    
    while len(data2) != len(data1):
        rate2,data2=read('temp.wav')
        y2=data2
        lungime2=len(y2)
        timp2=len(y2)/44100.
        t2=linspace(0,timp2,len(y2))
    
        s2.plot(t2, y2, 'r-')

        plotSpectru(y2,Fs,s4)
        fig.canvas.draw()
        
        #fig4.xlabel('Czas')
        #fig4.ylabel('Amplituda')
        #fig4.title('Plik po odebraniu.')


      
        
        

    



