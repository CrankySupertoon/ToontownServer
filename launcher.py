# Created by Abrahan Nevarez on August 24th 2019
# Created for the use of the base game Toontown Stride
# Can be modified for other servers

import os
import subprocess
from sys import platform
import zipfile
from PySide2 import QtWidgets, QtCore, QtGui
import shutil
from pathlib import Path
from ui import main, CPL

# Content pack launcher
# Lets the user select content packs and replace current resources with them
# Accepts .mf only
class Content_Pack_Launcher(CPL.Ui_CPL, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Content_Pack_Launcher, self).__init__(parent)
        self.setupUi(self)
        path = "content_packs"
        resources_dir = "resources"
        default_name = "default"

        # Checks if content pack folder is made, otherwise make it
        if os.path.isdir(path):
            print("this exists, doing nothing!\n")
            os.chdir(path)
            print("Current dir is : ", os.getcwd())
            self.load.clicked.connect(self.open_resource_folder)
        else:
            print("this does not exist, now making!")
            os.makedirs(path)
            os.chdir(path)
            

        # self.load.clicked.connect(self.open_resource_folder)
        self.back.clicked.connect(self.return_main)
        self.load_cp.clicked.connect(self.content_pack_opener)

        if open("default.mf", 'w'):
            try:
                if os.path.isdir(resources_dir):
                    print("Currently in resources, no need to change!")
                else:
                    print("Not present in resources... changing...")
                    os.chdir("../")
                    print("Current dir is : ", os.getcwd())
                    if os.path.isdir(resources_dir):
                        print("I'm here to prevent an error when there's a folder error\n")
                    else:
                        resources_path = os.chdir("resources")
                        print("Current dir is : ", os.getcwd())
                        print("Now done with directory change")
                    
            except ValueError:
                print("Wtf man...why am I doing this twice?")

    # Is the back button, returns to main menu       
    def return_main(self):
        self.hide()
        main_win = main_window()
        main_win.show()
        main_win.exec_()
        print("Now returning to main menu!")
        os.chdir("../")

    # Opens resource folder 
    def open_resource_folder(self, path):
        if os.path.isdir("content_packs"):
            os.chdir("content_packs")

            if os.path.isdir("content_packs"):
                os.system(f'start {os.path.realpath(os.getcwd())}')
                os.chdir("../")

            '''def retrieve_file(dir_name):
                # setup file paths variable
                filePaths = []

                # Read all directory, subdirectories and file lists
                for root, directories, files in os.walk(dir_name):
                    for filename in files:
                        # Create the full filepath by using os module.
                        filePath = os.path.join(root, filename)
                        filePaths.append(filePath)

            # return all paths
            return filePaths

    def zipper(dir_name):
        # writing files to a zipfile
        zip_file = zipfile.ZipFile(dir_name + '.zip', 'w')
        with zip_file:
            # writing each file one by one
            for file in filePaths:
                zip_file.write(file)

        print(dir_name + '.zip file is created successfully!')'''

        
    # Opens the contents of the zip file and looks for mf file
    # replaces the contents of the resource folder with the resources provided with the .mf
    def content_pack_opener(self):
        file, filename = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open mf"), self.tr("content_packs"), self.tr("MF files (*.mf)"))
        os.chdir("content_packs")

        # Allows us to break the path into multiple segments
        p = Path(file)

        # Decompresses the .mf files
        print("Now unzipping .mf file...please hold")
        content_pack_unzip = subprocess.Popen("multify.exe -x -f " + p.name, shell=False)
        content_pack_unzip.wait()

        print("Okay, I'm done unzipping all the files:")
        print("Now moving files to resources!")

        for file_name in os.listdir(os.getcwd()):
            if not file_name.endswith(".mf"):
                print(file_name)
                shutil.move(file_name, "../resources")

        print("Success! Now launch the game with your new files")
        os.chdir("../")
            
        
# Initates the basic UI elements
class main_window(main.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)

        # Sets the combobox item value to a blank item
        self.option.setCurrentIndex(-1)
        # Connects the signal for both
        self.option.currentTextChanged.connect(self.combo_options)
        if not self.name.text:
            QtWidgets.QMessageBox.about(self, "IP address", "Hey! \nYou need a name in order to launch the game\n")

        self.cp.clicked.connect(self.content_pack_window)
        print("Directory is currently: " + os.getcwd())
    # Opens the content pack window
    def content_pack_window(self):
        self.hide()
        cpl = Content_Pack_Launcher()
        cpl.show()
        cpl.exec_()

    def combo_options(self, index):
        
        if index == "Local":
            print("Local")
            self.option.setCurrentIndex(0)

            print("Username is: " + self.name.text())

            self.IP.setText("127.0.0.1")
            self.IP.setReadOnly(True)
            # Checks if platform is linux or windows
            if platform == "linux" or platform == "linux2":
                self.playButton.clicked.connect(self.linux_local_host)
            if platform == "win32":
                self.playButton.clicked.connect(self.win32_local_host)
        else:
            print("Server")
            self.option.setCurrentIndex(1)
            self.IP.setText("")
            print("Username is: " + self.name.text())
            self.playButton.clicked.connect(self.server_host)

    # Code to log onto a server that has already been started
    def server_host(self):
        # Grabs the server text and IP to pass into panda
        username = self.name.text()
        IP_Address = self.IP.text()

        # Sets up enviroment variables needed to launch the game
        os.environ['input'] = '1'
        os.environ['TTS_GAMESERVER'] = IP_Address
        os.environ['TTS_PLAYCOOKIE'] = username

        # os.environ['PANDADIRECTORY'] =
        subprocess.Popen("C:/Panda3D-1.10.0/python/ppython.exe -m toontown.toonbase.ToontownStart", shell=False)
        self.close()
    def linux_server_host(self):
        os.chdir("../")
        # Grabs the server text and IP to pass into panda
        username = self.name.text()
        IP_Address = self.IP.text()

        # Sets up enviroment variables needed to launch the game
        os.environ['input'] = '1'
        os.environ['TTS_GAMESERVER'] = IP_Address
        os.environ['TTS_PLAYCOOKIE'] = username

        # os.environ['PANDADIRECTORY'] =
        subprocess.Popen("ppython -m toontown.toonbase.ToontownStart", shell=False)
        self.close()

    # Code to start on linux
    def linux_local_host(self):
        os.chdir("../")

        os.environ['DYLD_LIBRARY_PATH'] = '`pwd`/Libraries.bundle'
        os.environ['DYLD_FRAMEWORK_PATH'] = "Frameworks"

        username = self.name.text()
        if not username:
            QtWidgets.QMessageBox.about(self, "Name required", "Hey! \nYou need a username before we can start!\n")
            return
        os.environ['ttsUsername'] = username
        os.environ['TTS_PLAYCOOKIE'] = username

        os.environ['TTS_GAMESERVER'] = "127.0.0.1"

        subprocess.Popen("ppython -m toontown.toonbase.ToontownStart")
        self.close()
    # Code to start local host on windows!
    def win32_local_host(self):
        backendir = os.chdir("dev/backend/")
        username = self.name.text()

        # Check to prevent a blank user
        if not username:
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

        os.environ['TTS_PLAYCOOKIE'] = username
        subprocess.Popen("C:\Panda3D-1.10.0\python\ppython.exe -m toontown.toonbase.ToontownStart", shell=False)
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = main_window()
    qt_app.show()
    app.exec_()
