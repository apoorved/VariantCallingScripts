Tkinter Variant calling GUI
--Prerequisite:Linux OS(tested on Ubuntu) and  CONDA (package and environment management system).
--Activate the given conda environment(viral.yml)
--run the GUI with command "python tkinterGUItest1.py"
--Select files and start the analysis.
--Track the progress and press "OK" options to move ahead 
SUMMARY WORKFLOW
-Import modules like tkinter for GUI, subprocess for running linux commands and pathlib for filenames
-Setup initial diretcory for analysis to work
-Setting up main app frame using Tkinter 
-Make files Dialog boxes and buttons to select the paired end reads and genome file 
-variant call Function to start the analysis 
-button to call the variant call function and start the analysis

output Files will be stored in var variable in the home/user directory