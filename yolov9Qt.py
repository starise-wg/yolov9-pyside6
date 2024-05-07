# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yolov9Qt.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QSplitter, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1445, 710)
        MainWindow.setMinimumSize(QSize(1445, 710))
        MainWindow.setMaximumSize(QSize(1445, 710))
        font = QFont()
        font.setPointSize(6)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u"icon/1000LOGO.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color:white;}\n"
"")
        self.gridLayoutWidget_7 = QWidget(self.centralwidget)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(310, 670, 851, 34))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.gridLayoutWidget_7)
        self.progressBar.setObjectName(u"progressBar")
        palette = QPalette()
        brush = QBrush(QColor(142, 197, 252, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(215, 215, 215, 100))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(142, 197, 252, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.progressBar.setPalette(palette)
        self.progressBar.setStyleSheet(u"\n"
"QProgressBar{ \n"
"height:5px;\n"
"color: #8EC5FC; \n"
"text-align:center; \n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 5px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background:  #6BABFA;\n"
"border-radius: 7px;\n"
"}")
        self.progressBar.setValue(0)

        self.gridLayout_7.addWidget(self.progressBar, 0, 1, 1, 1)

        self.pushButton_bofang = QPushButton(self.gridLayoutWidget_7)
        self.pushButton_bofang.setObjectName(u"pushButton_bofang")
        self.pushButton_bofang.setMinimumSize(QSize(32, 32))
        self.pushButton_bofang.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_bofang.setStyleSheet(u"border: none")
        icon1 = QIcon()
        icon1.addFile(u"icon/\u64ad\u653e.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_bofang.setIcon(icon1)
        self.pushButton_bofang.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.pushButton_bofang, 0, 0, 1, 1)

        self.pushButton_stop = QPushButton(self.gridLayoutWidget_7)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setMinimumSize(QSize(32, 32))
        self.pushButton_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_stop.setStyleSheet(u"border: none")
        icon2 = QIcon()
        icon2.addFile(u"icon/\u7ec8\u6b62.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_stop.setIcon(icon2)
        self.pushButton_stop.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.pushButton_stop, 0, 2, 1, 1)

        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setGeometry(QRect(0, 0, 1501, 71))
        self.horizontalFrame.setStyleSheet(u"background:#6BABFA;color:white;")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_title = QLabel(self.horizontalFrame)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 Medium"])
        font1.setPointSize(16)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"")
        self.label_title.setTextFormat(Qt.TextFormat.AutoText)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_title)

        self.frame_left_box = QFrame(self.centralwidget)
        self.frame_left_box.setObjectName(u"frame_left_box")
        self.frame_left_box.setGeometry(QRect(5, 80, 301, 621))
        self.frame_left_box.setStyleSheet(u"QFrame#frame_left_box{\n"
"background:#F1F6FF;\n"
"border: 1px solid #F1F6FF;\n"
"border-radius:8px;}")
        self.frame_left_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_left_box.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_is_save_box = QFrame(self.frame_left_box)
        self.frame_is_save_box.setObjectName(u"frame_is_save_box")
        self.frame_is_save_box.setEnabled(True)
        self.frame_is_save_box.setGeometry(QRect(10, 550, 281, 61))
        self.frame_is_save_box.setStyleSheet(u"QFrame#frame_is_save_box{\n"
"background:#6BABFA;}")
        self.frame_is_save_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_is_save_box.setFrameShadow(QFrame.Shadow.Raised)
        self.checkBox_isSave = QCheckBox(self.frame_is_save_box)
        self.checkBox_isSave.setObjectName(u"checkBox_isSave")
        self.checkBox_isSave.setGeometry(QRect(200, 20, 31, 21))
        font2 = QFont()
        font2.setPointSize(16)
        self.checkBox_isSave.setFont(font2)
        self.checkBox_isSave.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_isSave.setIconSize(QSize(40, 40))
        self.label_isSava = QLabel(self.frame_is_save_box)
        self.label_isSava.setObjectName(u"label_isSava")
        self.label_isSava.setGeometry(QRect(50, 20, 141, 21))
        font3 = QFont()
        font3.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_isSava.setFont(font3)
        self.label_isSava.setStyleSheet(u"color:white;")
        self.frame_weights_box = QFrame(self.frame_left_box)
        self.frame_weights_box.setObjectName(u"frame_weights_box")
        self.frame_weights_box.setGeometry(QRect(10, 10, 281, 121))
        self.frame_weights_box.setStyleSheet(u"QFrame#frame_weights_box{border:2px solid #CFEBD2;\n"
"background:white;\n"
"border-radius:8px;}")
        self.frame_weights_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_weights_box.setFrameShadow(QFrame.Shadow.Raised)
        self.line_weights = QLineEdit(self.frame_weights_box)
        self.line_weights.setObjectName(u"line_weights")
        self.line_weights.setGeometry(QRect(10, 60, 211, 41))
        font4 = QFont()
        font4.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font4.setPointSize(11)
        self.line_weights.setFont(font4)
        self.line_weights.setStyleSheet(u"padding-left:6px;\n"
"border:1px solid skyblue;\n"
"border-radius:5px;\n"
"\n"
"\n"
"\n"
"")
        self.line_weights.setEchoMode(QLineEdit.EchoMode.Normal)
        self.line_weights.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.Button_select_w_p = QPushButton(self.frame_weights_box)
        self.Button_select_w_p.setObjectName(u"Button_select_w_p")
        self.Button_select_w_p.setGeometry(QRect(230, 60, 41, 41))
        self.Button_select_w_p.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_select_w_p.setStyleSheet(u"border: none")
        icon3 = QIcon()
        icon3.addFile(u"icon/\u6587\u4ef6\u5939-\u5f00_folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_select_w_p.setIcon(icon3)
        self.Button_select_w_p.setIconSize(QSize(32, 32))
        self.frame_11 = QFrame(self.frame_weights_box)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 0, 281, 41))
        self.frame_11.setStyleSheet(u"border:1px solid #CFEBD2;\n"
"background:#CFEBD2;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0px;")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 91, 21))
        font5 = QFont()
        font5.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setHintingPreference(QFont.PreferFullHinting)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"background:none;\n"
"border:none;")
        self.frame_source_box = QFrame(self.frame_left_box)
        self.frame_source_box.setObjectName(u"frame_source_box")
        self.frame_source_box.setGeometry(QRect(10, 160, 281, 121))
        self.frame_source_box.setStyleSheet(u"QFrame#frame_source_box{border:2px solid #CFEBD2;\n"
"background:white;\n"
"\n"
"border-radius:8px;}")
        self.frame_source_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_source_box.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_13 = QFrame(self.frame_source_box)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(0, 0, 281, 41))
        self.frame_13.setStyleSheet(u"border:1px solid #CFEBD2;\n"
"background:#CFEBD2;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0px;")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 10, 131, 21))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"background:none;\n"
"border:none;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter = QSplitter(self.frame_source_box)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 60, 261, 38))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.Button_checkImg = QPushButton(self.splitter)
        self.Button_checkImg.setObjectName(u"Button_checkImg")
        self.Button_checkImg.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_checkImg.setStyleSheet(u"border: none;")
        icon4 = QIcon()
        icon4.addFile(u"icon/\u7167\u7247_pic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_checkImg.setIcon(icon4)
        self.Button_checkImg.setIconSize(QSize(38, 38))
        self.splitter.addWidget(self.Button_checkImg)
        self.Button_checkVideo = QPushButton(self.splitter)
        self.Button_checkVideo.setObjectName(u"Button_checkVideo")
        self.Button_checkVideo.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_checkVideo.setStyleSheet(u"border: none")
        icon5 = QIcon()
        icon5.addFile(u"icon/\u89c6\u9891_video-two.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_checkVideo.setIcon(icon5)
        self.Button_checkVideo.setIconSize(QSize(38, 38))
        self.splitter.addWidget(self.Button_checkVideo)
        self.Button_openCamera = QPushButton(self.splitter)
        self.Button_openCamera.setObjectName(u"Button_openCamera")
        self.Button_openCamera.setCursor(QCursor(Qt.ClosedHandCursor))
        self.Button_openCamera.setStyleSheet(u"border: none")
        icon6 = QIcon()
        icon6.addFile(u"icon/\u6444\u50cf\u5934_camera-one.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_openCamera.setIcon(icon6)
        self.Button_openCamera.setIconSize(QSize(38, 38))
        self.splitter.addWidget(self.Button_openCamera)
        self.Button_select_folder = QPushButton(self.splitter)
        self.Button_select_folder.setObjectName(u"Button_select_folder")
        self.Button_select_folder.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_select_folder.setStyleSheet(u"border: none")
        icon7 = QIcon()
        icon7.addFile(u"icon/\u56fe\u5c42_layers.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_select_folder.setIcon(icon7)
        self.Button_select_folder.setIconSize(QSize(38, 38))
        self.splitter.addWidget(self.Button_select_folder)
        self.Button_rtmpStream = QPushButton(self.splitter)
        self.Button_rtmpStream.setObjectName(u"Button_rtmpStream")
        self.Button_rtmpStream.setCursor(QCursor(Qt.OpenHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"D:/huohu/\u6d41\u5a92\u4f53\uff0c\u5a92\u4f53\u5217\u8868-copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_rtmpStream.setIcon(icon8)
        self.Button_rtmpStream.setIconSize(QSize(38, 38))
        self.splitter.addWidget(self.Button_rtmpStream)
        self.frame_conf_box = QFrame(self.frame_left_box)
        self.frame_conf_box.setObjectName(u"frame_conf_box")
        self.frame_conf_box.setGeometry(QRect(10, 320, 281, 81))
        self.frame_conf_box.setStyleSheet(u"QFrame#frame_conf_box{border:2px solid #CFEBD2;\n"
"background:white;\n"
"border-radius:8px;}")
        self.frame_conf_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_conf_box.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_15 = QFrame(self.frame_conf_box)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 0, 281, 41))
        self.frame_15.setStyleSheet(u"border:1px solid #CFEBD2;\n"
"background:#CFEBD2;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0px;")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 10, 51, 21))
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"background:none;\n"
"border:none;")
        self.horizontalSlider_conf = QSlider(self.frame_conf_box)
        self.horizontalSlider_conf.setObjectName(u"horizontalSlider_conf")
        self.horizontalSlider_conf.setGeometry(QRect(110, 50, 141, 22))
        self.horizontalSlider_conf.setStyleSheet(u"QSlider::groove:horizontal {\n"
"            border: none;\n"
"            height: 5px;\n"
"            background-color: lightgray;\n"
"		 border-radius: 5px;\n"
"        }\n"
"\n"
"        QSlider::handle:horizontal {\n"
"            background-color: #2f77cb;\n"
"            width: 8px;\n"
"            margin: -9px 0px -9px 0px;\n"
"            border-radius: 4px;\n"
"        }\n"
"\n"
"        QSlider::sub-page:horizontal {\n"
"            background-color: #4898ec;\n"
"border-radius: 5px;\n"
"        }\n"
"\n"
"\n"
"")
        self.horizontalSlider_conf.setMaximum(100)
        self.horizontalSlider_conf.setPageStep(10)
        self.horizontalSlider_conf.setValue(25)
        self.horizontalSlider_conf.setSliderPosition(25)
        self.horizontalSlider_conf.setOrientation(Qt.Orientation.Horizontal)
        self.doubleSpinBox_conf = QDoubleSpinBox(self.frame_conf_box)
        self.doubleSpinBox_conf.setObjectName(u"doubleSpinBox_conf")
        self.doubleSpinBox_conf.setGeometry(QRect(20, 50, 71, 21))
        self.doubleSpinBox_conf.setMaximum(1.000000000000000)
        self.doubleSpinBox_conf.setSingleStep(0.010000000000000)
        self.doubleSpinBox_conf.setValue(0.250000000000000)
        self.frame_iou_box = QFrame(self.frame_left_box)
        self.frame_iou_box.setObjectName(u"frame_iou_box")
        self.frame_iou_box.setGeometry(QRect(10, 440, 281, 81))
        self.frame_iou_box.setStyleSheet(u"QFrame#frame_iou_box{border:2px solid #CFEBD2;\n"
"background:white;\n"
"border-radius:8px;}")
        self.frame_iou_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_iou_box.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_16 = QFrame(self.frame_iou_box)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, 0, 281, 41))
        self.frame_16.setStyleSheet(u"border:1px solid #CFEBD2;\n"
"background:#CFEBD2;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0px;")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 10, 51, 21))
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"background:none;\n"
"border:none;")
        self.doubleSpinBox_iou = QDoubleSpinBox(self.frame_iou_box)
        self.doubleSpinBox_iou.setObjectName(u"doubleSpinBox_iou")
        self.doubleSpinBox_iou.setGeometry(QRect(20, 50, 71, 21))
        self.doubleSpinBox_iou.setMaximum(1.000000000000000)
        self.doubleSpinBox_iou.setSingleStep(0.010000000000000)
        self.doubleSpinBox_iou.setValue(0.700000000000000)
        self.horizontalSlider_iou = QSlider(self.frame_iou_box)
        self.horizontalSlider_iou.setObjectName(u"horizontalSlider_iou")
        self.horizontalSlider_iou.setGeometry(QRect(120, 50, 141, 22))
        self.horizontalSlider_iou.setStyleSheet(u"QSlider::groove:horizontal {\n"
"            border: none;\n"
"            height: 5px;\n"
"            background-color: lightgray;\n"
"		 border-radius: 5px;\n"
"        }\n"
"\n"
"        QSlider::handle:horizontal {\n"
"            background-color: #2f77cb;\n"
"            width: 8px;\n"
"            margin: -9px 0px -9px 0px;\n"
"            border-radius: 4px;\n"
"        }\n"
"\n"
"        QSlider::sub-page:horizontal {\n"
"            background-color: #4898ec;\n"
"border-radius: 5px;\n"
"        }\n"
"\n"
"\n"
"")
        self.horizontalSlider_iou.setMaximum(100)
        self.horizontalSlider_iou.setPageStep(10)
        self.horizontalSlider_iou.setValue(70)
        self.horizontalSlider_iou.setSliderPosition(70)
        self.horizontalSlider_iou.setOrientation(Qt.Orientation.Horizontal)
        self.frame_raw_box = QFrame(self.centralwidget)
        self.frame_raw_box.setObjectName(u"frame_raw_box")
        self.frame_raw_box.setGeometry(QRect(1170, 80, 271, 161))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_raw_box.sizePolicy().hasHeightForWidth())
        self.frame_raw_box.setSizePolicy(sizePolicy)
        self.frame_raw_box.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.frame_raw_box.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_raw_box.setAutoFillBackground(False)
        self.frame_raw_box.setStyleSheet(u"QFrame#frame_raw_box{\n"
"border:2px solid #6BABFA;}")
        self.frame_raw_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_raw_box.setFrameShadow(QFrame.Shadow.Raised)
        self.label_raw = QLabel(self.frame_raw_box)
        self.label_raw.setObjectName(u"label_raw")
        self.label_raw.setGeometry(QRect(10, 10, 241, 141))
        self.label_raw.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_raw.setAutoFillBackground(False)
        self.label_raw.setStyleSheet(u"")
        self.label_raw.setPixmap(QPixmap(u"icon/background-min.png"))
        self.label_raw.setScaledContents(False)
        self.label_raw.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_raw.setMargin(0)
        self.frame_result_box = QFrame(self.centralwidget)
        self.frame_result_box.setObjectName(u"frame_result_box")
        self.frame_result_box.setGeometry(QRect(310, 80, 851, 581))
        self.frame_result_box.setStyleSheet(u"QFrame#frame_result_box{\n"
"border:2px solid #6BABFA;\n"
"}")
        self.frame_result_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_result_box.setFrameShadow(QFrame.Shadow.Raised)
        self.label_result = QLabel(self.frame_result_box)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(8, 8, 831, 541))
        self.label_result.setStyleSheet(u"")
        self.label_result.setPixmap(QPixmap(u"icon/background.png"))
        self.label_result.setScaledContents(False)
        self.label_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_result_box_2 = QFrame(self.centralwidget)
        self.frame_result_box_2.setObjectName(u"frame_result_box_2")
        self.frame_result_box_2.setGeometry(QRect(1170, 250, 271, 451))
        self.frame_result_box_2.setStyleSheet(u"QFrame#frame_result_box_2{\n"
"border:1px solid skyblue;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0px;}")
        self.frame_result_box_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_result_box_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_12 = QFrame(self.frame_result_box_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 0, 271, 41))
        self.frame_12.setStyleSheet(u"border:1px solid #6BABFA;\n"
"background:#6BABFA;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0px;")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 10, 91, 21))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"background:none;\n"
"border:none;\n"
"color:white;")
        self.frame_6 = QFrame(self.frame_result_box_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 60, 261, 51))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_detect_num = QLabel(self.frame_6)
        self.label_detect_num.setObjectName(u"label_detect_num")
        self.label_detect_num.setGeometry(QRect(170, 0, 81, 51))
        font6 = QFont()
        font6.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font6.setPointSize(20)
        font6.setStyleStrategy(QFont.PreferDefault)
        self.label_detect_num.setFont(font6)
        self.label_detect_num.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_detect_num.setAutoFillBackground(False)
        self.label_detect_num.setStyleSheet(u"background:#6882FA;\n"
"color:black;\n"
"padding-left:5px;")
        self.label_detect_num.setTextFormat(Qt.TextFormat.RichText)
        self.label_detect_num.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_detect_num.setIndent(-1)
        self.label_speed_3 = QLabel(self.frame_6)
        self.label_speed_3.setObjectName(u"label_speed_3")
        self.label_speed_3.setGeometry(QRect(0, 0, 171, 51))
        font7 = QFont()
        font7.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font7.setPointSize(16)
        font7.setStyleStrategy(QFont.PreferDefault)
        self.label_speed_3.setFont(font7)
        self.label_speed_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_speed_3.setAutoFillBackground(False)
        self.label_speed_3.setStyleSheet(u"background:#6BABFA;\n"
"color:white;\n"
"padding-left:5px;")
        self.label_speed_3.setIndent(-1)
        self.frame_2 = QFrame(self.frame_result_box_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 120, 261, 51))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_speed = QLabel(self.frame_2)
        self.label_speed.setObjectName(u"label_speed")
        self.label_speed.setGeometry(QRect(170, 0, 81, 51))
        font8 = QFont()
        font8.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font8.setPointSize(15)
        font8.setStyleStrategy(QFont.PreferDefault)
        self.label_speed.setFont(font8)
        self.label_speed.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_speed.setAutoFillBackground(False)
        self.label_speed.setStyleSheet(u"background:#6882FA;\n"
"color:black;")
        self.label_speed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_speed.setIndent(-1)
        self.label_speed_4 = QLabel(self.frame_2)
        self.label_speed_4.setObjectName(u"label_speed_4")
        self.label_speed_4.setGeometry(QRect(0, 0, 171, 51))
        self.label_speed_4.setFont(font7)
        self.label_speed_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_speed_4.setAutoFillBackground(False)
        self.label_speed_4.setStyleSheet(u"background:#6BABFA;\n"
"color:white;\n"
"padding-left:5px;")
        self.label_speed_4.setIndent(-1)
        self.result_info = QTextBrowser(self.frame_result_box_2)
        self.result_info.setObjectName(u"result_info")
        self.result_info.setGeometry(QRect(5, 180, 261, 261))
        font9 = QFont()
        font9.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font9.setPointSize(12)
        self.result_info.setFont(font9)
        self.result_info.setStyleSheet(u"background:#e8e8e8;\n"
"color:black;\n"
"border:none;\n"
"border-radius:5px")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6853\u5065\u79d1\u6280\u76ee\u6807\u68c0\u6d4b\u53ef\u89c6\u5316\u7cfb\u7edf", None))
#if QT_CONFIG(tooltip)
        self.pushButton_bofang.setToolTip(QCoreApplication.translate("MainWindow", u"\u6682\u505c/\u5f00\u542f\u68c0\u6d4b", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_bofang.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_stop.setToolTip(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u68c0\u6d4b", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_stop.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u6853\u5065\u79d1\u6280\u76ee\u6807\u68c0\u6d4b\u7cfb\u7edf", None))
#if QT_CONFIG(tooltip)
        self.checkBox_isSave.setToolTip(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u4fdd\u5b58\u5728\u5f53\u524d\u76ee\u5f55runs\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_isSave.setText("")
#if QT_CONFIG(tooltip)
        self.label_isSava.setToolTip(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u4fdd\u5b58\u5728\u5f53\u524d\u76ee\u5f55runs\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.label_isSava.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u4fdd\u5b58\u7ed3\u679c\uff1a", None))
        self.line_weights.setInputMask("")
        self.line_weights.setText(QCoreApplication.translate("MainWindow", u"yolov9-c.pt", None))
        self.line_weights.setPlaceholderText("")
        self.Button_select_w_p.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6743\u91cd", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u68c0\u6d4b\u8d44\u6e90", None))
#if QT_CONFIG(tooltip)
        self.Button_checkImg.setToolTip(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u5355\u5f20\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.Button_checkImg.setText("")
#if QT_CONFIG(tooltip)
        self.Button_checkVideo.setToolTip(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u89c6\u9891\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.Button_checkVideo.setText("")
#if QT_CONFIG(tooltip)
        self.Button_openCamera.setToolTip(QCoreApplication.translate("MainWindow", u"\u5f00\u542f/\u5173\u95ed\u6444\u50cf\u5934", None))
#endif // QT_CONFIG(tooltip)
        self.Button_openCamera.setText("")
#if QT_CONFIG(tooltip)
        self.Button_select_folder.setToolTip(QCoreApplication.translate("MainWindow", u"\u591a\u56fe\uff08\u6587\u4ef6\u5939\u68c0\u6d4b\uff09", None))
#endif // QT_CONFIG(tooltip)
        self.Button_select_folder.setText("")
        self.Button_rtmpStream.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"conf", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"IOU", None))
        self.label_raw.setText("")
        self.label_result.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.label_detect_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_speed_3.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u5230\u7684\u76ee\u6807\u6570\uff1a", None))
        self.label_speed.setText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.label_speed_4.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7528\u65f6(ms)\uff1a", None))
#if QT_CONFIG(tooltip)
        self.result_info.setToolTip(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7684\u7ed3\u679c\u5c55\u793a\u7a97\u53e3", None))
#endif // QT_CONFIG(tooltip)
        self.result_info.setPlaceholderText("")
    # retranslateUi

