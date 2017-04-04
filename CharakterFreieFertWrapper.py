# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 18:09:33 2017

@author: Aeolitus
"""
import Fertigkeiten
from Wolke import Wolke
import CharakterFreieFert
from PyQt5 import QtWidgets, QtCore

class CharakterFreieFertWrapper(QtCore.QObject):
    modified = QtCore.pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.formFert = QtWidgets.QWidget()
        self.uiFert = CharakterFreieFert.Ui_Form()
        self.uiFert.setupUi(self.formFert)
        
        for count in range(2,13):
            eval("self.uiFert.editFF" + str(count) + ".editingFinished.connect(self.changedEntry)")
            eval("self.uiFert.comboFF" + str(count) + ".currentIndexChanged.connect(self.changedEntry)")
        
        self.loadFreie()
        
    def loadFreie(self):
        try:
            count = 2
            for el in Wolke.Char.freieFertigkeiten:
                if el.name == "Muttersprache":
                    continue
                eval("self.uiFert.editFF" + str(count) + ".blockSignals(True)")
                eval("self.uiFert.comboFF" + str(count) + ".blockSignals(True)")
                eval("self.uiFert.editFF" + str(count) + ".setText(\"" + el.name + "\")")
                eval("self.uiFert.comboFF" + str(count) + ".setCurrentIndex(" + str(el.wert-1) + ")")
                eval("self.uiFert.editFF" + str(count) + ".blockSignals(False)")
                eval("self.uiFert.comboFF" + str(count) + ".blockSignals(False)")
                count += 1
                if count > 12:
                    break
        except:
            print("Error in loadFreie")
    
    def updateFreie(self):
        Wolke.Char.freieFertigkeiten.clear()
        for count in range(1,13):
            tmp = eval("self.uiFert.editFF" + str(count) + ".text()")
            if tmp != "":
                val = eval("self.uiFert.comboFF" + str(count) + ".currentIndex()")+1
                fert = Fertigkeiten.FreieFertigkeit()
                fert.name = tmp
                fert.wert = val
                Wolke.Char.freieFertigkeiten.append(fert)
        self.modified.emit()
        
    def changedEntry(self):
        self.updateFreie()
        self.modified.emit()