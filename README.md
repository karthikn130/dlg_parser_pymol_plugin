# dlg_parser_pymol_plugin version 1.1.0
Download all the files or zip file.
Then install the plugin.
To install the plugin, goto plugin manager in pymol and click install new plugin.
Then select the __init__.py file to install the plugin.
After installation of Pymol plugin, new menu will be created in plugins menu.

This plugin is used to view the docking scores of autodock and autodock vina.
This plugin is usefull while analysing hundreds of dlg files and vina output files.
To view the docking scores enter the main docking folder location.
        main docking folder - it contain many autodock subfolders 
        dock folder         - it is the single autodock folder where dlg file is present
        dlg file            -  docking log file
when dlg file is given      - docking score of that compound will be displayed
when dock folder is given   - docking score of that compound will be displayed
when main docking folder is given - docking score of all the subfolders will be displayed

To get docking score of autodock vina give merge all output file in a single text file and give it as input in the plugin. It will show the docking score along with output ligand name.

The doi is: 10.5281/zenodo.6821116
please cite this plugin in your work
get other citation information in my github page
https://github.com/karthikn130/dlg_parser_pymol_plugin