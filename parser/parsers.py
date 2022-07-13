
import os
import re
import glob
import openbabel as obabel
import openbabel.pybel as babel
import pandas as pd

def citation():
    print("please cite this plugin in your work")
    print("The doi is: 10.5281/zenodo.6821116")
    print("get other citation information in my github page")

def parse_it(main_folder):
    #creates a list of dlg files in folder and passes the list to score funtion.
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
    citation()
    

def score(dlg_file):
    # parses the autodock dlg file
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
    # this function parses the vina output log file
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
    citation()

def parse_vina_pdbqt(vina_pdbqt_fol):
    # takes all vina output pdbqt files in a folder
    os.chdir(vina_pdbqt_fol)
    files = []
    names = []
    scores = []
    mass = []
    formula = []
    smiles = []
    model = []
    for file in glob.glob("*.pdbqt"):
        with open(file, 'rt') as pdbqt_file:
            for line in pdbqt_file:
                line = line.strip()
                if "VINA RESULT" in line:
                    neg = re.search(r'-\d.\d', line)
                    neg_2 = re.search(r'-\d\d.\d', line)
                    if neg:
                        files.append(pdbqt_file.name)
                        scores.append(float(neg.group()))

                    elif neg_2:
                        files.append(pdbqt_file.name)
                        scores.append(float(neg_2.group()))

                    if not (neg or neg_2):
                        files.append(pdbqt_file.name)
                        scores.append(
                            'positive value, sorry I can´t keep it (yet)')

        for mol in babel.readfile("pdbqt", file):
            names.append(mol.title)
            mass.append(mol.molwt)
            formula.append(mol.formula)
            model.append(mol.data['MODEL'])
            smiles.append(mol)

    d = {'file': pd.Series(files),
        'score': pd.Series(scores),
        'model': pd.Series(model),
        'compound name': pd.Series(names),
        'molecular formula': pd.Series(formula),
        'molecular weight': pd.Series(mass),
        'smiles': pd.Series(smiles)}
    table = pd.DataFrame(d)
    table

# get scores from vina out pdbqt under development
def scores(vina_pdbqt_fol):
            os.chdir (vina_pdbqt_fol) #Path where *.pdbqt output files are located
            files=[]
            scores=[]
            for file in glob.glob('*.pdbqt'):
                with open(file,'rt') as file:
                    for line in file:
                        line = line.strip()
                        if "VINA RESULT" in line:
                            neg = re.search(r'-\d.\d', line)
                            if neg:
                                files.append (file.name)
                                scores.append (neg.group())
            d={'file':pd.Series(files),'score':pd.Series(scores)}
            print ('Raw score values')
            table=pd.DataFrame (d)
            print (table)
            print ('Sorted score values')
            sort=table.sort_values ('score',ascending=False)
            print (sort)
            table.to_csv ('no_sorted_scores.csv')
            sort.to_csv ('sorted_scores.csv')