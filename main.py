from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem
import io
from PyQt6 import uic
import sys
import sqlite3


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>732</width>
    <height>363</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QTableWidget" name="tableWidget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>160</y>
     <width>711</width>
     <height>192</height>
    </rect>
   </property>
   <property name="sizePolicy">
    <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
     <horstretch>0</horstretch>
     <verstretch>0</verstretch>
    </sizepolicy>
   </property>
   <property name="maximumSize">
    <size>
     <width>711</width>
     <height>192</height>
    </size>
   </property>
   <column>
    <property name="text">
     <string>ID</string>
    </property>
    <property name="font">
     <font>
      <strikeout>false</strikeout>
     </font>
    </property>
   </column>
   <column>
    <property name="text">
     <string>Название</string>
    </property>
   </column>
   <column>
    <property name="text">
     <string>Степень обжарки</string>
    </property>
   </column>
   <column>
    <property name="text">
     <string>Молотый/в зернах</string>
    </property>
   </column>
   <column>
    <property name="text">
     <string>Описание</string>
    </property>
   </column>
   <column>
    <property name="text">
     <string>Цена</string>
    </property>
   </column>
   <column>
    <property name="text">
     <string>Объём</string>
    </property>
   </column>
  </widget>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>20</y>
     <width>160</width>
     <height>121</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QPushButton" name="pushButton">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>Отобразить</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_2">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>Изменить</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        tabl = sqlite3.connect('coffee.sqlite')
        self.cur = tabl.cursor()
        self.pushButton.clicked.connect(self.view)

    def view(self):
        g = self.cur.execute('''SELECT * FROM coffee''').fetchall()
        self.tableWidget.setRowCount(len(g))
        b = 0
        for el in g:
            for el1 in el:
                self.tableWidget.setItem(g.index(el), b, QTableWidgetItem(str(el1)))
                b += 1
            b = 0


if __name__ == '__main__':
    ex = QApplication(sys.argv)
    ex1 = MyWidget()
    ex1.show()
    ex.exec()