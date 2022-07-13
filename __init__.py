import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from . import parsers

parsers.citation()

def __init_plugin__(app=None):
    from pymol.plugins import addmenuitemqt
    addmenuitemqt('Dlg Parse', dlg_parse_gui)

dialog = None


def dlg_parse_gui():
    # pymol.Qt provides the PyQt5 interface, but may support PyQt4 and/or PySide as well
    from pymol.Qt import QtWidgets

    global dialog
    
    if dialog is None:
        # create a new (empty) Window
        dialog = make_dialog()
    dialog.show()

single_pdbqt_file = None
single_dlg_file = None

def make_dialog():
    # entry point to PyMOL's API
    from pymol import cmd

    # pymol.Qt provides the PyQt5 interface, but may support PyQt4
    # and/or PySide as well
    from pymol.Qt import QtWidgets
    from pymol.Qt.utils import loadUi
    from pymol.Qt.utils import getSaveFileNameWithExt

    # create a new Window
    dialog = QtWidgets.QDialog()

    # populate the Window from our *.ui file which was created with the Qt Designer
    uifile = os.path.join(os.path.dirname(__file__), 'demowidget.ui')
    form = loadUi(uifile, dialog)

        
    ## callback for the "submit" button
    def submit_vina():
        global vina_log_file_name 
        vina_log_file_name  = form.input_vina.text()
        parsers.parse_vina(vina_log_file_name)

    def submit_vina_pdbqt_fol():
        vina_pdbqt_fol = form.input_vina_pdbqt_fol()
        parsers.parse_vina_pdbqt(vina_pdbqt_fol)


    def submit_dlg():
        global folder_name

        folder_name = form.input_dlg.text()

        if str(folder_name).endswith(".dlg"):
            parsers.score(folder_name)
        else:
            parsers.parse_it(folder_name)
    

    def close():
        dialog.close()

    def help():
        print("To view all docking scores in all autodock folder, \nenter main docking folder \nDock folder - working directory of autodock\nMain docking folder - Folder which contain all docking folders")
    

    # connect the signals to the slots

    # hook up button callbacks
    form.pushButton_submit_dlg.clicked.connect(submit_dlg)
    form.pushButton_submit_vina.clicked.connect(submit_vina)
    form.pushButton_submit_vina_pdbqt_fol.clicked.connect(submit_vina_pdbqt_fol)
    form.pushButton_close.clicked.connect(close)
    form.pushButton_help.clicked.connect(help)

    return dialog

