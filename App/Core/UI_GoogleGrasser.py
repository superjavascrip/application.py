# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_GoogleGrasser.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_application(object):
    def setupUi(self, application):
        if not application.objectName():
            application.setObjectName(u"application")
        application.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"res/application-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        application.setWindowIcon(icon)
        self.content_window = QWidget(application)
        self.content_window.setObjectName(u"content_window")
        self.gridLayout_2 = QGridLayout(self.content_window)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabs = QTabWidget(self.content_window)
        self.tabs.setObjectName(u"tabs")
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.main_tab.setMaximumSize(QSize(783, 16777215))
        self.gridLayout_4 = QGridLayout(self.main_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.grass_content_layout = QHBoxLayout()
        self.grass_content_layout.setObjectName(u"grass_content_layout")
        self.original_text_edit = QPlainTextEdit(self.main_tab)
        self.original_text_edit.setObjectName(u"original_text_edit")
        self.original_text_edit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.grass_content_layout.addWidget(self.original_text_edit)

        self.grass_result_browser = QTextBrowser(self.main_tab)
        self.grass_result_browser.setObjectName(u"grass_result_browser")
        self.grass_result_browser.setOpenLinks(False)

        self.grass_content_layout.addWidget(self.grass_result_browser)


        self.gridLayout_4.addLayout(self.grass_content_layout, 1, 2, 1, 2)

        self.grass_option_push_buttons = QHBoxLayout()
        self.grass_option_push_buttons.setObjectName(u"grass_option_push_buttons")
        self.open_file = QPushButton(self.main_tab)
        self.open_file.setObjectName(u"open_file")

        self.grass_option_push_buttons.addWidget(self.open_file)

        self.start_grass = QPushButton(self.main_tab)
        self.start_grass.setObjectName(u"start_grass")

        self.grass_option_push_buttons.addWidget(self.start_grass)


        self.gridLayout_4.addLayout(self.grass_option_push_buttons, 3, 2, 1, 1)

        self.grass_option = QGridLayout()
        self.grass_option.setObjectName(u"grass_option")
        self.use_config_prompt_label = QLabel(self.main_tab)
        self.use_config_prompt_label.setObjectName(u"use_config_prompt_label")

        self.grass_option.addWidget(self.use_config_prompt_label, 0, 0, 1, 1)

        self.select_config = QComboBox(self.main_tab)
        self.select_config.setObjectName(u"select_config")

        self.grass_option.addWidget(self.select_config, 1, 0, 1, 1)

        self.grass_frequency_prompt_label = QLabel(self.main_tab)
        self.grass_frequency_prompt_label.setObjectName(u"grass_frequency_prompt_label")

        self.grass_option.addWidget(self.grass_frequency_prompt_label, 0, 1, 1, 1)

        self.grass_frequency = QSpinBox(self.main_tab)
        self.grass_frequency.setObjectName(u"grass_frequency")
        self.grass_frequency.setCursor(QCursor(Qt.ArrowCursor))
        self.grass_frequency.setMinimum(1)
        self.grass_frequency.setMaximum(1000000)

        self.grass_option.addWidget(self.grass_frequency, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.grass_option, 2, 2, 1, 1)

        self.second_grid_layout = QGridLayout()
        self.second_grid_layout.setObjectName(u"second_grid_layout")
        self.save_result = QPushButton(self.main_tab)
        self.save_result.setObjectName(u"save_result")

        self.second_grid_layout.addWidget(self.save_result, 3, 0, 1, 1)

        self.output_google_voice = QPushButton(self.main_tab)
        self.output_google_voice.setObjectName(u"output_google_voice")

        self.second_grid_layout.addWidget(self.output_google_voice, 3, 1, 1, 1)

        self.save_this_grass_as_config = QPushButton(self.main_tab)
        self.save_this_grass_as_config.setObjectName(u"save_this_grass_as_config")

        self.second_grid_layout.addWidget(self.save_this_grass_as_config, 2, 1, 1, 1)

        self.copy_result = QPushButton(self.main_tab)
        self.copy_result.setObjectName(u"copy_result")

        self.second_grid_layout.addWidget(self.copy_result, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.second_grid_layout, 2, 3, 2, 1)

        self.tabs.addTab(self.main_tab, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.gridLayout = QGridLayout(self.settings_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.second_setting_option = QHBoxLayout()
        self.second_setting_option.setObjectName(u"second_setting_option")
        self.second_setting_option_prompt = QLabel(self.settings_tab)
        self.second_setting_option_prompt.setObjectName(u"second_setting_option_prompt")

        self.second_setting_option.addWidget(self.second_setting_option_prompt)

        self.radio_first_setting_option = QRadioButton(self.settings_tab)
        self.second_setting_option_button_group = QButtonGroup(application)
        self.second_setting_option_button_group.setObjectName(u"second_setting_option_button_group")
        self.second_setting_option_button_group.addButton(self.radio_first_setting_option)
        self.radio_first_setting_option.setObjectName(u"radio_first_setting_option")
        self.radio_first_setting_option.setChecked(True)

        self.second_setting_option.addWidget(self.radio_first_setting_option)

        self.radio_second_setting_option = QRadioButton(self.settings_tab)
        self.second_setting_option_button_group.addButton(self.radio_second_setting_option)
        self.radio_second_setting_option.setObjectName(u"radio_second_setting_option")
        self.radio_second_setting_option.setChecked(False)

        self.second_setting_option.addWidget(self.radio_second_setting_option)


        self.gridLayout.addLayout(self.second_setting_option, 4, 0, 1, 1)

        self.first_setting_option = QHBoxLayout()
        self.first_setting_option.setObjectName(u"first_setting_option")
        self.first_settings_option_prompt = QLabel(self.settings_tab)
        self.first_settings_option_prompt.setObjectName(u"first_settings_option_prompt")

        self.first_setting_option.addWidget(self.first_settings_option_prompt)

        self.select_google_translate_url = QComboBox(self.settings_tab)
        self.select_google_translate_url.setObjectName(u"select_google_translate_url")

        self.first_setting_option.addWidget(self.select_google_translate_url)


        self.gridLayout.addLayout(self.first_setting_option, 0, 0, 1, 1)

        self.third_setting_option = QHBoxLayout()
        self.third_setting_option.setObjectName(u"third_setting_option")
        self.third_setting_option_prompt = QLabel(self.settings_tab)
        self.third_setting_option_prompt.setObjectName(u"third_setting_option_prompt")

        self.third_setting_option.addWidget(self.third_setting_option_prompt)

        self.set_config_file_name = QLineEdit(self.settings_tab)
        self.set_config_file_name.setObjectName(u"set_config_file_name")

        self.third_setting_option.addWidget(self.set_config_file_name)


        self.gridLayout.addLayout(self.third_setting_option, 2, 0, 1, 1)

        self.fourth_setting_option = QHBoxLayout()
        self.fourth_setting_option.setObjectName(u"fourth_setting_option")
        self.fourth_setting_option_prompt_2 = QLabel(self.settings_tab)
        self.fourth_setting_option_prompt_2.setObjectName(u"fourth_setting_option_prompt_2")

        self.fourth_setting_option.addWidget(self.fourth_setting_option_prompt_2)

        self.select_application_style = QComboBox(self.settings_tab)
        self.select_application_style.setObjectName(u"select_application_style")

        self.fourth_setting_option.addWidget(self.select_application_style)


        self.gridLayout.addLayout(self.fourth_setting_option, 3, 0, 1, 1)

        self.fifth_setting_option = QHBoxLayout()
        self.fifth_setting_option.setObjectName(u"fifth_setting_option")
        self.fifth_setting_option_prompt = QLabel(self.settings_tab)
        self.fifth_setting_option_prompt.setObjectName(u"fifth_setting_option_prompt")

        self.fifth_setting_option.addWidget(self.fifth_setting_option_prompt)

        self.select_application_qss = QComboBox(self.settings_tab)
        self.select_application_qss.setObjectName(u"select_application_qss")

        self.fifth_setting_option.addWidget(self.select_application_qss)


        self.gridLayout.addLayout(self.fifth_setting_option, 5, 0, 1, 1)

        self.tabs.addTab(self.settings_tab, "")
        self.config_tab = QWidget()
        self.config_tab.setObjectName(u"config_tab")
        self.gridLayout_8 = QGridLayout(self.config_tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.all_config = QTreeWidget(self.config_tab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.all_config.setHeaderItem(__qtreewidgetitem)
        self.all_config.setObjectName(u"all_config")

        self.gridLayout_8.addWidget(self.all_config, 1, 0, 1, 1)

        self.config_tab_button_group = QVBoxLayout()
        self.config_tab_button_group.setObjectName(u"config_tab_button_group")
        self.add_language = QPushButton(self.config_tab)
        self.add_language.setObjectName(u"add_language")

        self.config_tab_button_group.addWidget(self.add_language)

        self.add_random_language = QPushButton(self.config_tab)
        self.add_random_language.setObjectName(u"add_random_language")

        self.config_tab_button_group.addWidget(self.add_random_language)

        self.delete_config_and_language = QPushButton(self.config_tab)
        self.delete_config_and_language.setObjectName(u"delete_config_and_language")

        self.config_tab_button_group.addWidget(self.delete_config_and_language)

        self.add_config = QPushButton(self.config_tab)
        self.add_config.setObjectName(u"add_config")

        self.config_tab_button_group.addWidget(self.add_config)

        self.add_random_config = QPushButton(self.config_tab)
        self.add_random_config.setObjectName(u"add_random_config")

        self.config_tab_button_group.addWidget(self.add_random_config)

        self.import_config = QPushButton(self.config_tab)
        self.import_config.setObjectName(u"import_config")

        self.config_tab_button_group.addWidget(self.import_config)

        self.export_config = QPushButton(self.config_tab)
        self.export_config.setObjectName(u"export_config")

        self.config_tab_button_group.addWidget(self.export_config)


        self.gridLayout_8.addLayout(self.config_tab_button_group, 1, 1, 1, 1)

        self.all_config_prompt = QLabel(self.config_tab)
        self.all_config_prompt.setObjectName(u"all_config_prompt")

        self.gridLayout_8.addWidget(self.all_config_prompt, 0, 0, 1, 1)

        self.tabs.addTab(self.config_tab, "")
        self.about_tab = QWidget()
        self.about_tab.setObjectName(u"about_tab")
        self.gridLayout_6 = QGridLayout(self.about_tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.about_text_browser = QTextBrowser(self.about_tab)
        self.about_text_browser.setObjectName(u"about_text_browser")
        self.about_text_browser.setOpenExternalLinks(True)
        self.about_text_browser.setOpenLinks(False)

        self.gridLayout_6.addWidget(self.about_text_browser, 0, 0, 1, 1)

        self.tabs.addTab(self.about_tab, "")

        self.gridLayout_2.addWidget(self.tabs, 0, 0, 1, 1)

        application.setCentralWidget(self.content_window)
        self.statusbar = QStatusBar(application)
        self.statusbar.setObjectName(u"statusbar")
        application.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.original_text_edit, self.select_config)
        QWidget.setTabOrder(self.select_config, self.open_file)
        QWidget.setTabOrder(self.open_file, self.grass_frequency)
        QWidget.setTabOrder(self.grass_frequency, self.start_grass)
        QWidget.setTabOrder(self.start_grass, self.copy_result)
        QWidget.setTabOrder(self.copy_result, self.save_result)
        QWidget.setTabOrder(self.save_result, self.save_this_grass_as_config)
        QWidget.setTabOrder(self.save_this_grass_as_config, self.output_google_voice)
        QWidget.setTabOrder(self.output_google_voice, self.select_google_translate_url)
        QWidget.setTabOrder(self.select_google_translate_url, self.set_config_file_name)
        QWidget.setTabOrder(self.set_config_file_name, self.select_application_style)
        QWidget.setTabOrder(self.select_application_style, self.add_language)
        QWidget.setTabOrder(self.add_language, self.add_random_language)
        QWidget.setTabOrder(self.add_random_language, self.delete_config_and_language)
        QWidget.setTabOrder(self.delete_config_and_language, self.add_config)
        QWidget.setTabOrder(self.add_config, self.add_random_config)
        QWidget.setTabOrder(self.add_random_config, self.import_config)
        QWidget.setTabOrder(self.import_config, self.export_config)
        QWidget.setTabOrder(self.export_config, self.all_config)
        QWidget.setTabOrder(self.all_config, self.grass_result_browser)

        self.retranslateUi(application)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(application)
    # setupUi

    def retranslateUi(self, application):
        application.setWindowTitle(QCoreApplication.translate("application", u"GoogleGrasser", None))
        self.open_file.setText(QCoreApplication.translate("application", u"\u6253\u5f00\u6587\u4ef6", None))
        self.start_grass.setText(QCoreApplication.translate("application", u"\u5f00\u59cb\u751f\u8349", None))
        self.use_config_prompt_label.setText(QCoreApplication.translate("application", u"\u4f7f\u7528\u7684\u914d\u7f6e:", None))
        self.grass_frequency_prompt_label.setText(QCoreApplication.translate("application", u"\u751f\u8349\u7684\u6b21\u6570:", None))
        self.save_result.setText(QCoreApplication.translate("application", u"\u4fdd\u5b58\u7ed3\u679c", None))
        self.output_google_voice.setText(QCoreApplication.translate("application", u"\u5bfc\u51fa\u8c37\u6b4c\u8bed\u97f3", None))
        self.save_this_grass_as_config.setText(QCoreApplication.translate("application", u"\u5c06\u6b64\u6b21\u751f\u8349\u4fdd\u5b58\u4e3a\u914d\u7f6e", None))
        self.copy_result.setText(QCoreApplication.translate("application", u"\u590d\u5236\u7ed3\u679c", None))
        self.tabs.setTabText(self.tabs.indexOf(self.main_tab), QCoreApplication.translate("application", u"\u4e3b\u9875", None))
        self.second_setting_option_prompt.setText(QCoreApplication.translate("application", u"\u662f\u5426\u4e0d\u4f7f\u7528\u82f1\u6587(\u56e0\u4e3a\u8c37\u6b4c\u7ffb\u8bd1\u5bf9\u82f1\u6587\u7ffb\u8bd1\u652f\u6301\u8f83\u597d\uff0c\u5982\u679c\u4e0d\u4f7f\u7528\u82f1\u6587\u66f4\u52a0\u751f\u8349\uff0c\u5efa\u8bae\u9009\u62e9):", None))
        self.radio_first_setting_option.setText(QCoreApplication.translate("application", u"\u662f", None))
        self.radio_second_setting_option.setText(QCoreApplication.translate("application", u"\u5426", None))
        self.first_settings_option_prompt.setText(QCoreApplication.translate("application", u"\u9009\u62e9\u7684\u8c37\u6b4c\u7ffb\u8bd1\u57df\u540d(\u5efa\u8bae\u4e2d\u56fd\u5927\u9646\u7684\u5c45\u6c11\u9009\u62e9tanslate.google.cn):    ", None))
        self.third_setting_option_prompt.setText(QCoreApplication.translate("application", u"\u4f60\u8981\u4f7f\u7528\u7684Config\u6587\u4ef6\u6587\u4ef6\u540d(\u5efa\u8bae\u9009\u62e9\u9ed8\u8ba4\uff0c\u56e0\u4e3a\u6709\u5176\u4ed6Config\u53ef\u4ee5\u5bfc\u5165\u8fdb\u9ed8\u8ba4\u6587\u4ef6):", None))
        self.set_config_file_name.setText(QCoreApplication.translate("application", u"Config", None))
        self.fourth_setting_option_prompt_2.setText(QCoreApplication.translate("application", u"\u4f7f\u7528\u7684\u4e3b\u9898: ", None))
        self.fifth_setting_option_prompt.setText(QCoreApplication.translate("application", u"\u4f7f\u7528\u7684\u98ce\u683c\u6587\u4ef6", None))
        self.tabs.setTabText(self.tabs.indexOf(self.settings_tab), QCoreApplication.translate("application", u"\u8bbe\u7f6e", None))
        self.add_language.setText(QCoreApplication.translate("application", u"\u6dfb\u52a0\u8bed\u8a00", None))
        self.add_random_language.setText(QCoreApplication.translate("application", u"\u968f\u673a\u751f\u6210\u8bed\u8a00", None))
        self.delete_config_and_language.setText(QCoreApplication.translate("application", u"\u5220\u9664", None))
        self.add_config.setText(QCoreApplication.translate("application", u"\u6dfb\u52a0\u914d\u7f6e", None))
        self.add_random_config.setText(QCoreApplication.translate("application", u"\u968f\u673a\u751f\u6210\u914d\u7f6e", None))
        self.import_config.setText(QCoreApplication.translate("application", u"\u5bfc\u5165\u914d\u7f6e", None))
        self.export_config.setText(QCoreApplication.translate("application", u"\u5bfc\u51fa\u914d\u7f6e", None))
        self.all_config_prompt.setText(QCoreApplication.translate("application", u"\u5168\u90e8\u914d\u7f6e:", None))
        self.tabs.setTabText(self.tabs.indexOf(self.config_tab), QCoreApplication.translate("application", u"\u914d\u7f6e", None))
        self.about_text_browser.setHtml(QCoreApplication.translate("application", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h3 align=\"center\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:600;\">\u5173\u4e8e\u4f5c\u8005 </span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-weight:600;\" align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.github.com/superjavascrip\"><span style=\" text-decoration: underline; color:#16f216;\">Github @Superjavascrip</span></a> </li>\n"
"<li style=\" font-weight:600"
                        ";\" align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://space.bilibili.com/426825448\"><span style=\" text-decoration: underline; color:#16f216;\">Bilibili @\u5170\u683c\u5982\u540c</span></a> </li>\n"
"<li style=\" font-weight:600;\" align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u9177\u5b89 @\u5170\u683c\u5982\u540cOfficial </li></ul>\n"
"<h3 align=\"center\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:600;\">\u7b80\u4ecb </span></h3>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u8fd9\u662f\u4e00\u4e2a\u4f7f\u7528Python\u7f16\u5199\u7684\u8c37\u6b4c\u751f\u8349\u5668\uff08"
                        "GUI\uff09\uff0c\u53ef\u4ee5\u4f7f\u7528\u8c37\u6b4c\u7ffb\u8bd1\u5168\u81ea\u52a8\u7684\u5c06\u6587\u672c\u751f\u8349\u3002 </span></p>\n"
"<h3 align=\"center\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:600;\">\u9e23\u8c22 </span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-weight:600;\" align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/python/cpython\"><span style=\" text-decoration: underline; color:#16f216;\">Python\u89e3\u91ca\u5668\u5f00\u6e90\u4ee3\u7801</span></a> </li>\n"
"<li style=\" font-weight:600;\" align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.python.org/\"><span st"
                        "yle=\" text-decoration: underline; color:#16f216;\">Python\u5b98\u7f51</span></a> </li>\n"
"<li style=\" font-weight:600;\" align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/ssut/py-googletrans\"><span style=\" text-decoration: underline; color:#16f216;\">googletrans\u5e93</span></a> </li>\n"
"<li style=\" font-weight:600;\" align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pyside.org\"><span style=\" text-decoration: underline; color:#16f216;\">PySide\u5b98\u7f51</span></a> </li>\n"
"<li style=\" font-weight:600;\" align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/GTRONICK/QSS\"><span style=\" text-decoration: underline; color:#16f216;\">QSS\u9879\u76ee</span></a> </li>\n"
"<li style="
                        "\" font-weight:600;\" align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/Alexhuszagh/BreezeStyleSheets\"><span style=\" text-decoration: underline; color:#16f216;\">BreezeStyleSheets</span></a> </li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft YaHei UI'; font-size:medium; font-weight:696;\"><br /></p></body></html>", None))
        self.tabs.setTabText(self.tabs.indexOf(self.about_tab), QCoreApplication.translate("application", u"\u5173\u4e8e", None))
    # retranslateUi

