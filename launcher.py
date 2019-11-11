# Created by Abrahan Nevarez
# Created for the use of the base game Toontown Stride
# Can be modified for other servers

import os
import subprocess
from sys import platform
from PySide2 import QtWidgets, QtCore, QtGui
import shutil
from pathlib import Path
from ui import mainWindow, optionsMenu
import json

class optionsMenu(optionsMenu.Ui_Options_Menu, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(optionsMenu, self).__init__(parent)
        self.setupUi(self)
        # Sets up what will be run whenever we load the page
        # Loads up the content pack tree node
        self.contentPackExplorer()

        # Loads in our keys and game settings json data
        self.hotKeySelector()
        self.optionsJSON()

        # By default, shows an empty option so user can select the option that they want
        self.gameModes.setCurrentIndex(-1)

        # Handles sava button data
        self.saveChangesButton.clicked.connect(self.optionsJSON)

        # Login data combobox
        self.gameModes.currentTextChanged.connect(self.loginSettings)
        self.treeView.doubleClicked.connect(self.contentPackOpener)
    
    # Reads JSON data and dumps it
    def optionsJSON(self):
        # Reads the info for the sliders
        with open("settings/gameSettings.json", "r") as loop:
            data = json.load(loop)
            
            

        # Modifies the content of the sliders
        with open('settings/gameSettings.json', 'w') as update:
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

        with open("settings/data.json", "r") as loop:
            dataBox = json.load(loop)
            
            # Loops to grab the data from the JSON objects
            for i in dataBox["Resolution"]:
                self.resolutionBox.addItem(i)
                
            for i in dataBox["Display Mode"]:
                self.DisplayMode.addItem(str(i))
                
            for i in dataBox["Display Mode"]:
                self.antiAliasingBox.addItem(i)
            
            for i in dataBox["LOD Distance"]:
                self.lodDistanceBox.addItem(i)
        


        
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
        # Checks the content of the comboboxes
        
            if index == "Local":
                print("Local")
                self.gameModes.setCurrentIndex(0)
                self.ipAddress.setText("127.0.0.1")
                self.ipAddress.setReadOnly(True)
                 
                # Checks if platform is linux or windows
                if platform == "linux" or platform == "linux2":
                    self.playGame.clicked.connect(self.linuxLocalHost)
        
                if platform == "win32":
                    self.playGame.clicked.connect(self.win32LocalHost)
                
            elif index == "Server":
                print("Server")
                self.gameModes.setCurrentIndex(1)
                self.ipAddress.setText("")
                self.ipAddress.setReadOnly(False)

                if platform == "linux" or platform == "linux2":
                    self.playGame.clicked.connect(self.linuxServerHost)

                if platform == "win32":
                    self.playGame.clicked.connect(self.serverHost)
                
    
    # Loads up the content pack folder and lets the user select the content pack
    # Uses a treeview to show the actual contents of the folder itself
    def contentPackExplorer(self):
        # Gives us the proper path
        path ="contentpacks"

        # Creates a new filesystemmodel, makes it easy to click on .mf files
        self.display = QtWidgets.QFileSystemModel()

        self.display.setRootPath((QtCore.QDir.rootPath()))

        self.treeView.setModel(self.display)
        self.treeView.setRootIndex(self.display.index(path))
        self.treeView.setSortingEnabled(True)

    
    # Opens the contents of the zip file and looks for mf file
    # replaces the contents of the resource folder with the resources provided with the .mf
    def contentPackOpener(self, index):
        # Grabs the name of the file and file path
        index = self.treeView.currentIndex()
        file = self.display.filePath(index)

        # Allows us to break the path into multiple segments
        p = Path(file)

        # Lets us store the paths for later
        dirContentPacks = "./contentpacks"
        dirResources = "./resources"

        # Decompresses the .mf files
        print("Now unzipping .mf file...please hold")
        os.chdir("contentpacks")
        contentPackUnzip = subprocess.Popen("multify.exe -x -f " + p.name, shell=False)
        
        # Waits till process is done
        contentPackUnzip.wait()

        print("Okay, I'm done unzipping all the files:")
        print("Now moving files to resources!")
        
        # Search through all folders and files
        os.chdir("../")
        for root, folders, files in os.walk(dirContentPacks):

            # Look at each file
            for contentFile in files:

                # Save the path to the file from the ./content_packs/ folder
                contentRoot = root

                # Replace the ./content_packs/ path with the ./resources/ path
                resourceRoot = root.replace(dirContentPacks, dirResources)
                resourceFilePath = os.path.join(resourceRoot, contentFile)

                # Check whether the directory ./resources/ has that file
                if os.path.exists(resourceFilePath):

                # If so, replace the file inside ./resources/ with the one from ./content_packs/
                    contentFilePath  = os.path.join(contentRoot, contentFile)
                    shutil.copyfile(contentFilePath, resourceFilePath)

        print("Now cleaning up")
        print(os.getcwd())

        # Going back in to remove files that are folders   
        try:
            shutil.rmtree(dirContentPacks)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
        
        # Make another directory
        os.mkdir("contentpacks")
        
        print("Success! Now launch the game with your new files")
        
    # Runs the astron cluster to start the server
    def startAstronClusterWin32(self):
        os.chdir("dependencies/astron")

    # Starts up the AI server
    def startAiServerWin32(self, districtName, ppython):
        os.environ["MAX_CHANNELS"] = "999999"
        os.environ["STATESERVER"] = "4002"
        os.environ["ASTRON_IP"] = "127.0.0.1:7100"
        os.environ["EVENTLOGGER_IP"] = "127.0.0.1:7198"
        os.environ["DISTRICT NAME"] = ""
        os.environ["BASE_CHANNEL"] = "401000000"

        # Print out echo from batch script
        print("Starting Toontown Stride AI server...\n ppython:" + ppython + 
        "\nDistrict name:" + os.environ["DISTRICT NAME"]+ 
        "\nBase channel" + os.environ["BASE_CHANNEL"] + 
        "\nMax channels" + os.environ["MAX_CHANNELS"] +
        "\nAstron IP:" + os.environ["ASTRON_IP"] +
        "\nEvent Logger IP:" + os.environ["EVENTLOGGER_IP"])

    # Starts up the uberdog server
    def startUberDogWin32(self, ppython):
        # Create enviroment variables
        os.environ["MAX_CHANNELS"] = "999999"
        os.environ["STATESERVER"] = "4002"
        os.environ["ASTRON_IP"] = "127.0.0.1:7100"
        os.environ["EVENTLOGGER_IP"] = "127.0.0.1:7198"
        os.environ["BASE_CHANNEL"] = "1000000"
        
    # Code to log onto a server that has already been started
    # Added support for JSON loading data
    def serverHost(self):
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

    def linuxServerHost(self):
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
    def linuxLocalHost(self):
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
    def win32LocalHost(self):
        # Grabs ppython from where the user selects
        PPython, randomtext = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open ppython file"), self.tr("C:\\"), self.tr("PPython (*.exe)"))
        
        with open('settings/game_settings.json') as loop:
            data = json.load(loop)

        Username = data["Login Settings"]["Username"]
        districtName = data["Login Settings"]["District Name"]
        backendir = os.chdir("dev/backend/")
        # Check to prevent a blank user
        if not Username:
            QtWidgets.QMessageBox.about(self, "Name required", "Hey! \nYou need a username before we can start!\n")
            return

        SW_HIDE = 0
        Info = subprocess.STARTUPINFO()

        Info.dwFlags = subprocess.STARTF_USESHOWWINDOW
        Info.wShowWindow = SW_HIDE

        # Starts the server processes needed for windows localhost
        startAstronClusterWin32()
        startAiServerWin32(districtName, PPython)
        startUberDogWin32(PPython)

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
        main_menu.show()
        main_menu.exec_()
        main_menu.setWindowModality(QtCore.Qt.WindowModal)

# Initates the basic UI elements
class mainWindow(mainWindow.Ui_MainWindow, QtWidgets.QMainWindow):
     
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.options_menu.clicked.connect(self.optionsMenu)
        

    # Opens the content pack window
    def optionsMenu(self):

        # Loads JSON data each time we venture into the options menu, makes it easy to store data
        with open('settings/gameSettings.json', 'r') as loop:
            data = json.load(loop)

        with open('settings/gameSettings.json', 'w') as loop:
            data["Login Settings"]["Username"]  = self.name.text()
            data["Login Settings"]["District Name"] = self.districtName.text()
            json.dump(data, loop, indent = 1)

        # Assigns username data to JSON file    
        self.name.text = data["Login Settings"]["Username"]
        self.districtName.text = data["Login Settings"]["District Name"]
        # Hides the window
        self.hide()

        # Opens the window
        om = optionsMenu()
        om.show()
        om.exec_()
        om.setWindowModality(QtCore.Qt.WindowModal)

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = mainWindow()
    qt_app.show()
    app.exec_()
