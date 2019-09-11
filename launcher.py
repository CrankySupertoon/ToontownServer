from PySide2 import QtWidgets
import subprocess
import os
from ui import main, serverMenu, CPL

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
        
    def combo_options(self, txt):
        if self.option.currentTextChanged.connect(self.localHost):
            self.option.setCurrentIndex(0)
            print("Username is: " + self.name.text())
            self.IP.setText("127.0.0.1")
            self.IP.setReadOnly(True)
            self.playButton.clicked.connect(self.localHost)
        
        
        print("Current text is: " + txt)
    # Code to log onto a server that has already been started
    def serverHost(self):
        # Grabs the server text and IP to pass into panda
        Username = self.name.text()
        IP_Address = self.IP.text()

        # Sets up enviroment variables needed to launch the game
        os.environ['input'] = '1'
        os.environ['TTS_GAMESERVER'] = IP_Address
        os.environ['TTS_PLAYCOOKIE'] = Username

        #os.environ['PANDADIRECTORY'] = 
        subprocess.Popen("C:/Panda3D-1.10.0/python/ppython.exe -m toontown.toonbase.ToontownStart", shell = False)
        self.close()

    # Code to start local host(DEFAULT OPTION)
    def localHost(self):
        BackendDir = os.chdir("dev/backend/")
        Username = self.name.text()
        
        # Check to prevent a blank user
        if not Username:
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
    
        os.environ['TTS_PLAYCOOKIE'] = Username
        subprocess.Popen("C:\Panda3D-1.10.0\python\ppython.exe -m toontown.toonbase.ToontownStart", shell = False)
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = MyApp()
    qt_app.show()
    app.exec_()

    
   