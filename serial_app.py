# Import required modules
import sys, serial
from PySide.QtGui import *

def serial_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def testSerial(mType, mSerial, mBaudrate):
    ser = serial.Serial(mSerial, mBaudrate)
    ser.write("sys get ver\r\n")
    result= ser.readline()
    ser.close()
    return result


class MainWindow(QMainWindow):
    """ Our Main Window class
    """
    def __init__(self):
        """ Constructor Function
        """
        super(MainWindow,self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("ManglarNode Tester")
        self.setWindowIcon(QIcon('uart.png'))
        self.setGeometry(300, 250, 400, 250)
        self.SetupComponents()
        self.show()

    def SetupComponents(self):
        """ Function to setup status bar, central widget, menu bar
        """
        #statusbar
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 10000)
        #actions
        self.CreateActions()
        #menubar
        self.CreateMenus()
        #add action to menu items
        self.addActionToMenusItems()
        #add center components
        self.addSelectionPortSerialLora()
        self.addSelectionPortSerialGps()
        self.addTestComponents()
       
    
    def addSelectionPortSerialLora(self):
        #add serial port label
        self.ser_port_lbl_lora = QLabel('Serial Port:', self)
        self.ser_port_lbl_lora.move(10, 40) # offset the first control 5px
        #add combobox
        self.ports_cb_lora = QComboBox(self)
        self.ports_cb_lora.addItems(serial_ports())
        self.ports_cb_lora.setMinimumWidth(30)
        self.ports_cb_lora.move(70, 40)
    
    def addSelectionPortSerialGps(self):
        #add serial port label
        self.ser_port_lbl_gps = QLabel('Serial Port:', self)
        self.ser_port_lbl_gps.move(10, 150) # offset the first control 5px
        #add combobox
        self.ports_cb_gps = QComboBox(self)
        self.ports_cb_gps.addItems(serial_ports())
        self.ports_cb_gps.setMinimumWidth(20)
        self.ports_cb_gps.move(70, 150)
        
    
    def addTestComponents(self):
        #add rn2903 label 
        self.lora_lbl = QLabel('RN2903', self)
        self.lora_lbl.move(10, 80) # offset the first control 5px
        #add gps label
        self.gps_lbl = QLabel('GPS', self)
        self.gps_lbl.move(10, 190) # offset the first control 5px
        #add result test rn2903 label 
        self.result_lora_lbl = QLabel('N.A.', self)
        self.result_lora_lbl.move(240, 80) # offset the first control 5px
        #add result test gps label
        self.result_gps_lbl = QLabel('N.A.', self)
        self.result_gps_lbl.move(240, 190) # offset the first control 5px
        #add button to test lora
        self.lora_btn = QPushButton('TEST', self)
        self.lora_btn.clicked.connect(self.clickLoraTest)
        self.lora_btn.move(70, 80) # offset the first control 5px
        #add button to test gps
        self.gps_btn = QPushButton('TEST', self)
        self.gps_btn.clicked.connect(self.clickGpsTest)
        self.gps_btn.move(70, 190) # offset the first control 5px
        #add icons results
        self.myLabel1 = QLabel('', self)
        self.myLabel1.move(300,80)
        
        
        
    
    def addActionToMenusItems(self):
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.copyAction)
        self.fileMenu.addSeparator()
        self.editMenu.addAction(self.pasteAction)
        self.helpMenu.addAction(self.aboutAction)


    def clickLoraTest(self):
        text = str(self.ports_cb_lora.currentText())
        res=testSerial("LORA",text,57600)
        if "RN2903" in res:
            self.myIcon1 = QIcon("passed.png")
            self.pixmap1 = self.myIcon1.pixmap(40, 40, QIcon.Active, QIcon.On)
            self.myLabel1.setPixmap(self.pixmap1)
            self.myLabel1.show()
            self.result_lora_lbl.setText("PASSED")
        else:
            self.myIcon1 = QIcon("failed.png")
            self.pixmap1 = self.myIcon1.pixmap(40, 40, QIcon.Active, QIcon.On)
            self.myLabel1.setPixmap(self.pixmap1)
            self.myLabel1.show()
            self.result_lora_lbl.setText("FAILED")
    
    def clickGpsTest(self):
        text = str(self.ports_cb_gps.currentText())
        testSerial("GPS",text,9600)
        self.result_gps_lbl.setText(text)

    # Slots called when the menu actions are triggered
    def newFile(self):
        pass

    def exitFile(self):
        self.close()

    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor",
        "This example demonstrates the use "
        "of Menu Bar")

    def CreateActions(self):
        """ Function to create actions for menus
        """
        self.newAction = QAction( QIcon('new.png'), '&New',
            self, shortcut=QKeySequence.New,
            statusTip="Create a New File",triggered=self.newFile)
        self.exitAction = QAction( QIcon('exit.png'), 'E&xit',
            self, shortcut="Ctrl+Q",
            statusTip="Exit the Application",
            triggered=self.exitFile)
        self.copyAction = QAction( QIcon('copy.png'), 'C&opy',
            self, shortcut="Ctrl+C",
            statusTip="Copy",
            triggered=self.showMaximized)
        self.pasteAction = QAction( QIcon('paste.png'), '&Paste',
            self, shortcut="Ctrl+V",
            statusTip="Paste",
            triggered=self.showMinimized)
        self.aboutAction = QAction( QIcon('about.png'), 'A&bout',
            self, statusTip="Displays info about text editor",
            triggered=self.aboutHelp)
        
    # Actualmenubar item creation
    def CreateMenus(self):
        """ Function to create actual menu bar
        """
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.helpMenu = self.menuBar().addMenu("&Help")

if __name__ == '__main__':
    # Exception Handling
    try:
        #QApplication.setStyle('plastique')
        myApp = QApplication(sys.argv)
        myApp.setStyle(QStyleFactory.create("plastique"))
        mainWindow = MainWindow()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])