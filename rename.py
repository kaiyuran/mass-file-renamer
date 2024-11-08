#simple program to rename files in a folder
import os
import time
start = time.time()

#change these values
path = ""
prefix = ""
startNum = 0
fileType = "" #ex. ".jpg"

imagesNames = os.listdir(path)
try:
    for num, image in enumerate(imagesNames):
        os.rename(path+"/"+image, path+"/"+prefix+str(num+startNum)+fileType)
except FileExistsError:
    print("File already exists, renaming to temporary name then renaming to desired name")
    #rename to arbitrary value
    for num, image in enumerate(imagesNames):
        os.rename(path+"/"+image, path+"/"+"TEMPOARY"+str(num)+fileType) #if your files are named "TEMPOARY" then change this

    #rename to proper name
    newImagesNames = os.listdir(path)
    for num, image in enumerate(newImagesNames):
        os.rename(path+"/"+image, path+"/"+prefix+str(num+startNum)+fileType)

print(f"Total Time taken: {time.time()-start}")