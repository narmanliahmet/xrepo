#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QLabel>
#include <QPushButton>
#include <QString>
#include <QMessageBox>
#include <QList>
#include <QMap>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
private slots:
    void handleButton(int ind, QString name);
private:
    Ui::MainWindow *ui;
    QLabel *header;
    QLabel *back;
    QMap<int, QPushButton*> *tables;
    QMainWindow *pop;
    QMap<int, QMap<QString, bool>> menu;
    QHash<QString, bool> pays;

};
#endif // MAINWINDOW_H
