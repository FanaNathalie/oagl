# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QR_code.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 35, 10))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 35, 10))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(14, 170, 41, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 35, 10))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 35, 10))
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(80, 240, 62, 14))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(230, 240, 62, 14))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 270, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 270, 56, 17))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(70, 70, 251, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 110, 251, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(70, 160, 251, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(70, 203, 251, 31))
        self.textEdit_4.setObjectName("textEdit_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Formulaire de contact"))
        self.label_2.setText(_translate("Form", "Nom :"))
        self.label_3.setText(_translate("Form", "Prenom :"))
        self.label_4.setText(_translate("Form", "Matricule :"))
        self.label_5.setText(_translate("Form", "Email :"))
        
        self.label_6.setText(_translate("Form", "Genre :"))
        
        self.radioButton.setText(_translate("Form", "  Femme"))
        self.radioButton_2.setText(_translate("Form", "  Homme"))
        
        self.pushButton.setText(_translate("Form", "Soumettre"))
        self.pushButton_2.setText(_translate("Form", "Effacer"))
        self.pushButton.clicked.connect(self.saisirTexte)
        self.pushButton_2.clicked.connect(self.Effacer)
    def saisirTexte(self):
        self.textEditValue = self.textEdit.toPlainText()
        self.textEditValue_2 = self.textEdit_2.toPlainText()
        self.textEditValue_3 = self.textEdit_3.toPlainText() 
        self.textEditValue_4 = self.textEdit_4.toPlainText() 
        print(self.textEditValue)
        print(self.textEditValue_2)
        print(self.textEditValue_3)
        print(self.textEditValue_4)
    def Effacer(self):
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.textEdit_3.setText("")
        self.textEdit_4.setText("")
       
   
        
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form =QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    
    
    # afficher la fenetre
    Form.show()
    
    
    sys.exit(app.exec_())


