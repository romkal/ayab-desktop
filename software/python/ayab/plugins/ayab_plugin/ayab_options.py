# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ayab_options.ui'
#
# Created: Thu Jan 26 21:52:05 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(240, 581)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DockWidget.sizePolicy().hasHeightForWidth())
        DockWidget.setSizePolicy(sizePolicy)
        DockWidget.setMinimumSize(QtCore.QSize(240, 581))
        DockWidget.setMaximumSize(QtCore.QSize(240, 581))
        DockWidget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        DockWidget.setWindowTitle("")
        self.ayab_config = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ayab_config.sizePolicy().hasHeightForWidth())
        self.ayab_config.setSizePolicy(sizePolicy)
        self.ayab_config.setObjectName("ayab_config")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ayab_config)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.ayab_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(220, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(0, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.serial_port_dropdown = QtWidgets.QComboBox(self.groupBox)
        self.serial_port_dropdown.setObjectName("serial_port_dropdown")
        self.horizontalLayout_3.addWidget(self.serial_port_dropdown)
        self.refresh_ports_button = QtWidgets.QPushButton(self.groupBox)
        self.refresh_ports_button.setObjectName("refresh_ports_button")
        self.horizontalLayout_3.addWidget(self.refresh_ports_button)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget = QtWidgets.QTabWidget(self.ayab_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(180, 430))
        self.tabWidget.setMaximumSize(QtCore.QSize(1000000, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_knit = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_knit.sizePolicy().hasHeightForWidth())
        self.tab_knit.setSizePolicy(sizePolicy)
        self.tab_knit.setObjectName("tab_knit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_knit)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 221, 402))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.color_edit = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_edit.sizePolicy().hasHeightForWidth())
        self.color_edit.setSizePolicy(sizePolicy)
        self.color_edit.setMinimum(2)
        self.color_edit.setMaximum(6)
        self.color_edit.setObjectName("color_edit")
        self.verticalLayout_3.addWidget(self.color_edit)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.start_line_edit = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_line_edit.sizePolicy().hasHeightForWidth())
        self.start_line_edit.setSizePolicy(sizePolicy)
        self.start_line_edit.setSuffix("")
        self.start_line_edit.setMinimum(0)
        self.start_line_edit.setMaximum(256)
        self.start_line_edit.setObjectName("start_line_edit")
        self.verticalLayout_3.addWidget(self.start_line_edit)
        self.infRepeat_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infRepeat_checkbox.sizePolicy().hasHeightForWidth())
        self.infRepeat_checkbox.setSizePolicy(sizePolicy)
        self.infRepeat_checkbox.setObjectName("infRepeat_checkbox")
        self.verticalLayout_3.addWidget(self.infRepeat_checkbox)
        self.gbox_startneedle = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.gbox_startneedle.setMinimumSize(QtCore.QSize(0, 60))
        self.gbox_startneedle.setObjectName("gbox_startneedle")
        self.start_needle_color = QtWidgets.QComboBox(self.gbox_startneedle)
        self.start_needle_color.setGeometry(QtCore.QRect(60, 20, 81, 31))
        self.start_needle_color.setObjectName("start_needle_color")
        self.start_needle_color.addItem("")
        self.start_needle_color.addItem("")
        self.start_needle_edit = QtWidgets.QSpinBox(self.gbox_startneedle)
        self.start_needle_edit.setGeometry(QtCore.QRect(10, 20, 51, 31))
        self.start_needle_edit.setPrefix("")
        self.start_needle_edit.setMinimum(1)
        self.start_needle_edit.setMaximum(100)
        self.start_needle_edit.setProperty("value", 20)
        self.start_needle_edit.setObjectName("start_needle_edit")
        self.verticalLayout_3.addWidget(self.gbox_startneedle)
        self.gbox_stopneedle = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.gbox_stopneedle.setMinimumSize(QtCore.QSize(0, 60))
        self.gbox_stopneedle.setObjectName("gbox_stopneedle")
        self.stop_needle_color = QtWidgets.QComboBox(self.gbox_stopneedle)
        self.stop_needle_color.setGeometry(QtCore.QRect(60, 20, 81, 31))
        self.stop_needle_color.setObjectName("stop_needle_color")
        self.stop_needle_color.addItem("")
        self.stop_needle_color.addItem("")
        self.stop_needle_edit = QtWidgets.QSpinBox(self.gbox_stopneedle)
        self.stop_needle_edit.setGeometry(QtCore.QRect(10, 20, 51, 31))
        self.stop_needle_edit.setPrefix("")
        self.stop_needle_edit.setMinimum(1)
        self.stop_needle_edit.setMaximum(100)
        self.stop_needle_edit.setProperty("value", 20)
        self.stop_needle_edit.setObjectName("stop_needle_edit")
        self.verticalLayout_3.addWidget(self.gbox_stopneedle)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.machine_type_box = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_type_box.sizePolicy().hasHeightForWidth())
        self.machine_type_box.setSizePolicy(sizePolicy)
        self.machine_type_box.setObjectName("machine_type_box")
        self.machine_type_box.addItem("")
        self.machine_type_box.addItem("")
        self.machine_type_box.addItem("")
        self.verticalLayout_3.addWidget(self.machine_type_box)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.alignment_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alignment_combo_box.sizePolicy().hasHeightForWidth())
        self.alignment_combo_box.setSizePolicy(sizePolicy)
        self.alignment_combo_box.setObjectName("alignment_combo_box")
        self.alignment_combo_box.addItem("")
        self.alignment_combo_box.addItem("")
        self.alignment_combo_box.addItem("")
        self.verticalLayout_3.addWidget(self.alignment_combo_box)
        self.tabWidget.addTab(self.tab_knit, "")
        self.tab_test = QtWidgets.QWidget()
        self.tab_test.setObjectName("tab_test")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_test)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, -1, 211, 184))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.progress_hall_l = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progress_hall_l.setEnabled(False)
        self.progress_hall_l.setMaximum(1024)
        self.progress_hall_l.setProperty("value", 0)
        self.progress_hall_l.setObjectName("progress_hall_l")
        self.verticalLayout_4.addWidget(self.progress_hall_l)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.progress_hall_r = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progress_hall_r.setEnabled(False)
        self.progress_hall_r.setMaximum(1024)
        self.progress_hall_r.setProperty("value", 0)
        self.progress_hall_r.setObjectName("progress_hall_r")
        self.verticalLayout_4.addWidget(self.progress_hall_r)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.slider_position = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.slider_position.setEnabled(False)
        self.slider_position.setMaximum(199)
        self.slider_position.setOrientation(QtCore.Qt.Horizontal)
        self.slider_position.setObjectName("slider_position")
        self.verticalLayout_4.addWidget(self.slider_position)
        self.label_carriage = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_carriage.setObjectName("label_carriage")
        self.verticalLayout_4.addWidget(self.label_carriage)
        self.tabWidget.addTab(self.tab_test, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.configure_button = QtWidgets.QPushButton(self.ayab_config)
        self.configure_button.setObjectName("configure_button")
        self.verticalLayout.addWidget(self.configure_button)
        DockWidget.setWidget(self.ayab_config)

        self.retranslateUi(DockWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("DockWidget", "Port Selection"))
        self.refresh_ports_button.setText(_translate("DockWidget", "Refresh"))
        self.label_6.setText(_translate("DockWidget", "Colors"))
        self.label_5.setText(_translate("DockWidget", "Start Line"))
        self.start_line_edit.setPrefix(_translate("DockWidget", "line "))
        self.infRepeat_checkbox.setText(_translate("DockWidget", "Infinite Repeat"))
        self.gbox_startneedle.setTitle(_translate("DockWidget", "Start Needle"))
        self.start_needle_color.setItemText(0, _translate("DockWidget", "orange"))
        self.start_needle_color.setItemText(1, _translate("DockWidget", "green"))
        self.gbox_stopneedle.setTitle(_translate("DockWidget", "Stop Needle"))
        self.stop_needle_color.setItemText(0, _translate("DockWidget", "green"))
        self.stop_needle_color.setItemText(1, _translate("DockWidget", "orange"))
        self.label_4.setText(_translate("DockWidget", "Machine Type"))
        self.machine_type_box.setItemText(0, _translate("DockWidget", "single"))
        self.machine_type_box.setItemText(1, _translate("DockWidget", "ribber"))
        self.machine_type_box.setItemText(2, _translate("DockWidget", "circular"))
        self.label_3.setText(_translate("DockWidget", "Alignment"))
        self.alignment_combo_box.setItemText(0, _translate("DockWidget", "center"))
        self.alignment_combo_box.setItemText(1, _translate("DockWidget", "left"))
        self.alignment_combo_box.setItemText(2, _translate("DockWidget", "right"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_knit), _translate("DockWidget", "Knit"))
        self.label.setText(_translate("DockWidget", "Hall Left"))
        self.progress_hall_l.setFormat(_translate("DockWidget", "%p%"))
        self.label_2.setText(_translate("DockWidget", "Hall Right"))
        self.progress_hall_r.setFormat(_translate("DockWidget", "%p%"))
        self.label_7.setText(_translate("DockWidget", "Position"))
        self.label_carriage.setText(_translate("DockWidget", "No carriage detected"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_test), _translate("DockWidget", "Test"))
        self.configure_button.setText(_translate("DockWidget", "2. Configure"))

