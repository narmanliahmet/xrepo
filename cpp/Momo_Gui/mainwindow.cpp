#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setStyleSheet("background-color: rgb(50,20,0)");
    this->setWindowTitle("MMK-v1.0.0");
    // Construct
    header = new QLabel(this);
    pop = new QMainWindow(this);
    // Configure popup
    pop->setFixedSize(1000,700);
    pop->move((1920-1000)/2, (1080-700)/2-100);
    QPushButton *confirm = new QPushButton(pop);
    confirm->setText("Hesapla");
    confirm->setStyleSheet("QPushButton{font-size: 30px; color: rgb(0,0,0); background-color: rgb(200,50,0);border: 5px solid green; border-radius: 50px; border-style: inset;} QPushButton::hover{background-color: rgb(255,255,255);} QPushButton::pressed{background-color: rgb(0,0,0);}");
    confirm->resize(200, 100);
    confirm->move(750, 550);

    QSpinBox *coffee1 = new QSpinBox(pop);
    coffee1->setRange(0,20);
    coffee1->setSingleStep(1);
    coffee1->setValue(0);
    coffee1->resize(200, 50);
    coffee1->move(10, 50);
    coffee1->setStyleSheet("background-color: rgb(100,200,0);");

    QSpinBox *coffee2 = new QSpinBox(pop);
    coffee2->setRange(0,20);
    coffee2->setSingleStep(1);
    coffee2->setValue(0);
    coffee2->resize(200, 50);
    coffee2->move(10, 150);
    coffee2->setStyleSheet("background-color: rgb(100,200,0);");

    QSpinBox *coffee3 = new QSpinBox(pop);
    coffee3->setRange(0,20);
    coffee3->setSingleStep(1);
    coffee3->setValue(0);
    coffee3->resize(200, 50);
    coffee3->move(10, 250);
    coffee3->setStyleSheet("background-color: rgb(100,200,0);");

    QSpinBox *coffee4 = new QSpinBox(pop);
    coffee4->setRange(0,20);
    coffee4->setSingleStep(1);
    coffee4->setValue(0);
    coffee4->resize(200, 50);
    coffee4->move(10, 350);
    coffee4->setStyleSheet("background-color: rgb(100,200,0);");

    QSpinBox *coffee5 = new QSpinBox(pop);
    coffee5->setRange(0,20);
    coffee5->setSingleStep(1);
    coffee5->setValue(0);
    coffee5->resize(200, 50);
    coffee5->move(260, 50);
    coffee5->setStyleSheet("background-color: rgb(100,200,0);");

    QSpinBox *coffee6 = new QSpinBox(pop);
    coffee6->setRange(0,20);
    coffee6->setSingleStep(1);
    coffee6->setValue(0);
    coffee6->resize(200, 50);
    coffee6->move(260, 150);
    coffee6->setStyleSheet("background-color: rgb(100,200,0);");

    QSpinBox *coffee7 = new QSpinBox(pop);
    coffee7->setRange(0,20);
    coffee7->setSingleStep(1);
    coffee7->setValue(0);
    coffee7->resize(200, 50);
    coffee7->move(260, 250);
    coffee7->setStyleSheet("background-color: rgb(100,200,0);");

    QSpinBox *coffee8 = new QSpinBox(pop);
    coffee8->setRange(0,20);
    coffee8->setSingleStep(1);
    coffee8->setValue(0);
    coffee8->resize(200, 50);
    coffee8->move(260, 350);
    coffee8->setStyleSheet("background-color: rgb(100,200,0);");

    // Configure

    /// Header
    header->setText(QString("MOMO MASA KONTROL"));
    QFont font = header->font();
    font.setBold(true);
    font.setFamily(QString("Helvetica"));
    font.setPointSize(50);
    header->setFont(font);
    header->setAlignment(Qt::AlignCenter);
    header->move(10,10);
    header->setFixedSize(1920-20, 100);
    header->setStyleSheet("background-color: rgb(80,100,0);color: rgb(240,100,0); border: 5px; border-color: rgb(150,60,0); border-radius: 10px; border-style: inset");

    ///
    /// QPushButtons
    QPushButton *list_sum = new QPushButton(this);
    list_sum->setText("ÖZET");
    list_sum->setStyleSheet("QPushButton{font-size: 60px; color: rgb(0,0,0); background-color: rgb(200,50,0);border: 5px solid green; border-radius: 50px; border-style: inset;} QPushButton::hover{background-color: rgb(255,255,255);} QPushButton::pressed{background-color: rgb(0,0,0);}");
    list_sum->resize(200,100);
    list_sum->move(1920-250, 200);
    QList<QString> products = {"Kahve 1", "Kahve 2", "Kahve 3", "Kahve 4", "Kahve 5", "Kahve 6", "Kahve 7", "Kahve 8", "Kahve 9", "Kahve 10", "Kahve 11", "Kahve 12", "Kahve 13", "Kahve 14", "Kahve 15", "Kahve 16", "Kahve 17"};
    QList<float> prval = {16.6, 16.6, 16.6, 16.6, 16.6, 16.6, 16.6, 16.6,16.6, 16.6, 16.6, 16.6, 16.6, 16.6, 16.6, 16.6, 16.6};
    QList<QString> sqr_names = {"AğaçKakan","Tomruk","Gürgen","Sarmaşık"};
    QList<QString> wrk_names = {"Arbeit 1","Arbeit 2","Arbeit 3","Arbeit 4","İşGüç 1","İşGüç 2","İşGüç 3","İşGüç"};
    tables = new QMap<int, QPushButton*>();
    int nrnd = 8;
    int nsqr = 4;
    int work = 8;
    for (int j = 0; j<products.size(); j++){
        for (int i=0; i<nrnd; i++) {
            pays.insert(QString(QString('A' + i) + products[j]), false);
        }
    }
    for (int j = 0; j<products.size(); j++){
        for (int i=0; i<nsqr; i++) {
            pays.insert(QString(sqr_names[i] + products[j]), false);
        }
    }
    for (int j = 0; j<products.size(); j++){
        for (int i=0; i<work; i++) {
            pays.insert(QString(wrk_names[i] + products[j]), false);
        }
    }
    for (int i=0; i<(nrnd+nsqr+work); i++ ) {
        if (i<nrnd) {
            tables->insert(i, new QPushButton(QString('A'+i),this));
            tables->find(i).value()->move(((1920-100*5)/5)*(i%4+1)+100*(i%4), (i/4)*150+150);
            tables->find(i).value()->resize(100,100);
            if (i==nrnd-1)
                tables->find(i).value()->setStyleSheet(QString("QPushButton{font-size: 60px; color: rgb(0,0,0); background-color: rgb(%1,%2,%3);border: 5px solid green; border-radius: 50px; border-style: inset;} QPushButton::hover{background-color: rgb(255,255,255);} QPushButton::pressed{background-color: rgb(0,0,0);} ").arg(255).arg(255).arg(255));
            else
                tables->find(i).value()->setStyleSheet(QString("QPushButton{font-size: 60px; color: rgb(0,0,0); background-color: rgb(%1,%2,%3);border: 5px solid green; border-radius: 50px; border-style: inset;} QPushButton::hover{background-color: rgb(255,255,255);} QPushButton::pressed{background-color: rgb(0,0,0);} ").arg((255-i*(255/8))).arg((i*(255/4)%255)).arg((i*(255/2))%255));
            connect(tables->find(i).value(), &QPushButton::clicked, [i,this](){handleButton(i, tables->find(i).value()->text());});
            tables->find(i).value()->show();
//            pays->insert(QString('A'+i), prmap);
        }
        else if (i<(nrnd+nsqr)) {
            tables->insert(i, new QPushButton(sqr_names[i-8], this));
            tables->find(i).value()->move(((1920-100*5)/5)*((i-8)%4+1)+100*((i-8)%4)-50, ((i-8)/4)*150+450);
            tables->find(i).value()->resize(200,100);
            tables->find(i).value()->setStyleSheet(QString("QPushButton{font-size: 30px; color: rgb(0,0,0); background-color: rgb(%1,%2,%3);border: 5px solid green; border-style: outset;} QPushButton::hover{background-color: rgb(255,255,255);} QPushButton::pressed{background-color: rgb(0,0,0);} ").arg((255-(i-8)*(255/8))).arg(((i-8)*(255/4)%255)).arg(((i-8)*(255/2))%255));
            connect(tables->find(i).value(), &QPushButton::clicked, [i,this](){handleButton(i, tables->find(i).value()->text());});
            tables->find(i).value()->show();
//            pays->insert(sqr_names[i-8], prmap);
        }
        else if ((i==nrnd+nsqr+work-1) | (i < nrnd+nsqr+4)){
            tables->insert(i, new QPushButton(wrk_names[i-12], this));
            tables->find(i).value()->move(((1920-100*5)/5)*((i-12)%4+1)+100*((i-12)%4)-150, ((i-12)/4)*150+600);
            tables->find(i).value()->resize(400,100);
            if (i==nrnd+nsqr+work-1)
                tables->find(i).value()->setStyleSheet(QString("QPushButton{font-size: 40px; color: rgb(0,0,0); background-color: rgb(%1,%2,%3);border: 5px solid green; border-style: outset;} QPushButton::hover{background-color: rgb(255,255,255);} QPushButton::pressed{background-color: rgb(0,0,0);} ").arg(255).arg(255).arg(255));
            else
                tables->find(i).value()->setStyleSheet(QString("QPushButton{font-size: 40px; color: rgb(0,0,0); background-color: rgb(%1,%2,%3);border: 5px solid green; border-style: outset;} QPushButton::hover{background-color: rgb(255,255,255);} QPushButton::pressed{background-color: rgb(0,0,0);} ").arg((255-(i-12)*(255/8))).arg(((i-12)*(255/4)%255)).arg(((i-12)*(255/2))%255));
            connect(tables->find(i).value(), &QPushButton::clicked, [i,this](){handleButton(i, tables->find(i).value()->text());});
            tables->find(i).value()->show();
//            pays->insert(wrk_names[i-12], prmap);
        }
    }
    //Paycheck Maps
            // Initiate
    list_sum->show();
    header->show();
}

MainWindow::~MainWindow()
{
    delete ui;
    delete header;
    delete tables;
    delete pop;
    delete back;
}

void MainWindow::handleButton(int ind, QString name)
{
    pop->setWindowTitle(name);
    qDebug()<< name;
    pays.insert("AKahve 5", true);
    qDebug() << pays.value("AKahve 5");
    pop->show();
}
