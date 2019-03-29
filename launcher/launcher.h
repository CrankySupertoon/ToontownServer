#ifndef LAUNCHER_H
#define LAUNCHER_H

#include <QMainWindow>
#include <QDir>
#include <QProcess>
namespace Ui {
class Launcher;
}

class Launcher : public QMainWindow
{
    Q_OBJECT

public:
    explicit Launcher(QWidget *parent = nullptr);
    ~Launcher();

private slots:

    void on_panda3d_locater_2_clicked();

    void on_Play_clicked();


    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

private:
    Ui::Launcher *ui;
};

#endif // LAUNCHER_H
