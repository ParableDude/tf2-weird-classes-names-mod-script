from . import UIModel, UIView
from customtkinter import filedialog
from pathlib import Path
import os
import re

def generate() :
    UIModel.generate()
    UIView.showSuccess()

def selectTf2Folder():
    tmpFolder = filedialog.askdirectory()

    tf2ExeFile = tmpFolder+"/tf.exe"
    if not os.path.exists(tf2ExeFile):
        UIView.showFolderError("The file \"tf.exe\" was not found in this folder")
    else :
        UIModel.setTf2Folder(tmpFolder)
        UIView.updateFolderEntry()
        updateAvailableLanguages()

def updateAvailableLanguages():
    resourceFolder = Path(UIModel.getResourceFolder())
    languages = []

    pattern_regex = re.compile(r"^tf_[^_]+\.txt$")

    for file in resourceFolder.iterdir():
        if file.is_file() and pattern_regex.match(file.name):
            languages.append(file.name.replace("tf_", "").replace(".txt", ""))

    UIModel.setLanguages(languages)

def selectTf2Folder():
    tmpFolder = filedialog.askdirectory()

    tf2ExeFile = tmpFolder+"/tf.exe"
    if not os.path.exists(tf2ExeFile):
        UIView.showFolderError("The file \"tf.exe\" was not found in this folder")
    else :
        UIModel.setTf2Folder(tmpFolder)
        UIView.updateFolderEntry()
