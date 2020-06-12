import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTableWidget,QTableWidgetItem,QVBoxLayout

def getSelectedItemData():
    for currentItem in tableWidget.selectedItems():
        print("ROw : "+str(currentItem.row())+" Column : "+str(currentItem.column())+" "+currentItem.text())

app=QApplication(sys.argv)

qwidget=QWidget()

qwidget.setWindowTitle("Python GUI Table")
qwidget.resize(700,450)

layout=QVBoxLayout()

tableWidget=QTableWidget()
tableWidget.setColumnCount(5)
tableWidget.setRowCount(10)

# adding item in table
tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem("Day"))
tableWidget.setHorizontalHeaderItem(1,QTableWidgetItem("Time"))
tableWidget.setHorizontalHeaderItem(2,QTableWidgetItem("Course Code"))
tableWidget.setHorizontalHeaderItem(3,QTableWidgetItem("Course Title"))
tableWidget.setHorizontalHeaderItem(4,QTableWidgetItem("Teacher Initial"))
# Data Entry
# Row 1
tableWidget.setItem(0,0,QTableWidgetItem("Monday"))
tableWidget.setItem(0,1,QTableWidgetItem("1.00PM-2.30PM"))
tableWidget.setItem(0,2,QTableWidgetItem("CSE322"))
tableWidget.setItem(0,3,QTableWidgetItem("Computer Architecture & Organization"))
tableWidget.setItem(0,4,QTableWidgetItem("AKMM"))

# Row 2
tableWidget.setItem(1,0,QTableWidgetItem("Monday"))
tableWidget.setItem(1,1,QTableWidgetItem("2.30PM-4.00PM"))
tableWidget.setItem(1,2,QTableWidgetItem("CSE321"))
tableWidget.setItem(1,3,QTableWidgetItem("System Analysis and Design"))
tableWidget.setItem(1,4,QTableWidgetItem("NIS"))

# Row 3
tableWidget.setItem(2,0,QTableWidgetItem("Monday"))
tableWidget.setItem(2,1,QTableWidgetItem("4.00PM-5.30PM"))
tableWidget.setItem(2,2,QTableWidgetItem("ECO314"))
tableWidget.setItem(2,3,QTableWidgetItem("Economics"))
tableWidget.setItem(2,4,QTableWidgetItem("SM"))

# Row 4
tableWidget.setItem(3,0,QTableWidgetItem("Tuesday"))
tableWidget.setItem(3,1,QTableWidgetItem("10.00AM-11.30AM"))
tableWidget.setItem(3,2,QTableWidgetItem("CSE321"))
tableWidget.setItem(3,3,QTableWidgetItem("System Analysis and Design"))
tableWidget.setItem(3,4,QTableWidgetItem("NIS"))

# Row 5
tableWidget.setItem(4,0,QTableWidgetItem("Tuesday"))
tableWidget.setItem(4,1,QTableWidgetItem("11.30AM-1.00PM"))
tableWidget.setItem(4,2,QTableWidgetItem("CSE323"))
tableWidget.setItem(4,3,QTableWidgetItem("Operating Systems"))
tableWidget.setItem(4,4,QTableWidgetItem("HH"))

# Row 6
tableWidget.setItem(5,0,QTableWidgetItem("Tuesday"))
tableWidget.setItem(5,1,QTableWidgetItem("1.00PM-2.30PM"))
tableWidget.setItem(5,2,QTableWidgetItem("CSE322"))
tableWidget.setItem(5,3,QTableWidgetItem("Computer Architecture & Organization"))
tableWidget.setItem(5,4,QTableWidgetItem("AKMM"))

# Row 7
tableWidget.setItem(6,0,QTableWidgetItem("Wednesday"))
tableWidget.setItem(6,1,QTableWidgetItem("10.00-11.30AM"))
tableWidget.setItem(6,2,QTableWidgetItem("ECO314"))
tableWidget.setItem(6,3,QTableWidgetItem("Economics"))
tableWidget.setItem(6,4,QTableWidgetItem("SM"))


# Row 8
tableWidget.setItem(7,0,QTableWidgetItem("Wednesday"))
tableWidget.setItem(7,1,QTableWidgetItem("11.30AM-1.00PM"))
tableWidget.setItem(7,2,QTableWidgetItem("CSE323"))
tableWidget.setItem(7,3,QTableWidgetItem("Operating Systems"))
tableWidget.setItem(7,4,QTableWidgetItem("HH"))

# Row 9
tableWidget.setItem(8,0,QTableWidgetItem("Thursday"))
tableWidget.setItem(8,1,QTableWidgetItem("8.30AM-10.00AM"))
tableWidget.setItem(8,2,QTableWidgetItem("CSE324"))
tableWidget.setItem(8,3,QTableWidgetItem("Operating Systems Lab"))
tableWidget.setItem(8,4,QTableWidgetItem("HH"))

# Row 10
tableWidget.setItem(9,0,QTableWidgetItem("Thursday"))
tableWidget.setItem(9,1,QTableWidgetItem("10.00AM-11.30AM"))
tableWidget.setItem(9,2,QTableWidgetItem("CSE324"))
tableWidget.setItem(9,3,QTableWidgetItem("Operating Systems Lab"))
tableWidget.setItem(9,4,QTableWidgetItem("HH"))

tableWidget.doubleClicked.connect(getSelectedItemData)
layout.addWidget(tableWidget)
qwidget.setLayout(layout)
qwidget.show()

sys.exit(app.exec_())