# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatenbankEditTalent.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_talentDialog(object):
    def setupUi(self, talentDialog):
        talentDialog.setObjectName("talentDialog")
        talentDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        talentDialog.resize(442, 604)
        self.gridLayout_2 = QtWidgets.QGridLayout(talentDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(talentDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nameEdit = QtWidgets.QLineEdit(talentDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(talentDialog)
        self.label_12.setMinimumSize(QtCore.QSize(110, 0))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(talentDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(talentDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.fertigkeitenEdit = QtWidgets.QLineEdit(talentDialog)
        self.fertigkeitenEdit.setObjectName("fertigkeitenEdit")
        self.gridLayout.addWidget(self.fertigkeitenEdit, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(talentDialog)
        self.label_4.setMinimumSize(QtCore.QSize(110, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.voraussetzungenEdit = QtWidgets.QPlainTextEdit(talentDialog)
        self.voraussetzungenEdit.setObjectName("voraussetzungenEdit")
        self.gridLayout.addWidget(self.voraussetzungenEdit, 7, 1, 1, 1)
        self.checkKommentar = QtWidgets.QCheckBox(talentDialog)
        self.checkKommentar.setObjectName("checkKommentar")
        self.gridLayout.addWidget(self.checkKommentar, 4, 1, 1, 1)
        self.warning = QtWidgets.QLabel(talentDialog)
        self.warning.setVisible(False)
        self.warning.setStyleSheet("background-color: rgb(255, 255, 0); color: black;")
        self.warning.setWordWrap(True)
        self.warning.setObjectName("warning")
        self.gridLayout.addWidget(self.warning, 0, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(talentDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(talentDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.textEdit = QtWidgets.QPlainTextEdit(talentDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 8, 1, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.sortierungEdit = QtWidgets.QSpinBox(talentDialog)
        self.sortierungEdit.setSuffix("")
        self.sortierungEdit.setMinimum(-1)
        self.sortierungEdit.setMaximum(999)
        self.sortierungEdit.setSingleStep(1)
        self.sortierungEdit.setProperty("value", -1)
        self.sortierungEdit.setObjectName("sortierungEdit")
        self.horizontalLayout_12.addWidget(self.sortierungEdit)
        self.gridLayout.addLayout(self.horizontalLayout_12, 9, 1, 1, 1)
        self.label = QtWidgets.QLabel(talentDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonRegulaer = QtWidgets.QRadioButton(talentDialog)
        self.buttonRegulaer.setChecked(True)
        self.buttonRegulaer.setObjectName("buttonRegulaer")
        self.verticalLayout.addWidget(self.buttonRegulaer)
        self.buttonVerbilligt = QtWidgets.QRadioButton(talentDialog)
        self.buttonVerbilligt.setObjectName("buttonVerbilligt")
        self.verticalLayout.addWidget(self.buttonVerbilligt)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonSpezial = QtWidgets.QRadioButton(talentDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSpezial.sizePolicy().hasHeightForWidth())
        self.buttonSpezial.setSizePolicy(sizePolicy)
        self.buttonSpezial.setObjectName("buttonSpezial")
        self.horizontalLayout.addWidget(self.buttonSpezial)
        self.spinKosten = QtWidgets.QSpinBox(talentDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinKosten.sizePolicy().hasHeightForWidth())
        self.spinKosten.setSizePolicy(sizePolicy)
        self.spinKosten.setMinimumSize(QtCore.QSize(60, 0))
        self.spinKosten.setAlignment(QtCore.Qt.AlignCenter)
        self.spinKosten.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinKosten.setMinimum(0)
        self.spinKosten.setMaximum(200)
        self.spinKosten.setSingleStep(20)
        self.spinKosten.setObjectName("spinKosten")
        self.horizontalLayout.addWidget(self.spinKosten)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkVariable = QtWidgets.QCheckBox(talentDialog)
        self.checkVariable.setObjectName("checkVariable")
        self.horizontalLayout_2.addWidget(self.checkVariable)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(talentDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.checkCheatsheet = QtWidgets.QCheckBox(talentDialog)
        self.checkCheatsheet.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkCheatsheet.setChecked(True)
        self.checkCheatsheet.setObjectName("checkCheatsheet")
        self.gridLayout.addWidget(self.checkCheatsheet, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(talentDialog)
        self.buttonBox.accepted.connect(talentDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(talentDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(talentDialog)
        talentDialog.setTabOrder(self.nameEdit, self.buttonRegulaer)
        talentDialog.setTabOrder(self.buttonRegulaer, self.buttonVerbilligt)
        talentDialog.setTabOrder(self.buttonVerbilligt, self.buttonSpezial)
        talentDialog.setTabOrder(self.buttonSpezial, self.spinKosten)
        talentDialog.setTabOrder(self.spinKosten, self.checkVariable)
        talentDialog.setTabOrder(self.checkVariable, self.checkKommentar)
        talentDialog.setTabOrder(self.checkKommentar, self.checkCheatsheet)
        talentDialog.setTabOrder(self.checkCheatsheet, self.fertigkeitenEdit)
        talentDialog.setTabOrder(self.fertigkeitenEdit, self.voraussetzungenEdit)
        talentDialog.setTabOrder(self.voraussetzungenEdit, self.textEdit)
        talentDialog.setTabOrder(self.textEdit, self.sortierungEdit)

    def retranslateUi(self, talentDialog):
        _translate = QtCore.QCoreApplication.translate
        talentDialog.setWindowTitle(_translate("talentDialog", "Sephrasto - Talent bearbeiten..."))
        self.label_12.setText(_translate("talentDialog", "Sortierung"))
        self.label_2.setText(_translate("talentDialog", "Lernkosten"))
        self.label_5.setText(_translate("talentDialog", "Beschreibung"))
        self.label_4.setText(_translate("talentDialog", "Voraussetzungen"))
        self.checkKommentar.setText(_translate("talentDialog", "Nutzern erlauben einen Kommentar einzutragen"))
        self.warning.setText(_translate("talentDialog", "<html><head/><body><p>Dies ist ein Ilaris-Standardtalent. Sobald du hier etwas veränderst, bekommst du eine persönliche Kopie und das Original wird in den Hausregeln gelöscht. Damit erhältst du für dieses Talent keine automatischen Updates mehr mit neuen Sephrasto-Versionen.</p></body></html>"))
        self.label_6.setText(_translate("talentDialog", "Kommentar"))
        self.label_3.setText(_translate("talentDialog", "Fertigkeiten"))
        self.label.setText(_translate("talentDialog", "Talentname"))
        self.buttonRegulaer.setText(_translate("talentDialog", "Reguläres Talent (Kosten nach Fertigkeit)"))
        self.buttonVerbilligt.setText(_translate("talentDialog", "Verbilligtes Talent (Kosten nach Fertigkeit)"))
        self.buttonSpezial.setText(_translate("talentDialog", "Spezialtalent (Kosten frei wählbar)"))
        self.spinKosten.setSuffix(_translate("talentDialog", " EP"))
        self.checkVariable.setText(_translate("talentDialog", "Kosten sind variabel"))
        self.label_7.setText(_translate("talentDialog", "Regelanhang"))
        self.checkCheatsheet.setText(_translate("talentDialog", "Auflisten"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    talentDialog = QtWidgets.QDialog()
    ui = Ui_talentDialog()
    ui.setupUi(talentDialog)
    talentDialog.show()
    sys.exit(app.exec_())
