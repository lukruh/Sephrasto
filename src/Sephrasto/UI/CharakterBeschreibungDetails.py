# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterBeschreibungDetails.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formBeschreibung(object):
    def setupUi(self, formBeschreibung):
        formBeschreibung.setObjectName("formBeschreibung")
        formBeschreibung.resize(872, 535)
        self.gridLayout_3 = QtWidgets.QGridLayout(formBeschreibung)
        self.gridLayout_3.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(formBeschreibung)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.leAugenfarbe = QtWidgets.QLineEdit(self.tab_2)
        self.leAugenfarbe.setObjectName("leAugenfarbe")
        self.gridLayout_2.addWidget(self.leAugenfarbe, 8, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 5, 4, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setMinimumSize(QtCore.QSize(68, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 4, 1, 1)
        self.leHintergrund6 = QtWidgets.QLineEdit(self.tab_2)
        self.leHintergrund6.setObjectName("leHintergrund6")
        self.gridLayout_2.addWidget(self.leHintergrund6, 12, 4, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 7, 1, 1, 1)
        self.leAussehen1 = QtWidgets.QLineEdit(self.tab_2)
        self.leAussehen1.setObjectName("leAussehen1")
        self.gridLayout_2.addWidget(self.leAussehen1, 9, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 1, 1, 1)
        self.leHintergrund5 = QtWidgets.QLineEdit(self.tab_2)
        self.leHintergrund5.setObjectName("leHintergrund5")
        self.gridLayout_2.addWidget(self.leHintergrund5, 11, 4, 1, 2)
        self.leHintergrund1 = QtWidgets.QLineEdit(self.tab_2)
        self.leHintergrund1.setObjectName("leHintergrund1")
        self.gridLayout_2.addWidget(self.leHintergrund1, 7, 4, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 9, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1)
        self.leHintergrund3 = QtWidgets.QLineEdit(self.tab_2)
        self.leHintergrund3.setObjectName("leHintergrund3")
        self.gridLayout_2.addWidget(self.leHintergrund3, 9, 4, 1, 2)
        self.leAussehen3 = QtWidgets.QLineEdit(self.tab_2)
        self.leAussehen3.setObjectName("leAussehen3")
        self.gridLayout_2.addWidget(self.leAussehen3, 11, 1, 1, 2)
        self.leAussehen4 = QtWidgets.QLineEdit(self.tab_2)
        self.leAussehen4.setObjectName("leAussehen4")
        self.gridLayout_2.addWidget(self.leAussehen4, 12, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 1, 1, 1)
        self.leGroesse = QtWidgets.QLineEdit(self.tab_2)
        self.leGroesse.setObjectName("leGroesse")
        self.gridLayout_2.addWidget(self.leGroesse, 5, 2, 1, 1)
        self.leAussehen2 = QtWidgets.QLineEdit(self.tab_2)
        self.leAussehen2.setObjectName("leAussehen2")
        self.gridLayout_2.addWidget(self.leAussehen2, 10, 1, 1, 2)
        self.chkKultur = QtWidgets.QCheckBox(self.tab_2)
        self.chkKultur.setChecked(True)
        self.chkKultur.setObjectName("chkKultur")
        self.gridLayout_2.addWidget(self.chkKultur, 1, 5, 1, 1)
        self.leHintergrund7 = QtWidgets.QLineEdit(self.tab_2)
        self.leHintergrund7.setObjectName("leHintergrund7")
        self.gridLayout_2.addWidget(self.leHintergrund7, 13, 4, 1, 2)
        self.leGeschlecht = QtWidgets.QLineEdit(self.tab_2)
        self.leGeschlecht.setObjectName("leGeschlecht")
        self.gridLayout_2.addWidget(self.leGeschlecht, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 8, 1, 1, 1)
        self.leKultur = QtWidgets.QLineEdit(self.tab_2)
        self.leKultur.setEnabled(False)
        self.leKultur.setObjectName("leKultur")
        self.gridLayout_2.addWidget(self.leKultur, 1, 2, 1, 3)
        self.leGeburtsdatum = QtWidgets.QLineEdit(self.tab_2)
        self.leGeburtsdatum.setObjectName("leGeburtsdatum")
        self.gridLayout_2.addWidget(self.leGeburtsdatum, 4, 2, 1, 1)
        self.labelImage = QtWidgets.QLabel(self.tab_2)
        self.labelImage.setMinimumSize(QtCore.QSize(208, 272))
        self.labelImage.setMaximumSize(QtCore.QSize(208, 272))
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setWordWrap(True)
        self.labelImage.setObjectName("labelImage")
        self.gridLayout_2.addWidget(self.labelImage, 3, 3, 11, 1)
        self.leHaarfarbe = QtWidgets.QLineEdit(self.tab_2)
        self.leHaarfarbe.setObjectName("leHaarfarbe")
        self.gridLayout_2.addWidget(self.leHaarfarbe, 7, 2, 1, 1)
        self.leHintergrund8 = QtWidgets.QLineEdit(self.tab_2)
        self.leHintergrund8.setObjectName("leHintergrund8")
        self.gridLayout_2.addWidget(self.leHintergrund8, 14, 4, 1, 2)
        self.leHintergrund2 = QtWidgets.QLineEdit(self.tab_2)
        self.leHintergrund2.setObjectName("leHintergrund2")
        self.gridLayout_2.addWidget(self.leHintergrund2, 8, 4, 1, 2)
        self.leProfession = QtWidgets.QLineEdit(self.tab_2)
        self.leProfession.setObjectName("leProfession")
        self.gridLayout_2.addWidget(self.leProfession, 2, 2, 1, 4)
        self.leHintergrund4 = QtWidgets.QLineEdit(self.tab_2)
        self.leHintergrund4.setObjectName("leHintergrund4")
        self.gridLayout_2.addWidget(self.leHintergrund4, 10, 4, 1, 2)
        self.leTitel = QtWidgets.QLineEdit(self.tab_2)
        self.leTitel.setMinimumSize(QtCore.QSize(0, 0))
        self.leTitel.setObjectName("leTitel")
        self.gridLayout_2.addWidget(self.leTitel, 4, 5, 1, 1)
        self.leAussehen6 = QtWidgets.QLineEdit(self.tab_2)
        self.leAussehen6.setObjectName("leAussehen6")
        self.gridLayout_2.addWidget(self.leAussehen6, 14, 1, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonLoadImage = QtWidgets.QPushButton(self.tab_2)
        self.buttonLoadImage.setObjectName("buttonLoadImage")
        self.horizontalLayout.addWidget(self.buttonLoadImage)
        self.buttonDeleteImage = QtWidgets.QPushButton(self.tab_2)
        self.buttonDeleteImage.setObjectName("buttonDeleteImage")
        self.horizontalLayout.addWidget(self.buttonDeleteImage)
        self.gridLayout_2.addLayout(self.horizontalLayout, 14, 3, 1, 1)
        self.leGewicht = QtWidgets.QLineEdit(self.tab_2)
        self.leGewicht.setObjectName("leGewicht")
        self.gridLayout_2.addWidget(self.leGewicht, 6, 2, 1, 1)
        self.leAussehen5 = QtWidgets.QLineEdit(self.tab_2)
        self.leAussehen5.setObjectName("leAussehen5")
        self.gridLayout_2.addWidget(self.leAussehen5, 13, 1, 1, 2)
        self.leHintergrund0 = QtWidgets.QLineEdit(self.tab_2)
        self.leHintergrund0.setObjectName("leHintergrund0")
        self.gridLayout_2.addWidget(self.leHintergrund0, 6, 4, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 2, 1)

        self.retranslateUi(formBeschreibung)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(formBeschreibung)
        formBeschreibung.setTabOrder(self.leKultur, self.chkKultur)
        formBeschreibung.setTabOrder(self.chkKultur, self.leProfession)
        formBeschreibung.setTabOrder(self.leProfession, self.leGeschlecht)
        formBeschreibung.setTabOrder(self.leGeschlecht, self.leGeburtsdatum)
        formBeschreibung.setTabOrder(self.leGeburtsdatum, self.leGroesse)
        formBeschreibung.setTabOrder(self.leGroesse, self.leGewicht)
        formBeschreibung.setTabOrder(self.leGewicht, self.leHaarfarbe)
        formBeschreibung.setTabOrder(self.leHaarfarbe, self.leAugenfarbe)
        formBeschreibung.setTabOrder(self.leAugenfarbe, self.leAussehen1)
        formBeschreibung.setTabOrder(self.leAussehen1, self.leAussehen2)
        formBeschreibung.setTabOrder(self.leAussehen2, self.leAussehen3)
        formBeschreibung.setTabOrder(self.leAussehen3, self.leAussehen4)
        formBeschreibung.setTabOrder(self.leAussehen4, self.leAussehen5)
        formBeschreibung.setTabOrder(self.leAussehen5, self.leAussehen6)
        formBeschreibung.setTabOrder(self.leAussehen6, self.leTitel)
        formBeschreibung.setTabOrder(self.leTitel, self.leHintergrund0)
        formBeschreibung.setTabOrder(self.leHintergrund0, self.leHintergrund1)
        formBeschreibung.setTabOrder(self.leHintergrund1, self.leHintergrund2)
        formBeschreibung.setTabOrder(self.leHintergrund2, self.leHintergrund3)
        formBeschreibung.setTabOrder(self.leHintergrund3, self.leHintergrund4)
        formBeschreibung.setTabOrder(self.leHintergrund4, self.leHintergrund5)
        formBeschreibung.setTabOrder(self.leHintergrund5, self.leHintergrund6)
        formBeschreibung.setTabOrder(self.leHintergrund6, self.leHintergrund7)
        formBeschreibung.setTabOrder(self.leHintergrund7, self.leHintergrund8)
        formBeschreibung.setTabOrder(self.leHintergrund8, self.buttonLoadImage)
        formBeschreibung.setTabOrder(self.buttonLoadImage, self.buttonDeleteImage)
        formBeschreibung.setTabOrder(self.buttonDeleteImage, self.tabWidget)

    def retranslateUi(self, formBeschreibung):
        _translate = QtCore.QCoreApplication.translate
        formBeschreibung.setWindowTitle(_translate("formBeschreibung", "Beschreibung"))
        self.label_10.setText(_translate("formBeschreibung", "Familie/Hintergrund/Herkunft"))
        self.label_2.setText(_translate("formBeschreibung", "Titel"))
        self.label_7.setText(_translate("formBeschreibung", "Haarfarbe"))
        self.label_5.setText(_translate("formBeschreibung", "Größe"))
        self.label_9.setText(_translate("formBeschreibung", "Aussehen"))
        self.label_6.setText(_translate("formBeschreibung", "Gewicht"))
        self.label_3.setText(_translate("formBeschreibung", "Geschlecht"))
        self.label.setText(_translate("formBeschreibung", "Profession"))
        self.label_11.setText(_translate("formBeschreibung", "Kultur"))
        self.chkKultur.setText(_translate("formBeschreibung", "Automatisch befüllen"))
        self.label_4.setText(_translate("formBeschreibung", "Geburtsdatum"))
        self.label_8.setText(_translate("formBeschreibung", "Augenfarbe"))
        self.labelImage.setText(_translate("formBeschreibung", "Bild-Auflösung: 260x340 px\n"
"(wird automatisch angepasst)"))
        self.buttonLoadImage.setText(_translate("formBeschreibung", "Bild laden"))
        self.buttonDeleteImage.setText(_translate("formBeschreibung", "Bild Löschen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("formBeschreibung", "Details"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formBeschreibung = QtWidgets.QWidget()
    ui = Ui_formBeschreibung()
    ui.setupUi(formBeschreibung)
    formBeschreibung.show()
    sys.exit(app.exec_())
