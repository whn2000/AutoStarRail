# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'script_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QVBoxLayout,
                               QWidget)

from qfluentwidgets import SmoothScrollArea


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(561, 408)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.SmoothScrollArea = SmoothScrollArea(Frame)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName(u"scroll_widget")
        self.scroll_widget.setGeometry(QRect(0, 0, 559, 406))
        self.SmoothScrollArea.setWidget(self.scroll_widget)

        self.verticalLayout.addWidget(self.SmoothScrollArea)

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)

    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
    # retranslateUi
