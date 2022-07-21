import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import parsers

from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication([])

parsers.citation()

def __init_plugin__(app=None):
    from pymol.plugins import addmenuitemqt
    addmenuitemqt('Docking score Parser', dlg_parse_gui)

dialog = None


def dlg_parse_gui():
    # pymol.Qt provides the PyQt5 interface, but may support PyQt4 and/or PySide as well
    from pymol.Qt import QtWidgets

    global dialog
    
    if dialog is None:
        # create a new (empty) Window
        dialog = make_dialog()
    dialog.show()


def make_dialog():
    # entry point to PyMOL's API
    from pymol import cmd

    # pymol.Qt provides the PyQt5 interface, but may support PyQt4
    # and/or PySide as well
    from pymol.Qt import QtWidgets
    from pymol.Qt.utils import loadUi

    # create a new Window
    dialog = QtWidgets.QDialog()

    # populate the Window from our *.ui file which was created with the Qt Designer
    uifile = os.path.join(os.path.dirname(__file__), 'demowidget.ui')
    form = loadUi(uifile, dialog)

        
    ## callback for the "submit" button
    def submit_vina_log_fol():
        vina_log_folder  = form.input_vina_log.text()
        parsers.parse_vina_log(vina_log_folder)

    def submit_vina_pdbqt_fol():
        vina_pdbqt_fol = form.input_vina_pdbqt_fol.text()
        parsers.parse_vina_pdbqt(vina_pdbqt_fol)


    def submit_dlg_fol():
        dlg_fol = form.input_dlg.text()
        parsers.parse_dlg(dlg_fol)
    

    def close():
        print("Thank you for using this plugin")
        print("For feedback write to karthikn130@gmail.com")
        dialog.close()

    def help():
        print("***************************************************************************")
        print("Version 2.0")
        print("This tool shows the docking scores from ")
        print("                1. Autodock dlg file located in subfolders")
        print("                2. Autodock vina output log file located in subfolders")
        print("                3. Autodock vina output pdbqt file located in subfolders")
        print("To view all docking scores from working directory or Main docking folder")
        print("Enter the Main docking folder location and press submit")
        print("Dock folder - working directory of autodock")
        print("Main docking folder - Folder which contain all docking folders")
        print("For more detailed help visit PymolBiomolecules Youtube Chennel")
        print("***************************************************************************")
        print("Thank you for using this plugin")
        print("For feedback write to karthikn130@gmail.com")
    
    def browse_dlg():
        # browse for a folder
        folder = QFileDialog.getExistingDirectory(dialog, "Select main docking folder - Autodock")
        form.input_dlg.setText(folder)

    def browse_vina_log():
        # browse for a folder
        folder = QFileDialog.getExistingDirectory(dialog, "Select main docking folder - Autodock vina")
        form.input_vina_log.setText(folder)

    def browse_vina_pdbqt():
        # browse for a folder
        folder = QFileDialog.getExistingDirectory(dialog, "Select main docking folder - Autodock vina")
        form.input_vina_pdbqt_fol.setText(folder)


    # hook up the buttons to their callback functions

    # hook up submit buttons
    form.pushButton_submit_dlg.clicked.connect(submit_dlg_fol)
    form.pushButton_submit_vina.clicked.connect(submit_vina_log_fol)
    form.pushButton_submit_vina_pdbqt_fol.clicked.connect(submit_vina_pdbqt_fol)

    # hook up close and help button
    form.pushButton_close.clicked.connect(close)
    form.pushButton_help.clicked.connect(help)

    # hook up browse button
    form.browse_dlg.clicked.connect(browse_dlg)
    form.browse_log.clicked.connect(browse_vina_log)
    form.browse_pdbqt.clicked.connect(browse_vina_pdbqt)

    return dialog




if __name__ == '__main__':
    print("This plugin is intended to be used in pymol")
    parsers.citation()
    
    dialog = make_dialog()
    dialog.show()
    app.exec_()

