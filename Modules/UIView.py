import customtkinter
import tkinter
from PIL import Image
from . import UIController, UIModel

class WeirdApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("weird names app")
        self.geometry("600x300")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(0, weight=5)

        self.label = customtkinter.CTkLabel(
            self,
            text="Text will go there",
        )
        self.label.grid(row=0, column=0)

        createFolderLayout(self, 1)

        # createLanguageLayout(self, 2)

        self.button = customtkinter.CTkButton(
            self, text="Generate", command=UIController.generate
        )
        self.button.grid(row=3, column=0, padx=20, pady=20)

app = None

def createFolderLayout(app, frameRow):
    app.folderFrame = customtkinter.CTkFrame(app, fg_color="transparent")
    app.folderFrame.grid(row=frameRow, column=0, padx=20, pady=20)

    app.folderLabel = customtkinter.CTkLabel(
        app.folderFrame,
        text="Select base TF2 folder (eg: D:/SteamLibrary/steamapps/common/Team Fortress 2)",
    )
    app.folderLabel.grid(row=0, column=0, columnspan=2)

    app.folderEntry = customtkinter.CTkEntry(
        app.folderFrame,
        width=300,
        placeholder_text="TF2 folder",
        textvariable=tkinter.StringVar(app.folderFrame, UIModel.getTf2Folder())
    )
    app.folderEntry.grid(row=1, column=0, sticky="e")

    folderEditIcon = customtkinter.CTkImage(
        light_image=Image.open("./Resources/icons/folder-edit-dark.png"),
        dark_image=Image.open("./Resources/icons/folder-edit-light.png"),
        size=(20, 20),
    )
    app.folderBtn = customtkinter.CTkButton(
        app.folderFrame,
        text="",
        command=UIController.selectTf2Folder,
        image=folderEditIcon,
        width=20,
        height=30,
        fg_color="transparent",
    )
    app.folderBtn.grid(row=1, column=1, padx=10, sticky="w")

def createLanguageLayout(app, frameRow):
    UIController.updateAvailableLanguages()

    app.languageFrame = customtkinter.CTkFrame(app, fg_color="transparent")
    app.languageFrame.grid(row=frameRow, column=0, padx=20, pady=20)

    app.languageLabel = customtkinter.CTkLabel(
        app.languageFrame,
        text="Select base TF2 folder (eg: D:/SteamLibrary/steamapps/common/Team Fortress 2)",
    )
    app.languageLabel.grid(row=0, column=0)

    app.languageOptions = customtkinter.CTkOptionMenu(app.languageFrame, values=UIModel.getLanguages())
    app.languageOptions.grid(row=1, column=0)


def displayWindow():
    # load the coconut to ensure UI optimisation
    Image.open("./Resources/pictures/coconut.png")

    # launch UI
    global app
    app = WeirdApp()
    app.mainloop()

def updateLanguages():
    if app != None:
        app.languageOptions.values = UIModel.getLanguages()

def updateFolderEntry():
    if app != None:
        app.folderEntry.delete(0, len(app.folderEntry.get()))
        app.folderEntry.insert(0, UIModel.getTf2Folder())

def showFolderError(error):
    if app != None:
        app.folderError = customtkinter.CTkLabel(app.folderFrame) # TODO

def showSuccess():
    if app != None:
        app.successLabel = customtkinter.CTkLabel(
            app,
            text="Mod succesfully installed",
        )
        app.successLabel.grid(row=4, column=0)
