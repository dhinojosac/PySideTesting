import sys, time
from PySide.QtCore import *
from PySide.QtGui import *

# Our main window class [PySide.QtGui.QWidget]
class SampleWindow(QWidget):
	# Constructor function
	def __init__(self):
		super(SampleWindow,self).__init__()
		self.initGUI()

	def initGUI(self):
		self.setWindowTitle("RN2903")
		self.setGeometry(300, 300, 200, 150)
		self.setMinimumHeight(100)
		self.setMinimumWidth(250)
		self.setMaximumHeight(200)
		self.setMaximumWidth(800)
		#icon --
		appIcon = QIcon('uart.png')
		self.setWindowIcon(appIcon)
		#--
		self.show()
		print("Sample Window show in the GUI\n")

if __name__ == '__main__':
	# Exception Handling
	try:
		myApp = QApplication(sys.argv)
		myWindow = SampleWindow()
		QCoreApplication.processEvents()
		time.sleep(3)
		myWindow.resize(300, 300)
		myWindow.setWindowTitle("RN2903 Tester")
		myWindow.repaint()
		myApp.exec_()
		sys.exit(0)
	except NameError:
		print("Name Error:", sys.exc_info()[1])
	except SystemExit:
		print("Closing Window...")
	except Exception:
		print (sys.exc_info()[1])
