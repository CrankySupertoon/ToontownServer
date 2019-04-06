#include "launcher.h"
#include "ui_launcher.h"
#include <QTimer>
#include <QUrl>
#include <QtNetwork/QNetworkAccessManager>
#include <QFileDialog>
#include <QFile>
#include <QMessageBox>
#include <QProcess>
#include <QDesktopServices>
#include "constants.h"
Launcher::Launcher(QWidget *parent) : QMainWindow(parent), ui(new Ui::Launcher)
{
    //gameInstances = 0;
    ui->setupUi(this);
}

Launcher::~Launcher()
{
    this->setFixedSize(600,600);
}


bool isDuplicate(QString username)
{

}
QString pandaHolder(QString panda)
{
    PANDAPATH = panda;
    PPYTHON_PATH = PANDAPATH + "/python/ppython.exe";
    return PANDAPATH;
}


void Launcher::on_panda3d_locater_2_clicked()
{

    // Allows the user to set the existing directory to the decomp project.

    QString panda = QFileDialog::getExistingDirectory(this, tr("Open Directory"),
                                                    "/home",
                                                    QFileDialog::ShowDirsOnly
                                                    | QFileDialog::DontResolveSymlinks);


     PANDAPATH = panda;
     PPYTHON_PATH = PANDAPATH + "/python/ppython.exe";
}


void Launcher::on_Play_clicked()
{
    QStringList params;
    params << START;
    QProcess *process;
    QString panda = QFileDialog::getExistingDirectory(this, tr("Open Directory"),
                                                    "/home",
                                                    QFileDialog::ShowDirsOnly
                                                    | QFileDialog::DontResolveSymlinks);
    QMessageBox q;
    PANDAPATH = panda;
    PPYTHON_PATH = PANDAPATH + "/python/ppython.exe";
    USERNAME = ui->userNameEdit->text();
    QString text = ui->gameMode_Box->currentText();
    TTS_PLAYCOOKIE = USERNAME;
    QString output;
    if(text == "Localhost")
    {

         GAME_MODE = "Localhost";
         GAME_SERVER = "replace this with IP";
        output = ("Starting Toontown Stride...\nPPython directory: " + PPYTHON_PATH + "\nUsername: " + USERNAME + "\nGameserver: " + GAME_SERVER + "\nGame mode: " + GAME_MODE);
        // set the IP address to local host
       q.setWindowTitle("Information");
       q.setText("Starting Toontown Stride...\nppython: " + PPYTHON_PATH + "\nUsername: " + USERNAME + "\nGameserver: " + GAME_SERVER + "\nGame mode: " + GAME_MODE);
       q.exec();
       process->start("python");
       process->waitForFinished();


    }

    // sets the stuff for the server
    if(text == "Server")
    {
        GAME_MODE = "Server";
        GAME_SERVER = "replace this with IP";
        output = ("Starting Toontown Stride...\nPPython directory: " + PPYTHON_PATH + "\nUsername: " + USERNAME + "\nGameserver: " + GAME_SERVER + "\nGame mode: " + GAME_MODE);
        // set the IP address to local host
        q.setWindowTitle("Information");
        q.setText("Starting Toontown Stride...\nppython: " + PPYTHON_PATH + "\nUsername: " + USERNAME + "\nGameserver: " + GAME_SERVER + "\nGame mode: " + GAME_MODE);
        q.exec();
        system("launcher.bat " + PPYTHON_PATH);
    }
}

void Launcher::on_pushButton_clicked()
{
    QUrl githubDirect;
    githubDirect.setScheme("http");
    githubDirect.setHost("github.com");
    githubDirect.setPath("/zenith110/Toontown_Server");
    QDesktopServices::openUrl(githubDirect);
}

void Launcher::on_pushButton_2_clicked()
{
    QUrl githubDirect;
    githubDirect.setScheme("http");
    githubDirect.setHost("github.com");
    githubDirect.setPath("/zenith110/Toontown_Server/issues");
    QDesktopServices::openUrl(githubDirect);
}
