import os
import shutil

path = input("enter name of the folder which u want to organise :")
list_of_files =  os.listdir(path)

#Going through each & every file
for i in list_of_files:
    name ,ext =os.path.splitext(i)

    #To store all the extension types
    #: - selects all
    ext = ext[1:]

    #To check if extension is empty - folder
    if ext=="" :
        continue
    if os.path.exists(path + "/" + ext) :
        #source = downloads/abc.pdf
        #destination = downloads/pdf/abc.pdf
        shutil.move(path + "/" + i,path + "/" + ext + "/" +i)
    else :
        os.makedirs(path+"/"+ext)
        shutil.move(path + "/" + i,path + "/" + ext + "/" +i)