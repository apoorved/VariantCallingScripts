Tkinter Variant calling GUI
--Prerequisite:CONDA (package and environment management system).
Procedure:
--Run analysis.sh(bash analysis.sh) to activate GUI.
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

SETUP FOR WINDOWS:
For computer running Windows 10 or 11:

1) Open control panel,go to "Programs",
 2)click " Turn Windows feature on or off",
3)Tick the option  "Windows Subsystem for Linux"
4)"Let the system restart"
5)"Download any linux distribution app like Ubuntu 18.04 /Ubuntu 20.04/Kali Linux etc from Microsoft store
6)" Open the specific app"
7)"Make your username and password for linux distribution
8)" Install miniconda"  for the Linux distribution
