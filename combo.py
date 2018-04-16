import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3

class combodemo(QWidget):
   def __init__(self, parent = None):
        conn=sqlite3.connect('list.db')
        super(combodemo, self).__init__(parent)

        layout = QHBoxLayout()
        self.cb = QComboBox()
        query=conn.execute("SELECT * FROM Lime6")
        str 
        conn.commit()
        for row[0] in query:
          print row[0]
        self.cb.addItem(row[0])
        self.cb.currentIndexChanged.connect(self.selectionchange)

        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("combo box demo")

   def selectionchange(self,i):
      print "Items in the list are :"

      for count in range(self.cb.count()):
         print self.cb.itemText(count)
      print "Current index",i,"selection changed ",self.cb.currentText()

def main():
   app = QApplication(sys.argv)
   ex = combodemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
