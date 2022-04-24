import os
import shutil
usr = os.getlogin()

inputtxt = input("For File Press 1, For Folder Press 2 :- ")

if inputtxt == "1":
    source = input("Enter Source File Path (With Forward Slash eg:- C:/Users/usrname/Desktop/filename.extension) :- ")
    destination = "C:/Users/"+usr+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    destination = destination + "/"
    shutil.copy(source, destination)

if inputtxt == "2":
    source = input("Enter Source Folder Path (With Forward Slash eg:- C:/Users/usrname/Desktop/filename.extension) :- ")
    source = source + "/"
    destination = "C:/Users/"+usr+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    destination = destination + "/"
    listoffiles = os.listdir(source)
    for file in listoffiles :
        shutil.copy((source + file), destination)