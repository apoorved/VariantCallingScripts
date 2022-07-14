#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:30:41 2021

@author: apoorv
"""

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
import subprocess as sub
import os
import time
from pathlib import Path
from Bio import SeqIO
fq1 = ""
fq2 = ""
genome = ""


#SET THE DIRECTORY
home = os.path.expanduser('~')
os.chdir(home)
dire = "var"
dirpath = os.path.join(home,dire)
try:
    os.mkdir(dirpath)
    print("folder var created")
except FileExistsError:
    print("folder var already there")

os.chdir(dirpath)

def check_fastq(file):
    with open(file,"r") as f:
        print(file)
        fq = SeqIO.parse(f, "fastq")
        
        try : return any(fq)
        
        except Exception as e:
            print(e)
            return False

def check_fasta(fil):
    with open(fil,"r") as fi:
        print(fil)
        fa = SeqIO.parse(fi,"fasta")
        
        try : return any(fa)
        
        except Exception as ex:
            print(ex)
            return False         
        
#FRAME FOR 
sel = tk.Tk()
sel.geometry("1980x1080")
sel.title("Variant Calling")
sel.configure(background='white')

progress = Progressbar(sel, orient = HORIZONTAL,
              length = 500, mode = 'determinate')

#FILESDIALOG BOX
def selectfile1():      
    filetypes = (('fastq files', '*.fastq'),('fq', '*.fq'))
    file1_path = filedialog.askopenfilename(title='Select SINGLE end or FORWARD read for PAIRED end', initialdir='/home', filetypes=filetypes)
    global fq1
    if (check_fastq(file1_path) == True):
        fq1 = file1_path
        messagebox.showinfo(title='Selected file',message=file1_path)
    else:
        a ="error in file, select again"
        messagebox.showerror(title='Selected file',message=a)
        
#button to select file   
file_1 = Button(sel,text="Select SINGLE end or FORWARD read for PAIRED end",command = selectfile1)
file_1.pack(pady=60)
 
def selectfile2():
    filetypes = (('fastq files', '*.fastq'),('fq', '*.fq'))   
    file2_path = filedialog.askopenfilename(parent=sel, title='Select REVERSE read for PAIRED end', initialdir='/home', filetypes=filetypes)
    global fq2
    if (check_fastq(file2_path) == True ):
        fq2 = file2_path
        messagebox.showinfo(title='Selected file',message=file2_path)
    else:
        b = "error in file,select again"
        messagebox.showerror(title= 'selected file',message=b)
        

file_2 = Button(sel,text="Select REVERSE read for PAIRED end",command = selectfile2)
file_2.pack(pady=90) 
 

def selectfile3():
    file3_path = filedialog.askopenfilename(parent=sel, title='Select GENOME file', initialdir='/home')
    global genome
    if (check_fasta(file3_path) == True):
        genome=file3_path
        messagebox.showinfo(title='Selected file',message=file3_path)
    else:
        c = "error in file, select again"
        messagebox.showerror(title= 'selected file',message=c)
        
    
file_3 = Button(sel,text="Select GENOME file",command = selectfile3)
file_3.pack(pady=120)     

#Variant calling function 
def analysis(x=None,y=None,z=None):
  
    if all(v == "" for v in [x,z]):
        print("values missing select files again")
        return
    
    
    
    base=Path(z).stem
    basename=Path(x).stem
    unsorted=basename + ".sam"
    sortbam=basename + ".bam"
    rawbcf=basename + '_raw' + '.bcf'
    variant=basename + '_variants' + '.vcf'
    final=basename + '_final_variants' + '.vcf'
    
    
    indexcmd=['bowtie2-build', '-f', z, base]
    sub.run(indexcmd)
    messagebox.showinfo(title='INFO',message="GENOME INDEXED")
    progress['value'] = 20
    sel.update_idletasks()
    time.sleep(1)
    
    
    if  y == "":
              print("Single end reads analysis")  
              alncmd=['bowtie2', '-q', '-x', base,  x, '-S', unsorted]
              sub.run(alncmd)
              messagebox.showinfo(title='INFO',message="Alignment done")
              progress['value'] = 40
              sel.update_idletasks()
              time.sleep(1)
          
    else:
             print("Paired end read analysis")
             alncmd=['bowtie2', '-q', '-x', base, '-1', x, '-2', y , '-S', unsorted]
             sub.run(alncmd)
             messagebox.showinfo(title='INFO',message="Alignmnet done")
             progress['value'] = 40
             sel.update_idletasks()
             time.sleep(1)
          
    
    sortcmd=['samtools', 'sort', '-o', sortbam, unsorted]
    sub.run(sortcmd)
    progress['value'] = 60
    sel.update_idletasks()
    time.sleep(1)
          

    mpileupcmd=['bcftools', 'mpileup', '-O', 'b', '-o', rawbcf, '-f', z ,sortbam  ]
    sub.run(mpileupcmd)
    messagebox.showinfo(title='INFO',message="Calling Variants")
    progress['value'] = 80
    sel.update_idletasks()
    time.sleep(1)
          
    
    bcfcallcmd=['bcftools', 'call', '--ploidy', '1', '-v', '-m', '-o', variant, rawbcf]
    sub.run(bcfcallcmd)
    
    with open(final,'wb') as i:
        vcfutils=sub.Popen(['vcfutils.pl', 'varFilter', variant],stdout=i)
    messagebox.showinfo(title='INFO',message="Files saved in var directory")
    progress['value'] = 100
    exit()
          
  
         
#NEXT BUTTON STARTS ANALYSIS   
progress.pack(pady = 20)
Button = tk.Button(sel,text="Variant Calling",font=("Arial",20), command=lambda: analysis(fq1,fq2,genome))
Button.place(x=230,y=950)
Button.pack(pady=150)

exit_button = tk.Button(sel, text="EXIT",font=("Arial",16),background = "red",fg = "white", command=sel.destroy)
exit_button.pack(side = RIGHT)
sel.mainloop()
