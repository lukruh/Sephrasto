# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(974, 659)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelEinstellungen = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelEinstellungen.setFont(font)
        self.labelEinstellungen.setObjectName("labelEinstellungen")
        self.verticalLayout_4.addWidget(self.labelEinstellungen)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboHausregeln = QtWidgets.QComboBox(self.groupBox_3)
        self.comboHausregeln.setObjectName("comboHausregeln")
        self.gridLayout_5.addWidget(self.comboHausregeln, 3, 1, 1, 1)
        self.checkFinanzen = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkFinanzen.setChecked(True)
        self.checkFinanzen.setObjectName("checkFinanzen")
        self.gridLayout_5.addWidget(self.checkFinanzen, 1, 0, 1, 2)
        self.checkRegeln = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkRegeln.setChecked(True)
        self.checkRegeln.setTristate(False)
        self.checkRegeln.setObjectName("checkRegeln")
        self.gridLayout_5.addWidget(self.checkRegeln, 7, 0, 1, 2)
        self.comboRegelnGroesse = QtWidgets.QComboBox(self.groupBox_3)
        self.comboRegelnGroesse.setObjectName("comboRegelnGroesse")
        self.comboRegelnGroesse.addItem("")
        self.comboRegelnGroesse.addItem("")
        self.comboRegelnGroesse.addItem("")
        self.gridLayout_5.addWidget(self.comboRegelnGroesse, 8, 1, 1, 1)
        self.comboCharsheet = QtWidgets.QComboBox(self.groupBox_3)
        self.comboCharsheet.setObjectName("comboCharsheet")
        self.gridLayout_5.addWidget(self.comboCharsheet, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 8, 0, 1, 1)
        self.checkUeberPDF = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkUeberPDF.setObjectName("checkUeberPDF")
        self.gridLayout_5.addWidget(self.checkUeberPDF, 2, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 5, 0, 1, 1)
        self.labelReload = QtWidgets.QLabel(self.groupBox_3)
        self.labelReload.setStyleSheet("background-color: rgb(255, 255, 0); color: black;")
        self.labelReload.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelReload.setWordWrap(True)
        self.labelReload.setObjectName("labelReload")
        self.gridLayout_5.addWidget(self.labelReload, 9, 0, 1, 2)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.labelEP = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelEP.setFont(font)
        self.labelEP.setObjectName("labelEP")
        self.verticalLayout_4.addWidget(self.labelEP)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinFertigkeitenSpent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinFertigkeitenSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinFertigkeitenSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinFertigkeitenSpent.setReadOnly(True)
        self.spinFertigkeitenSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinFertigkeitenSpent.setMaximum(999999)
        self.spinFertigkeitenSpent.setObjectName("spinFertigkeitenSpent")
        self.gridLayout_2.addWidget(self.spinFertigkeitenSpent, 3, 1, 1, 1)
        self.spinUebernatuerlichPercent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinUebernatuerlichPercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUebernatuerlichPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUebernatuerlichPercent.setReadOnly(True)
        self.spinUebernatuerlichPercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUebernatuerlichPercent.setMaximum(100)
        self.spinUebernatuerlichPercent.setObjectName("spinUebernatuerlichPercent")
        self.gridLayout_2.addWidget(self.spinUebernatuerlichPercent, 6, 2, 1, 1)
        self.labelUeber3 = QtWidgets.QLabel(self.groupBox_2)
        self.labelUeber3.setMinimumSize(QtCore.QSize(230, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        self.labelUeber3.setFont(font)
        self.labelUeber3.setObjectName("labelUeber3")
        self.gridLayout_2.addWidget(self.labelUeber3, 8, 0, 1, 1)
        self.spinProfanPercent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinProfanPercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinProfanPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinProfanPercent.setReadOnly(True)
        self.spinProfanPercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinProfanPercent.setMaximum(100)
        self.spinProfanPercent.setObjectName("spinProfanPercent")
        self.gridLayout_2.addWidget(self.spinProfanPercent, 2, 2, 1, 1)
        self.spinVorteileSpent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinVorteileSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinVorteileSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinVorteileSpent.setReadOnly(True)
        self.spinVorteileSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinVorteileSpent.setMaximum(99999999)
        self.spinVorteileSpent.setObjectName("spinVorteileSpent")
        self.gridLayout_2.addWidget(self.spinVorteileSpent, 1, 1, 1, 1)
        self.spinAttributeSpent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinAttributeSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinAttributeSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinAttributeSpent.setReadOnly(True)
        self.spinAttributeSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinAttributeSpent.setMaximum(99999999)
        self.spinAttributeSpent.setObjectName("spinAttributeSpent")
        self.gridLayout_2.addWidget(self.spinAttributeSpent, 0, 1, 1, 1)
        self.spinUeberTalenteSpent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinUeberTalenteSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUeberTalenteSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUeberTalenteSpent.setReadOnly(True)
        self.spinUeberTalenteSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUeberTalenteSpent.setMaximum(999999)
        self.spinUeberTalenteSpent.setObjectName("spinUeberTalenteSpent")
        self.gridLayout_2.addWidget(self.spinUeberTalenteSpent, 8, 1, 1, 1)
        self.spinFreieSpent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinFreieSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinFreieSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinFreieSpent.setReadOnly(True)
        self.spinFreieSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinFreieSpent.setMaximum(999999)
        self.spinFreieSpent.setObjectName("spinFreieSpent")
        self.gridLayout_2.addWidget(self.spinFreieSpent, 5, 1, 1, 1)
        self.spinUeberFertigkeitenPercent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinUeberFertigkeitenPercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUeberFertigkeitenPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUeberFertigkeitenPercent.setReadOnly(True)
        self.spinUeberFertigkeitenPercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUeberFertigkeitenPercent.setMaximum(100)
        self.spinUeberFertigkeitenPercent.setObjectName("spinUeberFertigkeitenPercent")
        self.gridLayout_2.addWidget(self.spinUeberFertigkeitenPercent, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setMinimumSize(QtCore.QSize(230, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinAttributePercent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinAttributePercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinAttributePercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinAttributePercent.setReadOnly(True)
        self.spinAttributePercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinAttributePercent.setMaximum(100)
        self.spinAttributePercent.setObjectName("spinAttributePercent")
        self.gridLayout_2.addWidget(self.spinAttributePercent, 0, 2, 1, 1)
        self.spinUeberTalentePercent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinUeberTalentePercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUeberTalentePercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUeberTalentePercent.setReadOnly(True)
        self.spinUeberTalentePercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUeberTalentePercent.setMaximum(100)
        self.spinUeberTalentePercent.setObjectName("spinUeberTalentePercent")
        self.gridLayout_2.addWidget(self.spinUeberTalentePercent, 8, 2, 1, 1)
        self.labelUeber1 = QtWidgets.QLabel(self.groupBox_2)
        self.labelUeber1.setMinimumSize(QtCore.QSize(230, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelUeber1.setFont(font)
        self.labelUeber1.setObjectName("labelUeber1")
        self.gridLayout_2.addWidget(self.labelUeber1, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setMinimumSize(QtCore.QSize(230, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.spinUebernatuerlichSpent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinUebernatuerlichSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUebernatuerlichSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUebernatuerlichSpent.setReadOnly(True)
        self.spinUebernatuerlichSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUebernatuerlichSpent.setMaximum(999999)
        self.spinUebernatuerlichSpent.setObjectName("spinUebernatuerlichSpent")
        self.gridLayout_2.addWidget(self.spinUebernatuerlichSpent, 6, 1, 1, 1)
        self.spinUeberFertigkeitenSpent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinUeberFertigkeitenSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUeberFertigkeitenSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUeberFertigkeitenSpent.setReadOnly(True)
        self.spinUeberFertigkeitenSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUeberFertigkeitenSpent.setMaximum(999999)
        self.spinUeberFertigkeitenSpent.setObjectName("spinUeberFertigkeitenSpent")
        self.gridLayout_2.addWidget(self.spinUeberFertigkeitenSpent, 7, 1, 1, 1)
        self.spinFreiePercent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinFreiePercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinFreiePercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinFreiePercent.setReadOnly(True)
        self.spinFreiePercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinFreiePercent.setMaximum(100)
        self.spinFreiePercent.setObjectName("spinFreiePercent")
        self.gridLayout_2.addWidget(self.spinFreiePercent, 5, 2, 1, 1)
        self.spinFertigkeitenPercent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinFertigkeitenPercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinFertigkeitenPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinFertigkeitenPercent.setReadOnly(True)
        self.spinFertigkeitenPercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinFertigkeitenPercent.setMaximum(100)
        self.spinFertigkeitenPercent.setObjectName("spinFertigkeitenPercent")
        self.gridLayout_2.addWidget(self.spinFertigkeitenPercent, 3, 2, 1, 1)
        self.spinTalentePercent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinTalentePercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinTalentePercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinTalentePercent.setReadOnly(True)
        self.spinTalentePercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinTalentePercent.setMaximum(100)
        self.spinTalentePercent.setObjectName("spinTalentePercent")
        self.gridLayout_2.addWidget(self.spinTalentePercent, 4, 2, 1, 1)
        self.spinProfanSpent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinProfanSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinProfanSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinProfanSpent.setReadOnly(True)
        self.spinProfanSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinProfanSpent.setMaximum(999999)
        self.spinProfanSpent.setObjectName("spinProfanSpent")
        self.gridLayout_2.addWidget(self.spinProfanSpent, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMinimumSize(QtCore.QSize(230, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setMinimumSize(QtCore.QSize(230, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)
        self.labelUeber2 = QtWidgets.QLabel(self.groupBox_2)
        self.labelUeber2.setMinimumSize(QtCore.QSize(230, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        self.labelUeber2.setFont(font)
        self.labelUeber2.setObjectName("labelUeber2")
        self.gridLayout_2.addWidget(self.labelUeber2, 7, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setMinimumSize(QtCore.QSize(230, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMinimumSize(QtCore.QSize(230, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinTalenteSpent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinTalenteSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinTalenteSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinTalenteSpent.setReadOnly(True)
        self.spinTalenteSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinTalenteSpent.setMaximum(999999)
        self.spinTalenteSpent.setObjectName("spinTalenteSpent")
        self.gridLayout_2.addWidget(self.spinTalenteSpent, 4, 1, 1, 1)
        self.spinVorteilePercent = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinVorteilePercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinVorteilePercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinVorteilePercent.setReadOnly(True)
        self.spinVorteilePercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinVorteilePercent.setMaximum(100)
        self.spinVorteilePercent.setObjectName("spinVorteilePercent")
        self.gridLayout_2.addWidget(self.spinVorteilePercent, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelNotiz = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelNotiz.setFont(font)
        self.labelNotiz.setObjectName("labelNotiz")
        self.verticalLayout_3.addWidget(self.labelNotiz)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.teNotiz = QtWidgets.QPlainTextEdit(self.groupBox)
        self.teNotiz.setPlainText("")
        self.teNotiz.setObjectName("teNotiz")
        self.gridLayout_3.addWidget(self.teNotiz, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelEinstellungen.setText(_translate("Form", "Charakter-Einstellungen"))
        self.checkFinanzen.setText(_translate("Form", "Finanzen anzeigen"))
        self.checkRegeln.setText(_translate("Form", "Dem Charakterbogen relevante Ilaris Regeln anhängen"))
        self.comboRegelnGroesse.setItemText(0, _translate("Form", "Klein"))
        self.comboRegelnGroesse.setItemText(1, _translate("Form", "Mittel"))
        self.comboRegelnGroesse.setItemText(2, _translate("Form", "Groß"))
        self.label_5.setText(_translate("Form", "Hausregeln:"))
        self.label_7.setText(_translate("Form", "Regeln Schriftgröße:"))
        self.checkUeberPDF.setText(_translate("Form", "PDF-Ausgabe von übernatürlichen Fertigkeiten manuell auswählen"))
        self.label_6.setText(_translate("Form", "Charakterbogen:"))
        self.labelReload.setText(_translate("Form", "Der Charakter muss gespeichert und neu geladen werden, damit alle Änderungen übernommen werden können!"))
        self.labelEP.setText(_translate("Form", "EP-Verteilung"))
        self.spinFertigkeitenSpent.setSuffix(_translate("Form", " EP"))
        self.spinUebernatuerlichPercent.setSuffix(_translate("Form", " %"))
        self.labelUeber3.setText(_translate("Form", "    Talente"))
        self.spinProfanPercent.setSuffix(_translate("Form", " %"))
        self.spinVorteileSpent.setSuffix(_translate("Form", " EP"))
        self.spinAttributeSpent.setSuffix(_translate("Form", " EP"))
        self.spinUeberTalenteSpent.setSuffix(_translate("Form", " EP"))
        self.spinFreieSpent.setSuffix(_translate("Form", " EP"))
        self.spinUeberFertigkeitenPercent.setSuffix(_translate("Form", " %)"))
        self.spinUeberFertigkeitenPercent.setPrefix(_translate("Form", "("))
        self.label_2.setText(_translate("Form", "Vorteile"))
        self.spinAttributePercent.setSuffix(_translate("Form", " %"))
        self.spinUeberTalentePercent.setSuffix(_translate("Form", " %)"))
        self.spinUeberTalentePercent.setPrefix(_translate("Form", "("))
        self.labelUeber1.setText(_translate("Form", "Übernatürliche Fertigkeiten und Talente"))
        self.label_4.setText(_translate("Form", "    Freie Fertigkeiten"))
        self.spinUebernatuerlichSpent.setSuffix(_translate("Form", " EP"))
        self.spinUeberFertigkeitenSpent.setSuffix(_translate("Form", " EP"))
        self.spinFreiePercent.setSuffix(_translate("Form", " %)"))
        self.spinFreiePercent.setPrefix(_translate("Form", "("))
        self.spinFertigkeitenPercent.setSuffix(_translate("Form", " %)"))
        self.spinFertigkeitenPercent.setPrefix(_translate("Form", "("))
        self.spinTalentePercent.setSuffix(_translate("Form", " %)"))
        self.spinTalentePercent.setPrefix(_translate("Form", "("))
        self.spinProfanSpent.setSuffix(_translate("Form", " EP"))
        self.label.setText(_translate("Form", "Attribute"))
        self.label_9.setText(_translate("Form", "    Talente"))
        self.labelUeber2.setText(_translate("Form", "    Fertigkeiten"))
        self.label_8.setText(_translate("Form", "    Fertigkeiten"))
        self.label_3.setText(_translate("Form", "Profane Fertigkeiten und Talente"))
        self.spinTalenteSpent.setSuffix(_translate("Form", " EP"))
        self.spinVorteilePercent.setSuffix(_translate("Form", " %"))
        self.labelNotiz.setText(_translate("Form", "Notiz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())