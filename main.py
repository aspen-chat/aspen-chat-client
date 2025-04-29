import sys

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListView,
                               QMainWindow, QTextBrowser, QTextEdit,
                               QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(767, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.servers = QListView(self.centralwidget)
        self.servers.setObjectName(u"servers")
        self.servers.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.servers)

        self.channels = QListView(self.centralwidget)
        self.channels.setObjectName(u"channels")
        self.channels.setMinimumSize(QSize(200, 0))
        self.channels.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.channels)

        self.mainChatArea = QVBoxLayout()
        self.mainChatArea.setObjectName(u"mainChatArea")
        self.messagesView = QTextBrowser(self.centralwidget)
        self.messagesView.setObjectName(u"messagesView")
        self.messagesView.setMinimumSize(QSize(300, 60))

        self.mainChatArea.addWidget(self.messagesView)

        self.isTypingLabel = QLabel(self.centralwidget)
        self.isTypingLabel.setObjectName(u"isTypingLabel")

        self.mainChatArea.addWidget(self.isTypingLabel)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 100))

        self.mainChatArea.addWidget(self.textEdit)

        self.horizontalLayout.addLayout(self.mainChatArea)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aspen", None))
    # retranslateUi


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    win = Ui_MainWindow()
    win.setupUi(window)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
