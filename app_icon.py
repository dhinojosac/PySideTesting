# Import required modules
import sys, time
from PySide.QtGui import QApplication, QWidget, QIcon

# Our main window class
class SampleWindow(QWidget):
	# Constructor function
	def __init__(self):
		super(SampleWindow, self).__init__()
		self.initGUI()

	def initGUI(self):
		self.setWindowTitle("Icon Sample")
		self.setGeometry(300, 300, 200, 150)
		# Function to set Icon
		appIcon = QIcon('uart.png')
		self.setWindowIcon(appIcon)
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
