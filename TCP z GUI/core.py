import sys
import thread
from PyQt4 import QtCore, QtGui
#from audioplay import WavePlay
from gui1 import Ui_Form
from tcpsender import TcpSend
from tcprec import TcpRec
import audioAnalysis
import dolnoPrzepustowy

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.sendTool,QtCore.SIGNAL("clicked()"), self.sending)
        QtCore.QObject.connect(self.ui.recTool, QtCore.SIGNAL("clicked()"), self.receiving)
        QtCore.QObject.connect(self.ui.analyse, QtCore.SIGNAL("clicked()"), audioAnalysis.run)
        QtCore.QObject.connect(self.ui.lowPass, QtCore.SIGNAL("clicked()"), dolnoPrzepustowy.run)


                         
    def sending(self):
        sender = TcpSend()
        sender.setName(self.ui.FilePath.text())
        sender.setHost(self.ui.IPsendTool.text())
        sender.setPort(int(self.ui.PortsendTool.text()))
        thread.start_new_thread(sender.send, ())
        
    def receiving(self):
        recor = TcpRec()
        #recor.setName(self.ui.FilePath.text())
        recor.setHost(self.ui.IPrecTool.text())
        recor.setPort(int(self.ui.PortrecTool.text()))
        thread.start_new_thread(recor.receive, ())
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()     
    sys.exit(app.exec_())