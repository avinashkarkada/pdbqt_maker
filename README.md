# pdbqt_maker
This repo contains script for converting all the files in the folder of the formats sdf, pdb and mol2 to pdbqt



HOW TO USE:
========================================================================================
1. Paste the script in the folder with all the ligands that need to be converted
2. Run the script and select the format of your input files
3. Note that you need to have installed open babel
4. Click on run
5. Now you will have your output files in the folder

Note that you can easily change the script to include more file formats.



HOW TO INSTALL openbabel:

If you are facing an error while installing openbabel:

1. Open cmd and run "pip install openbabel"  -> error?
2. Then if you have openbabel gui already installed, open cmd in the installed folder and run "pip install -U openbabel" -> still no luck?......hmmm

3. Then, open the link: https://www.lfd.uci.edu/~gohlke/pythonlibs/
4. Search for openbabel for your python version. eg: cp39 represents python 3.9
5. After downloading the wheel file, redirect to the file directory, open cmd and run 'pip install "downloaded filename"'




Hope it helps :)
