from Modules.Rewriter import rewrite, deleteResourcesFolder
from Modules.VpkManager import packageFile, copyVpkToCustomFolder

# path to the TF2 folder
tf2Folder = "E:/SteamLibrary/steamapps/common/Team Fortress 2"

# resource folder name is static, it shouldn't change between installations unlike tf2Folder
resourceFolder = tf2Folder + "/tf/resource"

resourceFile = resourceFolder + "/tf_english.txt"

# read the content of the file
openedResourceFile = open(resourceFile)
# print(openedResourceFile.read())
openedResourceFile.close()

# will copy and rewrite the file
modFolder = rewrite(tf2Folder, resourceFile)

packageFile(tf2Folder + "/tf/custom/weirdClassesNames.vpk", modFolder)

deleteResourcesFolder()
