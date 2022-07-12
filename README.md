# dlg_parser_pymol_plugin
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
