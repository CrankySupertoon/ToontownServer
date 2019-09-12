from PySide2 import QtWidgets
import subprocess
import os
from ui import main, CPL 
import sys
import zipfile import *
# Created by Abrahan Nevarez
class Content_Pack_Launcher(CPL.Ui_Form, QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Content_Pack_Launcher, self).__init__(parent)

    # Opens the resource folder so the user can put in content folders
    def open_resource_folder(self):

    # Replaces resource file with selected resource that is available in the directory
    def replace_resource(self):

    # Looks at directory, and checks for mf file,then unzips file and puts a zip content of the resources in folder
    def unzip_mf(self):

    # Zips up the default content pack
    def zip_pack(self):

# Initates the basic UI elements
class MyApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        
        # Sets the combobox item value to a blank item
        self.option.setCurrentIndex(-1)
        self.option.currentTextChanged.connect(self.combo_options)
        if not self.name.text:
            QtWidgets.QMessageBox.about(self, "IP address", "Hey! \nYou need a name in order to launch the game\n")
        
        self.contentPacks.connect(self.content_pack_window)

    def content_pack_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = CPL.Ui_Form()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def combo_options(self, txt):
        #if self.option.currentTextChanged.connect(self.localHost):
        if self.option.currentTextChanged == "local"
            self.option.setCurrentIndex(1)
            print("Username is: " + self.name.text())
            self.IP.setText("127.0.0.1")
            self.IP.setReadOnly(True)
            self.playButton.clicked.connect(self.local_host)
        
        
        print("Current text is: " + txt)
    # Code to log onto a server that has already been started
    def server_host(self):
        # Grabs the server text and IP to pass into panda
        username = self.name.text()
        IP_Address = self.IP.text()

        # Sets up enviroment variables needed to launch the game
        os.environ['input'] = '1'
        os.environ['TTS_GAMESERVER'] = IP_Address
        os.environ['TTS_PLAYCOOKIE'] = username

        #os.environ['PANDADIRECTORY'] = 
        subprocess.Popen("C:/Panda3D-1.10.0/python/ppython.exe -m toontown.toonbase.ToontownStart", shell = False)
        self.close()

    # Code to start local host(DEFAULT OPTION)
    def local_host(self):
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

        subprocess.Popen(r"start-astron-cluster.bat", startupinfo = Info)
        subprocess.Popen(r"start-ai-server.bat", startupinfo = Info)
        subprocess.Popen(r"start-uberdog-server.bat", startupinfo = Info)

        ReturnDir = os.chdir("../../")

        os.environ['input'] = '1'
    
        os.environ['TTS_GAMESERVER'] = "127.0.0.1"
    
        os.environ['TTS_PLAYCOOKIE'] = username
        subprocess.Popen("C:\Panda3D-1.10.0\python\ppython.exe -m toontown.toonbase.ToontownStart", shell = False)
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = MyApp()
    qt_app.show()
    app.exec_()

    
   