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
       <string>Создать</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QPushButton" name="pushButton_3">
   <property name="geometry">
    <rect>
     <x>180</x>
     <y>90</y>
     <width>141</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string>Изменить</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


template1 = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>735</width>
    <height>337</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>30</y>
     <width>591</width>
     <height>231</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLineEdit" name="lineEdit_2"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit_5"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit_7"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit_6"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit_4"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit_3"/>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="verticalLayoutWidget_2">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>30</y>
     <width>112</width>
     <height>221</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout_2">
    <item alignment="Qt::AlignLeft">
     <widget class="QLabel" name="label">
      <property name="layoutDirection">
       <enum>Qt::RightToLeft</enum>
      </property>
      <property name="text">
       <string>ID</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_2">
      <property name="text">
       <string>Название</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_3">
      <property name="text">
       <string>Степень
обжарки</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_4">
      <property name="text">
       <string>Молотый / в зёрнах</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_5">
      <property name="text">
       <string>Описание</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_6">
      <property name="text">
       <string>Цена</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_7">
      <property name="text">
       <string>Объём</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>590</x>
     <y>270</y>
     <width>111</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string>Сохранить</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


template2 = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>857</width>
    <height>322</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>0</y>
     <width>341</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Мы с вами будем заменять по ID, на остальное кофе не хватило</string>
   </property>
  </widget>
  <widget class="QWidget" name="verticalLayoutWidget_2">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>30</y>
     <width>112</width>
     <height>221</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout_2">
    <item alignment="Qt::AlignLeft">
     <widget class="QLabel" name="label_2">
      <property name="layoutDirection">
       <enum>Qt::RightToLeft</enum>
      </property>
      <property name="text">
       <string>ID</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_3">
      <property name="text">
       <string>Название</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_4">
      <property name="text">
       <string>Степень
обжарки</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_5">
      <property name="text">
       <string>Молотый / в зёрнах</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_6">
      <property name="text">
       <string>Описание</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_7">
      <property name="text">
       <string>Цена</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignRight">
     <widget class="QLabel" name="label_8">
      <property name="text">
       <string>Объём</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>30</y>
     <width>591</width>
     <height>231</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLineEdit" name="lineEdit_2"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit_5"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit_7"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit_6"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit_4"/>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit_3"/>
    </item>
   </layout>
  </widget>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>270</y>
     <width>111</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Изменить</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_9">
   <property name="geometry">
    <rect>
     <x>710</x>
     <y>40</y>
     <width>111</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>по этой меняем</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Create(QDialog):
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(template1)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.really_create)

    def really_create(self):
        try:
            tabl = sqlite3.connect('coffee.sqlite')
            cur = tabl.cursor()
            cur.execute(f'''INSERT INTO coffee VALUES({int(self.lineEdit_2.text())}, '{self.lineEdit.text()}', {int(self.lineEdit_5.text())}, 
                            {bool(self.lineEdit_7.text())}, '{self.lineEdit_6.text()}', {int(self.lineEdit_4.text())}, {float(self.lineEdit_3.text())})''')
            tabl.commit()
            tabl.close()
            self.close()
        except Exception:
            pass  # В QDialog нету statusBar()


class Swap(QDialog):
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(template2)
        uic.loadUi(f, self)

        self.pushButton.clicked.connect(self.really_swap)

    def really_swap(self):
        try:
            tabl = sqlite3.connect('coffee.sqlite')
            cur = tabl.cursor()
            cur.execute(f'''UPDATE coffee 
                        SET name = '{self.lineEdit.text()}', roasting = {int(self.lineEdit_5.text())}, moloti_or_no = '{self.lineEdit_7.text()}', description = '{self.lineEdit_6.text()}', price = {int(self.lineEdit_4.text())}, size = {float(self.lineEdit_3.text())} 
                        WHERE id = {int(self.lineEdit_2.text())}''')
            tabl.commit()
            tabl.close()
            self.close()
        except Exception:
            pass  # В QDialog нету statusBar()


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        tabl = sqlite3.connect('coffee.sqlite')
        self.cur = tabl.cursor()
        self.pushButton.clicked.connect(self.view)
        self.pushButton_2.clicked.connect(self.new)
        self.pushButton_3.clicked.connect(self.new)

    def new(self):
        if self.sender().objectName() == 'pushButton_2':
            self.Cr = Create(self)
            self.Cr.show()
        else:
            self.Sw = Swap(self)
            self.Sw.show()

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
