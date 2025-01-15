from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem
import sys
import sqlite3
from main_design import Ui_Dialog
from addEditCoffeeForm import Ui_Dialog1
from saveCoffeeForm import Ui_Dialog2


class Create(QDialog, Ui_Dialog1):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.really_create)

    def really_create(self):
        try:
            tabl = sqlite3.connect('data/coffee.sqlite')
            cur = tabl.cursor()
            cur.execute(f'''INSERT INTO coffee VALUES({int(self.lineEdit_2.text())}, '{self.lineEdit.text()}', {int(self.lineEdit_5.text())}, 
                            {bool(self.lineEdit_7.text())}, '{self.lineEdit_6.text()}', {int(self.lineEdit_4.text())}, {float(self.lineEdit_3.text())})''')
            tabl.commit()
            tabl.close()
            self.close()
        except Exception:
            pass  # В QDialog нету statusBar()


class Swap(QDialog, Ui_Dialog2):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.really_swap)

    def really_swap(self):
        try:
            tabl = sqlite3.connect('data/coffee.sqlite')
            cur = tabl.cursor()
            cur.execute(f'''UPDATE coffee 
                        SET name = '{self.lineEdit.text()}', roasting = {int(self.lineEdit_5.text())}, moloti_or_no = '{self.lineEdit_7.text()}', description = '{self.lineEdit_6.text()}', price = {int(self.lineEdit_4.text())}, size = {float(self.lineEdit_3.text())} 
                        WHERE id = {int(self.lineEdit_2.text())}''')
            tabl.commit()
            tabl.close()
            self.close()
        except Exception:
            pass  # В QDialog нету statusBar()


class MyWidget(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        tabl = sqlite3.connect('data/coffee.sqlite')
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
