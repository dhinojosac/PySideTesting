# Import required modules
import sys, time
from PySide.QtGui import *
from PySide.QtCore import *

# Our main window class
class SampleWindow(QWidget):
    # Constructor function
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("UsAdmin")
        self.setGeometry(300, 300, 800, 500)
        # Function to set Icon
        appIcon = QIcon('uart.png')
        self.setWindowIcon(appIcon)
        self.setIconModes()
        self.setButton()
        self.center()
        self.setAboutButton()
        self.show()

    def setIconModes(self):
        myIcon3 = QIcon('cell.png')
        myLabel3 = QLabel('sample', self)
        pixmap3 = myIcon3.pixmap(70, 70, QIcon.Selected, QIcon.On)
        QToolTip.setFont(QFont("Decorative", 8 , QFont.Bold))
        #set tooltip on label
        myLabel3.setToolTip('Cell')
        myLabel3.setPixmap(pixmap3)
        myLabel3.move(10, 10)
        myLabel3.show()

    def setButton(self):
        """ Function to add a quit button """
        myButton = QPushButton('Quit', self)
        myButton.move(50, 100)
        myButton.setToolTip('Salir del programa')
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

    def setAboutButton(self):
        """ Function to set About Button """
        self.aboutButton = QPushButton("About", self)
        self.aboutButton.move(100, 100)
        self.aboutButton.clicked.connect(self.showAbout)

    def showAbout(self):
        """ Function to show About Box """
        QMessageBox.about(self.aboutButton, "About PySide", 
        '''UsAdmin es un programa para la administarcion de pacientes y usarios.\n\n
         dhinojosac@gmail.com''')
    
    

    
    
 
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





