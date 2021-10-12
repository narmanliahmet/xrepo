#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.setFixedSize(1920,1080);
    w.move(0,0);
    w.show();
    return a.exec();
}
