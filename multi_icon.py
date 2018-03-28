# Import required modules
import sys, time
from PySide.QtGui import QApplication, QWidget, QIcon, QLabel

# Our main window class
class SampleWindow(QWidget):
    # Constructor function
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.initGUI()

    def setIconModes(self):
        myIcon1 = QIcon('cell.png')
        myLabel1 = QLabel('sample', self)
        pixmap1 = myIcon1.pixmap(50, 50, QIcon.Active, QIcon.On)
        myLabel1.setPixmap(pixmap1)
        myLabel1.show()

        myIcon2 = QIcon('cell.png')
        myLabel2 = QLabel('sample', self)
        pixmap2 = myIcon2.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
        myLabel2.setPixmap(pixmap2)
        myLabel2.move(50, 0)
        myLabel2.show()

        myIcon3 = QIcon('cell.png')
        myLabel3 = QLabel('sample', self)
        pixmap3 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
        myLabel3.setPixmap(pixmap3)
        myLabel3.move(100, 0)
        myLabel3.show()

        myIcon4 = QIcon('cell.png')
        myLabel4 = QLabel('sample', self)
        pixmap4 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
        myLabel4.setPixmap(pixmap3)
        myLabel4.move(150, 0)
        myLabel4.show()

    def initGUI(self):
        self.setWindowTitle("Icon Sample")
        self.setGeometry(300, 300, 200, 150)
        # Function to set Icon
        appIcon = QIcon('uart.png')
        self.setWindowIcon(appIcon)
        self.setIconModes()
        self.show()
    
    
 
if __name__ == '__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])





