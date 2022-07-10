import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi

print("Welcome")

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
        parse_vina(vina_log_file_name)



    def submit_dlg():
        global folder_name

        folder_name = form.input_dlg.text()

        if str(folder_name).endswith(".dlg"):
            score(folder_name)
        else:
            parse_it(folder_name)
        
    def close():
        dialog.close()

    def help():
        print("Version 1.0 \nTo view all docking scores in all autodock folder, \nenter main docking folder \nDock folder - working directory of autodock\nMain docking folder - Folder which contain all docking folders")
    

    # connect the signals to the slots

    # hook up button callbacks
    form.pushButton_submit_dlg.clicked.connect(submit_dlg)
    form.pushButton_submit_vina.clicked.connect(submit_vina)
    form.pushButton_close.clicked.connect(close)
    form.pushButton_help.clicked.connect(help)

    return dialog


def parse_it(main_folder):
    dlg_files = []

    folder_list = os.listdir(main_folder)
    for eachfolder in folder_list:
        if os.path.isdir(os.path.join(main_folder, eachfolder)) == True:
            if os.path.exists(os.path.join(main_folder, eachfolder, "dock.dlg")):
                dlg_files.append(os.path.join(main_folder, eachfolder, "dock.dlg"))
        else:
            if str(eachfolder).endswith(".dlg"):
                dlg_files.append(os.path.join(main_folder, eachfolder))
    

    for file in dlg_files:
        score(file)
    

def score(dlg_file):
    
    search = "DOCKED: USER    Estimated Free Energy of Binding"
    fhandle = open(dlg_file, encoding='utf-8')
    lines = fhandle.readlines()
    conf_score = []
    for line in lines:
        if line.startswith(search):
            word = line.split()
            score = word[8]
            #list = score.split(sep = "-")
            #number = list[1]
            number = float(score)
            conf_score.append(number)
    conf_score.sort()
    best_conf = conf_score[0]
    print(best_conf, dlg_file)
            

def parse_vina(vina_log):
    search = "   1"
    ligand_name = "Output will be"
    vina_log_file = open(vina_log, "r")
    lines = vina_log_file.readlines()
    for line in lines:
        if line.startswith(ligand_name):
            word = line.split()
            ligand = word[3]
    
        if line.startswith(search):
            word = line.split()
            score = word[1]
            print(score, ligand)
    pass
