from PyQt5 import QtCore, QtGui, QtWidgets
from ca_algorithm import CellularAutomata


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1067, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_settings = QtWidgets.QFormLayout()
        self.formLayout_settings.setObjectName("formLayout_settings")
        self.label_neighbours_rule = QtWidgets.QLabel(self.centralwidget)
        self.label_neighbours_rule.setObjectName("label_neighbours_rule")
        self.formLayout_settings.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_neighbours_rule)
        self.comboBox_neighbours_rule = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_neighbours_rule.setObjectName("comboBox_neighbours_rule")
        self.comboBox_neighbours_rule.addItem("")
        self.comboBox_neighbours_rule.addItem("")
        self.formLayout_settings.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_neighbours_rule)
        self.label_border_condition = QtWidgets.QLabel(self.centralwidget)
        self.label_border_condition.setObjectName("label_border_condition")
        self.formLayout_settings.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_border_condition)
        self.comboBox_border_condition = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_border_condition.setObjectName("comboBox_border_condition")
        self.comboBox_border_condition.addItem("")
        self.comboBox_border_condition.addItem("")
        self.formLayout_settings.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_border_condition)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_settings.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout_settings.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_size_of_space = QtWidgets.QLabel(self.centralwidget)
        self.label_size_of_space.setObjectName("label_size_of_space")
        self.formLayout_settings.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_size_of_space)
        self.lineEdit_size_of_space = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_size_of_space.setObjectName("lineEdit_size_of_space")
        self.formLayout_settings.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_size_of_space)
        self.label_number_of_grains = QtWidgets.QLabel(self.centralwidget)
        self.label_number_of_grains.setObjectName("label_number_of_grains")
        self.formLayout_settings.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_number_of_grains)
        self.lineEdit_number_of_grains = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_number_of_grains.setObjectName("lineEdit_number_of_grains")
        self.formLayout_settings.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_number_of_grains)
        self.label_inclusions_number = QtWidgets.QLabel(self.centralwidget)
        self.label_inclusions_number.setObjectName("label_inclusions_number")
        self.formLayout_settings.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_inclusions_number)
        self.lineEdit_inclusions_number = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_inclusions_number.setObjectName("lineEdit_inclusions_number")
        self.formLayout_settings.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inclusions_number)
        self.label_min_radius = QtWidgets.QLabel(self.centralwidget)
        self.label_min_radius.setObjectName("label_min_radius")
        self.formLayout_settings.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_min_radius)
        self.lineEdit_min_radius = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_min_radius.setObjectName("lineEdit_min_radius")
        self.formLayout_settings.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_min_radius)
        self.label_max_radius = QtWidgets.QLabel(self.centralwidget)
        self.label_max_radius.setObjectName("label_max_radius")
        self.formLayout_settings.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_max_radius)
        self.lineEdit_max_radius = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_max_radius.setObjectName("lineEdit_max_radius")
        self.formLayout_settings.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_max_radius)
        self.radioButton_gbc_feature = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_gbc_feature.setObjectName("radioButton_gbc_feature")
        self.formLayout_settings.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.radioButton_gbc_feature)
        self.lineEdit_prob_threshold = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_prob_threshold.setObjectName("lineEdit_prob_threshold")
        self.formLayout_settings.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_prob_threshold)
        self.pushButton_delete_grains = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete_grains.setObjectName("pushButton_delete_grains")
        self.formLayout_settings.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.pushButton_delete_grains)
        self.comboBox_list_of_grains = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_list_of_grains.setObjectName("comboBox_list_of_grains")
        self.formLayout_settings.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.comboBox_list_of_grains)
        self.pushButton_import_from_csv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_import_from_csv.setObjectName("pushButton_import_from_csv")
        self.formLayout_settings.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.pushButton_import_from_csv)
        self.lineEdit_import_from_csv = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_import_from_csv.setObjectName("lineEdit_import_from_csv")
        self.formLayout_settings.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_import_from_csv)
        self.pushButton_export_to_csv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export_to_csv.setObjectName("pushButton_export_to_csv")
        self.formLayout_settings.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.pushButton_export_to_csv)
        self.pushButton_export_to_png = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export_to_png.setObjectName("pushButton_export_to_png")
        self.formLayout_settings.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.pushButton_export_to_png)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_settings.setWidget(14, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.pushButton_init_space = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_init_space.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_init_space.setObjectName("pushButton_init_space")
        self.formLayout_settings.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.pushButton_init_space)
        self.pushButton_start_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_stop.setObjectName("pushButton_2")
        self.formLayout_settings.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.pushButton_start_stop)
        self.pushButton_step = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_step.setObjectName("pushButton_3")
        self.formLayout_settings.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.pushButton_step)
        self.pushButton_clear_space = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear_space.setObjectName("pushButton_4")
        self.formLayout_settings.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.pushButton_clear_space)
        self.horizontalLayout.addLayout(self.formLayout_settings)

        self.line_vertical = QtWidgets.QFrame(self.centralwidget)
        self.line_vertical.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_vertical.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertical.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_vertical)

        self.label_pixmap = QtWidgets.QLabel(self.centralwidget)
        self.label_pixmap.setMinimumSize(QtCore.QSize(500, 500))
        self.label_pixmap.setMaximumSize(QtCore.QSize(500, 500))
        self.label_pixmap.setScaledContents(True)
        self.label_pixmap.setPixmap(QtGui.QPixmap("image.png"))
        self.label_pixmap.setText("")
        self.label_pixmap.setObjectName("label_pixmap")
        self.horizontalLayout.addWidget(self.label_pixmap)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1067, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_neighbours_rule.setText(_translate("MainWindow", "Neighbours rule"))
        self.comboBox_neighbours_rule.setItemText(0, _translate("MainWindow", "VONNEUMANN"))
        self.comboBox_neighbours_rule.setItemText(1, _translate("MainWindow", "MOORE"))
        self.label_border_condition.setText(_translate("MainWindow", "Border rule"))
        self.comboBox_border_condition.setItemText(0, _translate("MainWindow", "ABSORBING"))
        self.comboBox_border_condition.setItemText(1, _translate("MainWindow", "SNAKELIKE"))
        self.label_4.setText(_translate("MainWindow", "empty"))
        self.label_size_of_space.setText(_translate("MainWindow", "Size of space"))
        self.lineEdit_size_of_space.setText(_translate("MainWindow", "50"))
        self.label_number_of_grains.setText(_translate("MainWindow", "Number of grains"))
        self.lineEdit_number_of_grains.setText(_translate("MainWindow", "10"))
        self.label_inclusions_number.setText(_translate("MainWindow", "Number of incl."))
        self.lineEdit_inclusions_number.setText(_translate("MainWindow", "3"))
        self.label_min_radius.setText(_translate("MainWindow", "Min radius"))
        self.lineEdit_min_radius.setText(_translate("MainWindow", "0.5"))
        self.label_max_radius.setText(_translate("MainWindow", "Min radius"))
        self.lineEdit_max_radius.setText(_translate("MainWindow", "1.5"))
        self.radioButton_gbc_feature.setText(_translate("MainWindow", "GBC feature"))
        self.lineEdit_prob_threshold.setText(_translate("MainWindow", "Probability threshold [0-1]"))
        self.pushButton_delete_grains.setText(_translate("MainWindow", "Delete grains"))
        self.pushButton_import_from_csv.setText(_translate("MainWindow", "Import csv"))
        self.lineEdit_import_from_csv.setText(_translate("MainWindow", "Path to csv"))
        self.pushButton_export_to_csv.setText(_translate("MainWindow", "Export csv"))
        self.pushButton_export_to_png.setText(_translate("MainWindow", "Export png"))
        self.pushButton_init_space.setText(_translate("MainWindow", "Init space"))
        self.pushButton_start_stop.setText(_translate("MainWindow", "Start/Stop"))
        self.pushButton_step.setText(_translate("MainWindow", "Step"))
        self.pushButton_clear_space.setText(_translate("MainWindow", "Clear space"))

    # def init_ca_algo(self):
    #     self._ca_algo = CellularAutomata(int(self.lineEdit_number_of_grains.text()),
    #                                      int(self.lineEdit_size_of_space.text()),
    #                                      int(self.lineEdit_size_of_space.text()),
    #                                      str(self.comboBox_border_condition.currentText()),
    #                                      str(self.comboBox_neighbours_rule.currentText()))
    #     self._ca_algo.add_random()
    #     # display an image with the current state
    #
    # def _init_image_timer(self):
    #     self._number_of_clicked += 1
    #     if self._number_of_clicked % 2:
    #         self._timer.timeout.connect(self._update_func)
    #         self._timer.start(50)
    #     else:
    #         self._timer.stop()
    #
    # def _update_func(self):
    #     if self._ca_algo.cell_empty in self._ca_algo.space:
    #         self._ca_algo.one_step()
    #     # display an image with the current state
    #
    # def _clear_space(self):
    #     self._timer.stop()
    #     self._ca_algo.space = self._ca_algo.space_clear
    #     # clear the image
    #
    # def _one_step(self):
    #     self._timer.stop()
    #     self._ca_algo.one_step()
    #     # display an image with the current state


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
