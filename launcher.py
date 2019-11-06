# Created by Abrahan Nevarez on August 24th 2019
# Created for the use of the base game Toontown Stride
# Can be modified for other servers

import os
import subprocess
from sys import platform
from PySide2 import QtWidgets, QtCore, QtGui
import shutil
from pathlib import Path
from ui import main, CPL, options_menu
import json

class Options_Menu(options_menu.Ui_Options_Menu, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Options_Menu, self).__init__(parent)
        self.setupUi(self)
        # Sets up what will be run whenever we load the page
        self.contentPackExplorer()
        self.resource_Button.clicked.connect(self.openResourceFolder)
        self.run = main_window()

        # Loads in our keys and game settings json data
        self.hotKeySelector()
        self.optionsJSON()

        # By default, shows an empty option so user can select the option that they want
        self.gameModes.setCurrentIndex(-1)

        # Handles sava button data
        self.saveChangesButton.clicked.connect(self.optionsJSON)

        # Login data combobox
        self.gameModes.currentTextChanged.connect(self.loginSettings)

        

    # Opens up the content pack folder
    def openResourceFolder(self):
        if(os.getcwd() == "content_packs"):
            print("In this directory, no need to change")
        else:
            print("Not in the directory, switching now...")
            print(os.getcwd())
            os.chdir("content_packs")
            print(os.getcwd())

        if platform == "win32":
            subprocess.Popen(r'explorer /select, ' + os.getcwd(), shell = True)
    
    # Reads JSON data and dumps it
    def optionsJSON(self):
        # Reads the info for the sliders
        with open('settings/game_settings.json', 'r') as loop:
            data = json.load(loop)

        # Modifies the content of the sliders and other settings from comboboxes
        with open('settings/game_settings.json', 'w') as update:
            data["Graphical Settings"]["Show FPS"] = self.fpsSlider.value()
            data["Graphical Settings"]["V-Sync"] = self.vSyncSlider.value()
            data["Graphical Settings"]["Animation Blending"] = self.animationSlider.value()
            data["Graphical Settings"]["GUI Animation"] = self.guiSlider.value()
            data["Graphical Settings"]["Particle effects"] = self.particleSlider.value()
            data["Graphical Settings"]["Disable Accesories"] = self.disableAccessoriesSlider.value()
            data["Graphical Settings"]["Discord Integration"] = self.discordIntergration.value()
            data["Login Settings"]["IP Address"] = self.ipAddress.text()
            data["Login Settings"]["Index"] = self.gameModes.currentIndex()
            json.dump(data, update, indent = 1)
        
    # Loads up the defined hot keys located in settings/controls.json
    def hotKeySelector(self):
        with open('settings/controls.json') as loop:
            data = json.load(loop)

        # Sets the controls from the controls json file
        self.walkUpButton.setText(data["Controls"]['walk-up'])
        self.walkLeftButton.setText(data["Controls"]['walk-left'])
        self.walkRightButton.setText(data["Controls"]['walk-right'])
        self.walkDownButton.setText(data["Controls"]['walk-down'])

        self.jumpButton.setText(data["Controls"]['jump'])

        self.takeScreenButton.setText(data["Controls"]['screenshot'])

        self.walkButton.setText(data["Controls"]['walk'])

        self.lookUpButton.setText(data["Controls"]['look-up'])
        self.lookDownButton.setText(data["Controls"]['look-down'])

        self.viewGagsButtons.setText(data["Controls"]['showGags'])

        self.viewToontasksButton.setText(data["Controls"]['showTasks'])

        self.openBookButton.setText(data["Controls"]['stickerBook'])

        self.showAndHideButton.setText(data["Controls"]['toggleGUI'])

        self.viewMapButton.setText(data["Controls"]['showMap'])

        self.openFriendsButton.setText(data["Controls"]['friendsList'])

        self.changeCameraButton.setText(data["Controls"]['cameraNext'])

        self.PreviousCameraButton.setText(data["Controls"]['cameraPrev'])

        self.performActionButton.setText(data["Controls"]['performAction'])

        self.debugScreenButton.setText(data["Controls"]['debugScreenShots'])

        self.displayDebugButton.setText(data["Controls"]['debugInfo'])

        self.cogHQButton.setText(data["Controls"]['cogInfo'])

        self.exitActivityButton.setText(data["Controls"]['exitActivity'])

    def loginSettings(self, index):
        # Modifies the content of the sliders
        
            if index == "Local":
                print("Local")
                self.gameModes.setCurrentIndex(0)
                self.ipAddress.setText("127.0.0.1")
                self.ipAddress.setReadOnly(True)
                 
                # Checks if platform is linux or windows
                if platform == "linux" or platform == "linux2":
                    self.playGame.clicked.connect(self.linux_local_host)
                if platform == "win32":
                    print("I sent a localhost to the main button!")
                    self.playGame.clicked.connect(self.win32_local_host)
                
            elif index == "Server":
                print("Server")
                self.gameModes.setCurrentIndex(1)
                self.ipAddress.setText("")
                self.ipAddress.setReadOnly(False)
                if platform == "linux" or platform == "linux2":
                    self.playGame.clicked.connect(self.linux_server_host)
                if platform == "win32":
                    print("I sent a server to the main button!")
                    self.playGame.clicked.connect(self.server_host)
                
            else:
                print("Uh oh, user tried to run without an option...")
    
    # Loads up the content pack folder and lets the user select the content pack
    # Uses a treeview to show the actual contents of the folder itself
    def contentPackExplorer(self):
        path ="content_packs"
        display = QtWidgets.QFileSystemModel()

        display.setRootPath((QtCore.QDir.rootPath()))

        self.treeView.setModel(display)
        self.treeView.setRootIndex(display.index(path))
        self.treeView.setSortingEnabled(True)

    # Opens the contents of the zip file and looks for mf file
    # replaces the contents of the resource folder with the resources provided with the .mf
    # Will be replaced with a tree node based system
    def content_pack_opener(self):
        print(os.getcwd())
        file, filename = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open mf"), self.tr("content_packs"), self.tr("MF files (*.mf)"))
        
        # Allows us to break the path into multiple segments
        p = Path(file)
        Dir_Content_Packs= "./content_packs"
        Dir_Resources = "./resources"

        # Decompresses the .mf files
        print("Now unzipping .mf file...please hold")
        content_pack_unzip = subprocess.Popen("multify.exe -x -f " + p.name, shell=False)
        
        # Waits till process is done
        content_pack_unzip.wait()

        print("Okay, I'm done unzipping all the files:")
        print("Now moving files to resources!")
        # Search through all folders and files
        os.chdir("../")
        for root, folders, files in os.walk(Dir_Content_Packs):

            # Look at each file
            for contentFile in files:

                # Save the path to the file from the ./content_packs/ folder
                contentRoot = root

                # Replace the ./content_packs/ path with the ./resources/ path
                resourceRoot = root.replace(Dir_Content_Packs, Dir_Resources)
                resourceFilePath = os.path.join(resourceRoot, contentFile)

                # Check whether the directory ./resources/ has that file
                if os.path.exists(resourceFilePath):

                # If so, replace the file inside ./resources/ with the one from ./content_packs/
                    contentFilePath  = os.path.join(contentRoot, contentFile)
                    shutil.copyfile(contentFilePath, resourceFilePath)
                
        print(os.getcwd())
        os.chdir("../")
        print("Success! Now launch the game with your new files")
     # Code to log onto a server that has already been started
    # Added support for JSON loading data
    def server_host(self):
        PPython, randomtext = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open ppython file"), self.tr("C:"), self.tr("PPython (*.exe)"))
        with open('settings/game_settings.json', 'r') as loop:
        # Grabs the server text and IP to pass into panda
            with open('settings/game_settings.json') as loop:
                data = json.load(loop)

            Username = data["Login Settings"]["Username"]
            IP_Address = data["Login Settings"]["IP Address"]

            # Sets up enviroment variables needed to launch the game
            os.environ['input'] = '1'
            os.environ['TTS_GAMESERVER'] = IP_Address
            os.environ['TTS_PLAYCOOKIE'] = Username
            with open('settings/game_settings.json', 'w') as update:
                # Get rid of username and IP address after starting
                data["Login Settings"]["Username"] = ""
                data["Login Settings"]["IP Address"] = ""
                json.dump(data, update, indent = 1)
                subprocess.Popen(PPython + " -m toontown.toonbase.ToontownStart", shell=False)
            self.close()

    def linux_server_host(self):
        os.chdir("../")
        # Reads our JSON file
        with open('settings/game_settings.json', 'r') as loop:
            data = json.load(loop)
            # Grabs the server text and IP to pass into panda

            Username = data["Login Settings"]["Username"]
            IP_Address = data["Login Settings"]["IP Address"]

            # Sets up enviroment variables needed to launch the game
            os.environ['input'] = '1'
            os.environ['TTS_GAMESERVER'] = IP_Address
            os.environ['TTS_PLAYCOOKIE'] = Username
            with open('settings/game_settings.json', 'w') as update:
                # Get rid of username and IP address after starting
                data["Login Settings"]["Username"] = ""
                data["Login Settings"]["IP Address"] = ""
                json.dump(data, update, indent = 1)
            subprocess.Popen("ppython -m toontown.toonbase.ToontownStart", shell=False)
            self.close()

    # Code to start local on linux
    def linux_local_host(self):
        os.chdir("../")

        os.environ['DYLD_LIBRARY_PATH'] = '`pwd`/Libraries.bundle'
        os.environ['DYLD_FRAMEWORK_PATH'] = "Frameworks"

        # Reads JSON file
        with open('settings/game_settings.json', 'r') as loop:
            data = json.load(loop)

        # Grabs data from JSON file and passes it into username variable for loading
        Username = data["Login Settings"]["Username"]

        if not Username:
            QtWidgets.QMessageBox.about(self, "Name required", "Hey! \nYou need a username before we can start!\n")
            return
        os.environ['ttsUsername'] = Username
        os.environ['TTS_PLAYCOOKIE'] = Username

        os.environ['TTS_GAMESERVER'] = "127.0.0.1"
        with open('settings/game_settings.json', 'w') as update:
                # Get rid of username and IP address after starting
                data["Login Settings"]["Username"] = ""
                data["Login Settings"]["IP Address"] = ""
                json.dump(data, update, indent = 1)
        subprocess.Popen("ppython -m toontown.toonbase.ToontownStart")
        self.close()

    # Code to start local host on windows!
    def win32_local_host(self):
        PPython, randomtext = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open ppython file"), self.tr("C:\\"), self.tr("PPython (*.exe)"))
        if not open(PPython):
            print("Uh oh! stop this now!")
        with open('settings/game_settings.json') as loop:
            data = json.load(loop)

        Username = data["Login Settings"]["Username"]

        backendir = os.chdir("dev/backend/")
        # Check to prevent a blank user
        if not Username:
            QtWidgets.QMessageBox.about(self, "Name required", "Hey! \nYou need a username before we can start!\n")
            return

        SW_HIDE = 0
        Info = subprocess.STARTUPINFO()

        Info.dwFlags = subprocess.STARTF_USESHOWWINDOW
        Info.wShowWindow = SW_HIDE

        subprocess.Popen(r"start-astron-cluster.bat", startupinfo=Info)
        subprocess.Popen(r"start-ai-server.bat", startupinfo=Info)
        subprocess.Popen(r"start-uberdog-server.bat", startupinfo=Info)

        ReturnDir = os.chdir("../../")

        os.environ['input'] = '1'

        os.environ['TTS_GAMESERVER'] = "127.0.0.1"

        os.environ['TTS_PLAYCOOKIE'] = Username
        with open('settings/game_settings.json', 'w') as update:
                # Get rid of username and IP address after starting
                data["Login Settings"]["Username"] = ""
                data["Login Settings"]["IP Address"] = ""
                json.dump(data, update, indent = 1)
        subprocess.Popen(PPython + " -m toontown.toonbase.ToontownStart", shell=False)
        self.close()

    def returnMainMenu(self):
        self.hide()
        main_menu = main_window()
        with open('settings/game_settings.json', 'r') as loop:
            data = json.load(loop)
        self.run.name.text = data["Login Settings"]["Username"]
        main_menu.show()
        main_menu.exec_()
        main_menu.setWindowModality(QtCore.Qt.WindowModal)
# Initates the basic UI elements
class main_window(main.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)
        
        # Username check to make sure there exist one.
        if not self.name.text:
            QtWidgets.QMessageBox.about(self, "IP address", "Hey! \nYou need a name in order to launch the game\n")

    
        self.options_menu.clicked.connect(self.optionsMenu)
        print("Directory is currently: " + os.getcwd())
       
    # Opens the content pack window
    def optionsMenu(self):
        # Loads JSON data each time we venture into the options menu, makes it easy to store data
        with open('settings/game_settings.json', 'r') as loop:
            data = json.load(loop)

        with open('settings/game_settings.json', 'w') as loop:
            data["Login Settings"]["Username"]  = self.name.text()
            json.dump(data, loop, indent = 1)
        print("Username is:" + data["Login Settings"]["Username"])
        self.name.text = data["Login Settings"]["Username"]
        self.hide()
        om = Options_Menu()
        om.show()
        om.exec_()
        om.setWindowModality(QtCore.Qt.WindowModal)

   


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = main_window()
    qt_app.show()
    app.exec_()
