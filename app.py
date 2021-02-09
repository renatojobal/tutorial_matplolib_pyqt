import sys
from screen import *

from PyQt5 import QtWidgets, QtCore

import matplotlib

import numpy as np

matplotlib.use('QT5Agg')


class DialogApplication(QtWidgets.QDialog):
    """
    """
    def __init__(self):
        super().__init__()

        # Set up the dialog
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)
    
        self.axes = self.dialog.mplwidget.canvas.axes

        self.axes.plot(np.array([1,2,4,8,3,5,2]), color='tab:red')
        self.axesLeft = self.axes.twinx()
        self.axesLeft.plot(np.array([3,5,7,6,3,2,7]), color='tab:blue')

        # Show
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = DialogApplication()
    dialog.show()
    sys.exit(app.exec_())





