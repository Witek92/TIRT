import pyaudio
import wave
import sys
import time

class WavePlay(pyaudio.PyAudio):

    def __init__(self):
        self.nameFile = ''
        self.data = ''
        
    def setData(self,data):
        self.data = data
        
    def run(self, ):
        CHUNK = 1024
        
        wf = wave.open('temp.wav', 'wb')
        wf.setparams((1,2,16000,0,'NONE','not compressed'))
        wf.writeframes(self.data)
                  
        p = pyaudio.PyAudio()
        
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
        
        stream.start_stream()
        
        i = 1
        while True:
            time.sleep(0.1)
            data = wf.readframes(CHUNK)
            if data == '':
                print 'No data in buffer'
                break
            stream.write(data)
            wf = wave.open(self.nameFile, 'rb')
            try:
                wf.setpos(i*CHUNK)
            except wave.Error:
                break;        
            i = i+1
            
        
        wf.close()  
        stream.stop_stream()
        stream.close()     
        p.terminate()
        