# Created by Abrahan Nevarez on August 24th 2019
# Created for the use of the base game Toontown Stride
# Can be modified for other servers
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
import os
import subprocess
import sys
import zipfile
from PySide2 import QtWidgets
from ui import main, CPL


# Content pack launcher
# Lets the user select content packs and replace current resources with them
# Accepts .mf only
class Content_Pack_Launcher(CPL.Ui_CPL, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Content_Pack_Launcher, self).__init__(parent)
        self.setupUi(self)
<<<<<<< Updated upstream
        path = "/content_pack"
        # Checks if content pack folder is made, otherwise make it
        if os.path.isdir(path):
            print("this exists, doing nothing!\n")
        else:
            print("this does not exist, now making!")
            os.makedirs(path)
=======
        path = "content_packs"
        dir_name = "default_pack"
        resources_dir = "/resources"

        # Checks if content pack folder is made, otherwise make it
        if os.path.isdir(path):
            print("This exists, not going to create a new folder, let's switch into it!\n")
            os.chdir(path)
        else:
            print("this does not exist, now making!")
            os.makedirs(path)
            os.chdir("/content_packs")
>>>>>>> Stashed changes

        # self.load.clicked.connect(self.open_resource_folder)
        self.back.clicked.connect(self.return_main)

        self.name.setReadOnly(True)
        self.author.setReadOnly(True)
<<<<<<< Updated upstream
        self.load2.clicked.connect(self.content_pack_opener)
=======
        #self.load2.clicked.connect(self.content_pack_opener)
>>>>>>> Stashed changes

        # If no .mf exists, compress the resource folder into a .mf file and name it default, and add to combobox
        os.chdir("content_pack")
        '''if (open("default.mf", 'w')):
            print("yay, the default file is compressed!")
        else:
            print("Ok, let's compress that bad boi!")
            os.chdir("../resources/")
            dir_name = os.getcwd()
            retrieve_file(dir_name)
            zipper(dir_name)'''
            # Selects all the files and compresses

        def return_main(self):
            self.hide()
            main_win = main_window()
            main_win.show()
            main_win.exec_()

            # Opens resource folder 

        def open_resource_folder(self):
            if os.path.isdir(path) is not True:
                print("Not in content pack folder, changing!")
                content_pack_dir = os.chdir("content_pack")
                content = os.getcwd()
                os.system(f'start {os.path.realpath(os.getcwd())}')
            else:
                print("I'm in content packs!")
                os.system(f'start {os.path.realpath(os.getcwd())}')

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
    file = QFileDialog.getOpenFileName(self, tr("Open mf"), path, tr("MF files (*.mf)"))


<<<<<<< Updated upstream
=======
        if open("default.mf", 'w'):
            print("Current dir is : %s", os.getcwd())
            #print("Ok, let's compress that bad boi!")

            if os.path.isdir(resources_dir):
                print("Currently in resources, no need to change!")
            else:
                print("Not present in resources... changing...")
                os.chdir("../")
                print("Current dir is : %s", os.getcwd())
                resources_path = os.chdir("resources")
                print("Current dir is : %s", os.getcwd())


            #folder_name = os.getcwd()
            #retrieve_file(dir_name)
            #zipper(dir_name)


            # Selects all the files and compresses

    def return_main(self):
        self.hide()
        main_win = main_window()
        main_win.show()
        main_win.exec_()

            # Opens resource folder 

        def open_resource_folder(self):
            if os.path.isdir(path) is not True:
                print("Not in content pack folder, changing!")
                content_pack_dir = os.chdir("content_pack")
                content = os.getcwd()
                os.system(f'start {os.path.realpath(os.getcwd())}')
            else:
                print("I'm in content packs!")
                os.system(f'start {os.path.realpath(os.getcwd())}')

            def retrieve_file(dir_name):
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

        print(dir_name + '.zip file is created successfully!')


# Opens the contents of the zip file and looks for mf file
# replaces the contents of the resource folder with the resources provided with the .mf
def content_pack_opener(self):
    file = QFileDialog.getOpenFileName(self, tr("Open mf"), path, tr("MF files (*.mf)"))


>>>>>>> Stashed changes
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
            self.playButton.clicked.connect(self.local_host)
        else:
            print("Server")
            self.option.setCurrentIndex(1)
            self.IP.setText("")
            print("Username is: " + self.name.text())
            self.playButton.clicked.connect(self.local_host)

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
