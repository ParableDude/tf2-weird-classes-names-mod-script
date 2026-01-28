import vpk

def packageFile(vpkName, modFolder):
    vpkFile = vpk.new(modFolder)
    vpkFile.save(vpkName)


def copyVpkToCustomFolder(vpkFile, tf2Folder):
    customFolder = tf2Folder + "/tf/custom"
    shutil.copyfile(vpkFile, customFolder + "/WeirdClassesNames.vpk")
    print("copied vpk into the custom folder")
