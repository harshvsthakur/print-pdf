# search for file in folder and print file with matching name

import glob, os, tempfile, win32api, win32print
import pyinputplus as pyip

path = '' # fill in the folder path

print("Enter 5 digit PO Number to print")
POnumber = pyip.inputInt(greaterThan=10000, lessThan=99999) 

os.chdir(path)
for file in glob.glob(str(POnumber)+"*.pdf"):
    filepath = os.getcwd()+"\\"+file
    open(filepath)
    win32api.ShellExecute (
        0,
        "print",
        filepath,
        '/d:"%s"' % win32print.GetDefaultPrinter (),
        ".",
        0
        )
