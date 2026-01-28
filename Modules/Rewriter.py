import shutil
import os

tf2Folder = ""
tmpFileName = "/tmpFile.txt"
dataFolder = "resources"
modFolder = dataFolder + "/mod"

textValues = {
    "Scout": "Speedy Motherf#cker",
    "Soldier": "American Boot",
    "Pyro": "Mmmmmphh",
    "Demoman": "Drunk Scottish Cyclop",
    "Heavy": "Sandvich Mann",
    "Engineer": "Engineer Gaming",
    "Medic": "MeeM",
    "Sniper": "XxxprosniperlonewolfxxX",
    "Spy": "Baguette Onii-chan",
    "SCOUT": "SPEEDY MOTHERF#CKE",
    "SOLDIER": "AMERICAN BOOT",
    "PYRO": "MMMMMPHH",
    "DEMOMAN": "DRUNK SCOTTISH CYCLOP",
    "HEAVY": "SANDVICH MANN",
    "ENGINEER": "ENGINEER GAMING",
    "MEDIC": "MEEM",
    "SNIPER": "XXXPROSNIPERLONEWOLFXXX",
    "SPY": "BAGUETTE ONII-CHAN",
}


def rewrite(TF2Folder, resourceFile):
    global tf2Folder
    tf2Folder = TF2Folder

    copyFileToDataAsTmp(resourceFile)
    file = createFiles()
    return file


def ensureFolderExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def copyFileToDataAsTmp(file):
    ensureFolderExists(dataFolder)
    shutil.copyfile(file, dataFolder + tmpFileName)
    print("copied file into the resources folder")


# copy a file to the resources folder's mod folder
def copyFileToModFolder(file):
    ensureFolderExists(modFolder + "/resource")
    shutil.copyfile(file, modFolder + "/resource/tf_english.txt")
    print("copied file into the resource mod folder")
    return modFolder + "/resource/tf_english.txt"


def createFiles():
    previousFile = dataFolder + tmpFileName
    cl = 0
    for i in textValues:

        # creates a temporary file to write for each classes
        currentFile = dataFolder + "/tmp" + i + ".txt"

        findAndWrite(currentFile, previousFile, i, textValues[i])
        # shutil.copyfile(previousFile, currentFile)

        # delete old file
        if os.path.exists(previousFile):
            os.remove(previousFile)

        previousFile = currentFile
        cl += 1

    modFile = copyFileToModFolder(previousFile)

    if os.path.exists(previousFile):
        os.remove(previousFile)

    return modFolder


def findAndWrite(writingFile, readingFile, oldText, newText):

    newFile = open(writingFile, "w", encoding="utf-16-le")
    oldFile = open(readingFile, encoding="utf-16-le")
    for line in oldFile:

        # the lines we update have this format :
        # "VARIABLE_NAME"       "Text value"
        # We only want to change Text value (changing VARIABLE_NAME would break the game)
        newLine = ""
        lineParts = line.split('"')

        for i in range(len(lineParts)):
            part = lineParts[i]
            if i > 1 and part.strip() != "":
                part = part.replace(oldText, newText)
            if i == 0:
                newLine = part
            else:
                newLine = newLine + '"' + part

        newFile.write(newLine)

    newFile.close()
    oldFile.close()

def deleteResourcesFolder():
    if os.path.exists(dataFolder):
        shutil.rmtree(dataFolder)