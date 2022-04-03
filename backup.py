import os
import shutil #standard utilities

source = input("Enter the path of the folder to be copied: ")
destination = input("Enter the destination folder: ")

#String concatenation - joining anything with a string - end to end
#"Neel" + 10 = Neel10
source = source + "/"
destination = destination +'/'

list_of_files = os.listdir(source)
for i in list_of_files:
    shutil.copy((source + i), destination)
    