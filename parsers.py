
import os
import glob


def citation():
    print("please cite this plugin in your work")
    print("The doi is: 10.5281/zenodo.6821116")
    print("get other citation information in my github page")

def check_list(list):
    #check if a list is not empty
    if list:
        return True
    else:
        return False


def score_sort(scores):
    # sorts the scores and returns the best score
    scores.sort()
    best_conf = scores[0]
    return best_conf



def check_extension(main_folder, extension):
    #creates a list of files with that ext in folder and returns the list

    #check if main_folder is a file
    if os.path.isfile(main_folder):
        if main_folder.endswith(extension):
            return [main_folder]

    os.chdir(main_folder)
    file_list = []
    file_list = glob.glob(extension)

    #add a mainfolder path to each item in the list
    for i in range(len(file_list)):
        file_list[i] = os.path.join(main_folder, file_list[i])
    
    sub_fol = os.listdir(main_folder)
    for fol in sub_fol:
        if os.path.isdir(os.path.join(main_folder, fol)) == True:
            os.chdir(os.path.join(main_folder, fol))
            sub_list = glob.glob(extension)
            if check_list(sub_list) == True:
                for i in range(len(sub_list)):
                    sub_list[i] = os.path.join(main_folder, fol, sub_list[i])
                file_list.extend(sub_list)
                
    return file_list



def parse_dlg(main_folder):
    # this function parses the dlg files in folder and its subfolders
    dlg_list = check_extension(main_folder, "*.dlg")
    for dlg in dlg_list:
        search = "DOCKED: USER    Estimated Free Energy of Binding"
        fhandle = open(dlg, encoding='utf-8')
        lines = fhandle.readlines()
        scores = []
        for line in lines:
            if line.startswith(search):
                word = line.split()
                score = word[8]
                #list = score.split(sep = "-")
                #number = list[1]
                number = float(score)
                scores.append(number)
        best_conf = score_sort(scores)
        print(dlg, best_conf)
    citation()



def parse_vina_log(vina_log_folder):
    # this function parses the vina output log file
    log_list = check_extension(vina_log_folder, "*.txt")
    for log in log_list:
        search = "   1"
        ligand_name = "Output will be"
        vina_log_file = open(log, "r")
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


def parse_vina_pdbqt(vina_pdbqt_fol, extension = "*.pdbqt"):
    # takes all vina output pdbqt files in a folder
    os.chdir(vina_pdbqt_fol)
    pdbqt_list = check_extension(vina_pdbqt_fol, extension)
    for pdbqt in pdbqt_list:
        search = "REMARK VINA RESULT:"
        vina_pdbqt_file = open(pdbqt, "r")
        lines = vina_pdbqt_file.readlines()
        scores = []
        for line in lines:
            if line.startswith(search):
                word = line.split()
                score = word[3]
                scores.append(float(score))
        best_conf = score_sort(scores)
        print(pdbqt, best_conf)
    citation()




# run if file is main
# this file can be run independently after this point
if __name__ == "__main__":
    print("this is a module")
    citation()