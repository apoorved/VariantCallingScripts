Tkinter Variant calling GUI
--Prerequisite:CONDA (package and environment management system).
Procedure:
--Run analysis.sh(bash analysis.sh) to install conda and activate GUI.
--Select files and start the analysis.
--Track the progress and press "OK" options to move ahead
--Var folder is made in root folder(cd $HOME) which contains analysed files. ($HOME) folder) 
SUMMARY WORKFLOW
-Import modules like tkinter for GUI, subprocess for running linux commands and pathlib for filenames
-Setup initial diretcory for analysis to work
-Setting up main app frame using Tkinter 
-Make files Dialog boxes and buttons to select the paired end reads and genome file 
-variant call Function to start the analysis 
-button to call the variant call function and start the analysis

