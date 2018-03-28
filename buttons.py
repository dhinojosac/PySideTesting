# Import required modules
import sys, time
from PySide.QtGui import *

# Our main window class
class SampleWindow(QWidget):
    # Constructor function
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Icon Sample")
        self.setGeometry(300, 300, 200, 150)
        # Function to set tooltip
        QToolTip.setFont(QFont("Decorative", 8 , QFont.Bold))
        self.setToolTip('Our Main Windows')
        # Function to set Icon
        appIcon = QIcon('uart.png')
        self.setWindowIcon(appIcon)
        self.setIconModes()
        self.setButton()
        self.center()
        self.show()

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
        QToolTip.setFont(QFont("Decorative", 8 , QFont.Bold))
        #set tooltip on label
        myLabel3.setToolTip('Cell')
        myLabel3.setPixmap(pixmap3)
        myLabel3.move(100, 0)
        myLabel3.show()

    def setButton(self):
        """ Function to add a quit button """
        myButton = QPushButton('Quit', self)
        myButton.move(50, 100)
        myButton.clicked.connect(self.quitApp)
    
    #Function to Quit App that uses MsgApp
    def quitApp(self):
        response = self.msgApp("Confirmation","This will quit the application. Do you want to Continue?")
        if response == "Y":
            myApp.quit()
        else:
            pass

    def msgApp(self,title,msg):
        userInfo = QMessageBox.question(self,title,msg, QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            return "Y"
        if userInfo == QMessageBox.No:
            return "N"

    def center(self):
        """ Function to center the application """
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
    
    

    
    
 
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





