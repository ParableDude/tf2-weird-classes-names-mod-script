from .Rewriter import rewrite, deleteResourcesFolder
from .VpkManager import packageFile, copyVpkToCustomFolder

tf2Folder = "D:/SteamLibrary/steamapps/common/Team Fortress 2"
resourceFolder = tf2Folder + "/tf/resource"

languages = []

def getTf2Folder():
    return tf2Folder

def setTf2Folder(newFolder):
    global tf2Folder
    tf2Folder = newFolder

    global resourceFolder
    resourceFolder = tf2Folder + "/tf/resource"

def getResourceFolder():
    return resourceFolder

def getLanguages():
    return languages

def setLanguages(newLanguages):
    global languages
    languages = newLanguages

def generate():
    # resource folder name is static, it shouldn't change between installations unlike tf2Folder
    
    resourceFile = getResourceFolder() + "/tf_english.txt"

    # read the content of the file
    openedResourceFile = open(resourceFile)
    # print(openedResourceFile.read())
    openedResourceFile.close()

    # will copy and rewrite the file
    modFolder = rewrite(tf2Folder, resourceFile)

    packageFile(tf2Folder + "/tf/custom/weirdClassesNames.vpk", modFolder)

    deleteResourcesFolder()
