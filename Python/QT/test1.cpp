/********************************************************************************
** Form generated from reading UI file 'test1O27688.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef TEST1O27688_H
#define TEST1O27688_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QFrame>
#include <QtGui/QGridLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MyLoginForm
{
public:
    QFrame *mainFrame;
    QGridLayout *gridLayout;
    QLineEdit *lineEdit;
    QLabel *label;
    QSpacerItem *horizontalSpacer;
    QPushButton *pushButton;
    QSpacerItem *horizontalSpacer_2;

    void setupUi(QWidget *MyLoginForm)
    {
        if (MyLoginForm->objectName().isEmpty())
            MyLoginForm->setObjectName(QString::fromUtf8("MyLoginForm"));
        MyLoginForm->resize(400, 300);
        MyLoginForm->setStyleSheet(QString::fromUtf8("#MyLoginForm {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(75, 93, 72, 255), stop:1 rgba(156, 166, 62, 255))\n"
"}\n"
"\n"
"#mainFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background-color: rgba(255,255,255, 50%);\n"
"}\n"
"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 150px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}"));
        mainFrame = new QFrame(MyLoginForm);
        mainFrame->setObjectName(QString::fromUtf8("mainFrame"));
        mainFrame->setGeometry(QRect(50, 40, 301, 221));
        mainFrame->setAutoFillBackground(false);
        mainFrame->setFrameShape(QFrame::StyledPanel);
        mainFrame->setFrameShadow(QFrame::Raised);
        gridLayout = new QGridLayout(mainFrame);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        lineEdit = new QLineEdit(mainFrame);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        gridLayout->addWidget(lineEdit, 0, 2, 1, 1);

        label = new QLabel(mainFrame);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 0, 1, 1, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 0, 0, 1, 1);

        pushButton = new QPushButton(mainFrame);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        gridLayout->addWidget(pushButton, 1, 2, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 0, 3, 1, 1);


        retranslateUi(MyLoginForm);

        QMetaObject::connectSlotsByName(MyLoginForm);
    } // setupUi

    void retranslateUi(QWidget *MyLoginForm)
    {
        MyLoginForm->setWindowTitle(QApplication::translate("MyLoginForm", "Form", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MyLoginForm", "Name:", 0, QApplication::UnicodeUTF8));
        pushButton->setText(QApplication::translate("MyLoginForm", "Bl\303\266der Button", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MyLoginForm: public Ui_MyLoginForm {};
} // namespace Ui

QT_END_NAMESPACE

#endif // TEST1O27688_H
