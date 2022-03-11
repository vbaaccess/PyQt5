from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_settings(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Simple app to show setting FBD-SUR.NET ( {name})') # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
