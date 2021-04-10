from UI_GoogleGrasser import Ui_application

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from Grasser import GoogleGrasser
from ConfigManager import ConfigManager
from SettingsManager import SettingsManager
from GoogleVoice import GoogleVoice
import Grasser
import Constants

import langid
import os
import pyperclip
import random
import shiboken6
import time
import re
import webbrowser


class OnDeleteLanguageToAddClick(QObject):
    quit = Signal(name="exit")

    def __init__(
            self,
            parent
    ):
        super(OnDeleteLanguageToAddClick, self).__init__(parent)

    def on_click(
            self,
            dialog: QDialog
    ) -> None:
        for item in dialog.language_to_add.selectedItems():
            shiboken6.delete(item)
            time.sleep(0.5)
        dialog.language_to_add.clearSelection()
        dialog.all_language.clearSelection()
        self.quit.emit()


class OnOutputGoogleVoiceClick(QObject):
    warning = Signal(str, str, name="Warning")
    quit = Signal(name="exit")

    def __init__(
            self,
            parent
    ):
        super(OnOutputGoogleVoiceClick, self).__init__(parent)
        self.google_voice = GoogleVoice()

    def output_grass_voice(
            self,
            grass_result: Grasser.GrassResult,
            output_file: str
    ) -> None:
        grass_string = grass_result.text
        try:
            if len(grass_string) <= 198:
                self.google_voice.output_voice(grass_string, f"Output/{output_file}")
            else:
                number = len(grass_string) // 198
                number_of_remaining_digits = len(grass_string) % 198
                for i in range(number):
                    __CacheString__ = grass_string[i * 198:(i + 1) * 198]
                    self.google_voice.output_voice(
                        "__Cache__/__Cache__{}.mp3".format(i + 1),
                        __CacheString__
                    )
                self.google_voice.output_voice(
                    grass_string[number * 198:number * 198 + number_of_remaining_digits],
                    "__Cache__/__Cache__{}.mp3".format(number + 1)
                )
                input_list = []
                for a, b, c in os.walk(r'__Cache__/'):
                    for i in c:
                        input_list.append("__Cache__/{}".format(i))
                self.google_voice.splicing_audio(input_list, output_file)
                for i in input_list:
                    os.remove(i)
        except FileExistsError:
            self.warning.emit("请勿删除__Cache__文件夹或内部的任意文件")

    def on_click(
            self,
            grass_result: Grasser.GrassResult,
            output_file: str
    ) -> None:
        self.output_grass_voice(grass_result, output_file)
        self.quit.emit()


class OnStartGrassClick(QObject):
    set_grass_result = Signal(Grasser.GrassResult, name="GrassResult")
    warning = Signal(str, str, name="Warning")
    quit = Signal(name="exit")

    def __init__(
            self,
            parent
    ):
        super(OnStartGrassClick, self).__init__(parent)

    def on_click(
            self,
            grasser: Grasser.GoogleGrasser,
            original_text: str,
            grass_frequency: int,
            config_name: str,
    ) -> None:
        if original_text == "":
            self.warning.emit("错误", "输入不能为空")
        elif langid.classify(original_text)[0] != "zh":
            self.warning.emit("错误", "需要生草的语言必须为中文")
        else:
            if config_name == "随机":
                grass_result = grasser.get_random_grass(
                    original_text,
                    grass_frequency
                )
            else:
                grass_result = grasser.get_config_grass(
                    original_text,
                    config_name,
                    grass_frequency
                )
            self.set_grass_result.emit(grass_result)
        self.quit.emit()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.grass_result: Grasser.GrassResult
        self.output_google_voice_file_name: str
        self.settings_manager = SettingsManager()
        self.settings_manager.setup_settings(self)
        self.grasser = GoogleGrasser(
            self.config_file_name,
            self.google_translate_service_url,
            self.random_grass_no_english
        )
        self.config_manager = ConfigManager(
            self.config_file_name
        )

        self.change_style(self.application_style)
        self.setStyleSheet(self.get_qss(f"{self.application_qss}.qss"))

        self.ui = Ui_application()

        self.ui.setupUi(self)

        self.ui.select_google_translate_url.addItems(Constants.SERVICE_URLS)
        self.ui.select_application_style.addItems(QStyleFactory.keys())
        self.ui.select_application_qss.addItems(
            [file.replace(".qss", "") for file in os.listdir("Style") if os.path.isfile(f"Style/{file}") if
             file.split(".")[1] == "qss"]
        )

        self.ui.select_google_translate_url.setCurrentIndex(
            Constants.SERVICE_URLS.index(self.google_translate_service_url)
        )
        self.ui.select_application_style.setCurrentIndex(
            QStyleFactory.keys().index(self.application_style)
        )
        self.ui.select_application_qss.setCurrentIndex(
            [file.replace(".qss", "") for file in os.listdir("Style") if os.path.isfile(f"Style/{file}") if
             file.split(".")[1] == "qss"].index(self.application_qss)
        )

        if self.random_grass_no_english:
            self.ui.radio_first_setting_option.setChecked(True)
        else:
            self.ui.radio_second_setting_option.setChecked(True)

        self.add_language_dialog = QDialog()
        self.init_add_language_dialog()
        self.init_all_config()
        self.init_select_config()

        self.GrassingThread = QThread(self)
        self.OutputGoogleVoiceThread = QThread(self)
        self.DeleteLanguageToAddThread = QThread(self)
        self.OnStartGrassClick = OnStartGrassClick(self)
        self.OnStartGrassClick.moveToThread(self.GrassingThread)
        self.OnOutputGoogleVoiceClick = OnOutputGoogleVoiceClick(self)
        self.OnOutputGoogleVoiceClick.moveToThread(self.OutputGoogleVoiceThread)
        self.OnDeleteLanguageToAddClick = OnDeleteLanguageToAddClick(self)
        self.OnDeleteLanguageToAddClick.moveToThread(self.DeleteLanguageToAddThread)

        self.ui.start_grass.clicked.connect(self.on_start_grass_click)
        self.ui.open_file.clicked.connect(self.on_open_file_click)
        self.ui.copy_result.clicked.connect(self.on_copy_result_click)
        self.ui.save_this_grass_as_config.clicked.connect(self.on_save_this_grass_as_config_click)
        self.ui.save_result.clicked.connect(self.on_save_grass_result_click)
        self.ui.add_language.clicked.connect(self.on_add_language_click)
        self.ui.output_google_voice.clicked.connect(self.on_output_google_voice_click)
        self.ui.add_random_language.clicked.connect(self.on_add_random_language_click)
        self.ui.delete_config_and_language.clicked.connect(self.delete_config_and_language)
        self.ui.add_config.clicked.connect(self.on_add_config_click)
        self.ui.import_config.clicked.connect(self.on_import_config_click)
        self.ui.export_config.clicked.connect(self.on_export_config_click)
        self.ui.about_text_browser.anchorClicked.connect(self.open_link)

        self.OnStartGrassClick.set_grass_result.connect(self.set_grass_result)
        self.OnStartGrassClick.warning.connect(self.warning_dialog)
        self.OnStartGrassClick.quit.connect(self.quit_grassing_thread)
        self.OnOutputGoogleVoiceClick.quit.connect(self.quit_output_google_voice_click)
        self.OnOutputGoogleVoiceClick.warning.connect(self.warning_dialog)
        self.OnDeleteLanguageToAddClick.quit.connect(self.quit_delete_language_to_add)
        self.ui.select_google_translate_url.currentTextChanged.connect(
            self.on_select_google_translate_url_current_index_changed
        )
        self.ui.select_application_qss.currentTextChanged.connect(
            self.select_application_qss_current_index_changed
        )
        self.GrassingThread.started.connect(
            lambda:
            self.OnStartGrassClick.on_click(
                self.grasser,
                self.ui.original_text_edit.toPlainText(),
                self.ui.grass_frequency.value(),
                self.ui.select_config.currentText()
            )
        )
        self.OutputGoogleVoiceThread.started.connect(
            lambda:
            self.OnOutputGoogleVoiceClick.on_click(
                self.grass_result,
                self.output_google_voice_file_name
            )
        )
        self.DeleteLanguageToAddThread.started.connect(
            lambda:
            self.OnDeleteLanguageToAddClick.on_click(
                self.add_language_dialog
            )
        )
        self.ui.second_setting_option_button_group.buttonClicked.connect(
            self.on_second_setting_option_click
        )
        self.ui.set_config_file_name.returnPressed.connect(
            self.on_set_config_file_name_return_pressed
        )
        self.ui.select_application_style.currentTextChanged.connect(
            self.select_application_style_current_index_changed
        )

    def on_start_grass_click(self) -> None:
        self.GrassingThread.start()

    def on_open_file_click(self) -> None:
        file_name = QFileDialog.getOpenFileName(self, "选择要生草的txt文件", "", "Txt files(*.txt)")
        if file_name[0] != "":
            with open(file_name[0], "r+", encoding="utf-8") as file:
                text = file.read()
            self.ui.original_text_edit.setPlainText(text)

    def on_copy_result_click(self) -> None:
        if "grass_result" in vars(self):
            pyperclip.copy(self.grass_result.text)
        else:
            self.warning_dialog("错误", "没有生草结果，无法复制")

    def on_save_this_grass_as_config_click(self) -> None:
        if "grass_result" in vars(self):
            if self.grass_result.language_list is None:
                self.warning_dialog("错误", "此次生草本就使用了配置")
            else:
                config_name, ok_pressed = QInputDialog.getText(
                    self,
                    "输入配置名称",
                    "名称:",
                    QLineEdit.Normal,
                    "")
                if ok_pressed:
                    self.config_manager.new_config(self.grass_result.language_list, config_name)
        else:
            self.warning_dialog("错误", "没有生草结果，无法生成配置")

    def on_save_grass_result_click(self) -> None:
        if "grass_result" in vars(self):
            file_path, ok_pressed = QFileDialog.getSaveFileName(
                self,
                "保存生草结果文件",
                "",
                "txt类型 (*.txt)"
            )
            if ok_pressed:
                with open(file_path, "w+") as output_file:
                    output_file.write(self.grass_result.text)
        else:
            self.warning_dialog("错误", "没有生草结果，无法保存文件")

    def on_output_google_voice_click(self) -> None:
        if "grass_result" in vars(self):
            file_name, ok_pressed = QInputDialog.getText(
                self,
                "请输入文件名",
                "文件名",
                QLineEdit.Normal
            )
            if ok_pressed:
                vars(self)["output_google_voice_file_name"] = file_name
                self.OutputGoogleVoiceThread.start()
        else:
            self.warning_dialog("错误", "没有生草结果，无法保存文件")

    def on_export_config_click(self) -> None:
        file_path, ok_pressed = QFileDialog.getSaveFileName(
            self,
            "导出配置文件",
            "",
            "json类型 (*.json)"
        )
        if ok_pressed:
            config_name_list = []
            for item in self.ui.all_config.selectedItems():
                if item.parent() is None:
                    config_name_list.append(item.data(0, 0))
            self.config_manager.export_config(config_name_list, file_path)

    def on_select_google_translate_url_current_index_changed(self) -> None:
        self.settings_manager.manage_setting(
            "google_translate_service_url",
            self.ui.select_google_translate_url.currentText()
        )
        self.init_grasser()

    def on_second_setting_option_click(self) -> None:
        self.settings_manager.manage_setting(
            "random_grass_no_english",
            True if self.ui.second_setting_option_button_group.checkedButton().text() == "是" else False
        )
        self.init_grasser()

    def on_set_config_file_name_return_pressed(self) -> None:
        self.settings_manager.manage_setting(
            "config_file_name",
            self.ui.set_config_file_name.text()
        )
        self.init_grasser()

    def on_add_language_click(self) -> None:
        if len(self.ui.all_config.selectedItems()) == 1:
            selected_item = self.ui.all_config.selectedItems()[0]
            if selected_item.parent() is not None:
                self.add_language_dialog.show()
            else:
                self.add_language_dialog.show()
        elif len(self.ui.all_config.selectedItems()) == 0:
            self.warning_dialog("错误", "你还没有选择要操作的配置")
            raise Constants.SelectItemError("你还没有选择要操作的配置")
        else:
            self.warning_dialog("错误", "选择过多")
            raise Constants.SelectItemError("选择过多")

    def on_add_random_language_click(self) -> None:
        if len(self.ui.all_config.selectedItems()) == 0:
            self.warning_dialog("错误", "你还没有选择要操作的配置")
            raise Constants.SelectItemError("你还没有选择要操作的配置")
        else:
            languages_numbers, ok_pressed = QInputDialog.getText(
                self,
                "输入语言个数",
                "个数:",
                QLineEdit.Normal,
                "")
            if ok_pressed:
                language_list = []
                for _ in range(int(languages_numbers) + 1):
                    language_list.append(random.choice(Constants.LANGUAGES))
                if len(self.ui.all_config.selectedItems()) == 1:
                    item = self.ui.all_config.selectedItems()[0]
                    if item.parent() is not None:
                        self.config_manager.add_language(
                            language_list,
                            self.ui.all_config.selectedItems()[0].parent().text(0),
                            self.ui.all_config.selectedIndexes()[0].row()
                        )

                        self.init_all_config()
                    else:
                        self.config_manager.add_language(
                            language_list,
                            item.data(0, 0),
                            0
                        )
                        self.init_all_config()
                elif len(self.ui.all_config.selectedItems()) == 0:
                    self.warning_dialog("错误", "你还没有选择要操作的配置")
                    raise Constants.SelectItemError("你还没有选择要操作的配置")
                else:
                    self.warning_dialog("错误", "选择过多")
                    raise Constants.SelectItemError("选择过多")

    def delete_config_and_language(self) -> None:
        for item in self.ui.all_config.selectedItems():
            if item.parent() is not None:
                self.config_manager.remove_language(item.parent().indexOfChild(item), item.parent().data(0, 0))
                self.init_select_config()
                shiboken6.delete(item)
            else:
                self.config_manager.remove_config(item.data(0, 0))
                self.init_select_config()
                shiboken6.delete(item)

    def on_add_config_click(self) -> None:
        config_name, ok_pressed = QInputDialog.getText(
            self,
            "输入配置名称",
            "名称:",
            QLineEdit.Normal,
            "")
        if ok_pressed:
            if re.match("[\u4e00-\u9fa5_a-zA-Z0-9]", config_name) is None:
                self.warning_dialog("错误", "请重新输入")
            else:
                self.config_manager.new_config([], config_name)
                self.init_all_config()
                self.init_select_config()

    def on_add_language_dialog_add_language_click(self) -> None:
        if self.ui.all_config.selectedItems()[0].parent() is not None:
            self.config_manager.add_language(
                self.get_languages(self.add_language_dialog.language_to_add),
                self.ui.all_config.selectedItems()[0].parent().text(0),
                self.ui.all_config.selectedIndexes()[0].row()
            )
        else:
            self.config_manager.add_language(
                self.get_languages(self.add_language_dialog.language_to_add),
                self.ui.all_config.selectedItems()[0].text(0),
                0
            )
        self.init_all_config()
        self.add_language_dialog.language_to_add.clearSelection()
        self.add_language_dialog.all_language.clearSelection()

    def on_import_config_click(self) -> None:
        file_path, ok_pressed = QFileDialog.getOpenFileName(
            self,
            "配置文件",
            "",
            "json类型 (*.json)"
        )
        if ok_pressed:
            self.config_manager.import_config(file_path)
            self.init_all_config()

    def select_application_style_current_index_changed(self) -> None:
        self.settings_manager.manage_setting(
            "application_style",
            self.ui.select_application_style.currentText()
        )
        self.change_style(self.ui.select_application_style.currentText())

    def select_application_qss_current_index_changed(self) -> None:
        self.settings_manager.manage_setting(
            "application_qss",
            self.ui.select_application_qss.currentText()
        )
        self.setStyleSheet(self.get_qss(f"{self.ui.select_application_qss.currentText()}.qss"))

    def on_add_language_dialog_add_language_to_add_click(self) -> None:
        for item in self.add_language_dialog.all_language.selectedItems():
            language_item = QTreeWidgetItem(self.add_language_dialog.language_to_add)
            language_item.setText(0, item.text(0))
            language_item.setIcon(0, item.icon(0))
            language_item.setText(1, Constants.LANGUAGE_TRANSLATE.get(item.text(0)))
            language_item.setIcon(1, item.icon(1))
        self.add_language_dialog.language_to_add.clearSelection()
        self.add_language_dialog.all_language.clearSelection()

    def on_add_language_dialog_clean_all_language_click(self) -> None:
        self.add_language_dialog.language_to_add.clear()

    def on_add_language_dialog_delete_language_to_add_click(self) -> None:
        if len(self.add_language_dialog.language_to_add.selectedItems()) == 0:
            QMessageBox(
                QMessageBox.Warning,
                "错误",
                "你还没有选择要操作的语言",
                parent=self.add_language_dialog
            ).exec_()
            raise Constants.SelectItemError("你还没有选择要操作的语言")
        else:
            self.DeleteLanguageToAddThread.start()

    @staticmethod
    def open_link(url: QUrl) -> None:
        webbrowser.open(url.toString())

    def set_grass_result(
            self,
            grass_result: Grasser.GrassResult
    ) -> None:
        self.ui.grass_result_browser.setPlainText(grass_result.text)
        vars(self)["grass_result"] = grass_result

    def quit_grassing_thread(self) -> None:
        self.GrassingThread.quit()

    def quit_output_google_voice_click(self) -> None:
        self.OutputGoogleVoiceThread.quit()

    def quit_delete_language_to_add(self) -> None:
        self.DeleteLanguageToAddThread.quit()

    def warning_dialog(
            self,
            title: str,
            content_text: str
    ) -> None:
        QMessageBox(
            QMessageBox.Warning,
            title,
            content_text,
            parent=self
        ).exec_()

    def init_select_config(self) -> None:
        self.ui.select_config.clear()
        self.ui.select_config.addItems(
            ["随机"] + self.config_manager.return_all_config()
        )

    def init_grasser(self) -> None:
        self.grasser = Grasser.GoogleGrasser(
            self.ui.set_config_file_name.text(),
            self.ui.select_google_translate_url.currentText(),
            True if self.ui.second_setting_option_button_group.checkedButton().text() == "是" else False
        )

    def init_all_config(self) -> None:
        self.ui.all_config.clear()
        config_name_list = self.config_manager.return_all_config()
        self.ui.all_config.setColumnCount(2)
        self.ui.all_config.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.all_config.setHeaderLabels(["配置名", "语言中文名称"])
        self.ui.all_config.setColumnWidth(0, 130)
        for config_name_index in range(len(config_name_list)):
            config_item = QTreeWidgetItem(self.ui.all_config)
            config_item.setText(0, config_name_list[config_name_index])
            config_item.setIcon(0, QIcon("res/config.svg"))
            config = self.config_manager.return_config(config_name_list[config_name_index])
            for config_index in range(len(config)):
                language_item = QTreeWidgetItem(config_item)
                language_item.setText(0, config[config_index])
                language_item.setText(1, Constants.LANGUAGE_TRANSLATE[config[config_index]])
                language_item.setIcon(0, QIcon("res/language.svg"))
                language_item.setIcon(1, QIcon("res/language.svg"))

    def init_add_language_dialog(self) -> None:
        self.add_language_dialog.resize(450, 250)
        icon = QIcon()
        icon.addFile(u"res/application-icon.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.add_language_dialog.setWindowIcon(icon)
        self.add_language_dialog.gridLayout = QGridLayout(self.add_language_dialog)
        self.add_language_dialog.gridLayout.setObjectName(u"gridLayout")
        self.add_language_dialog.all_language = QTreeWidget(self.add_language_dialog)
        self.add_language_dialog.all_language.setObjectName(u"all_language")

        self.add_language_dialog.gridLayout.addWidget(self.add_language_dialog.all_language, 1, 0, 1, 1)

        self.add_language_dialog.add_language_to_add = QPushButton(self.add_language_dialog)
        self.add_language_dialog.add_language_to_add.setObjectName(u"add_language_to_add")

        self.add_language_dialog.gridLayout.addWidget(self.add_language_dialog.add_language_to_add, 2, 0, 1, 1)

        self.add_language_dialog.add_language = QPushButton(self.add_language_dialog)
        self.add_language_dialog.add_language.setObjectName(u"add_language")

        self.add_language_dialog.gridLayout.addWidget(self.add_language_dialog.add_language, 2, 1, 1, 1)

        self.add_language_dialog.language_to_add = QTreeWidget(self.add_language_dialog)
        self.add_language_dialog.language_to_add.setObjectName(u"language_to_add")

        self.add_language_dialog.gridLayout.addWidget(self.add_language_dialog.language_to_add, 1, 1, 1, 1)

        self.add_language_dialog.delete_language_to_add = QPushButton(self.add_language_dialog)
        self.add_language_dialog.delete_language_to_add.setObjectName(u"delete_language_to_add")

        self.add_language_dialog.gridLayout.addWidget(self.add_language_dialog.delete_language_to_add, 3, 0, 1, 1)

        self.add_language_dialog.clean_all_language = QPushButton(self.add_language_dialog)
        self.add_language_dialog.clean_all_language.setObjectName(u"clean_all_language")

        self.add_language_dialog.gridLayout.addWidget(self.add_language_dialog.clean_all_language, 3, 1, 1, 1)

        self.add_language_dialog.first_prompt = QLabel(self.add_language_dialog)
        self.add_language_dialog.first_prompt.setObjectName(u"first_prompt")

        self.add_language_dialog.gridLayout.addWidget(self.add_language_dialog.first_prompt, 0, 0, 1, 1)

        self.add_language_dialog.second_prompt = QLabel(self.add_language_dialog)
        self.add_language_dialog.second_prompt.setObjectName(u"second_prompt")

        self.add_language_dialog.gridLayout.addWidget(self.add_language_dialog.second_prompt, 0, 1, 1, 1)

        self.add_language_dialog.all_language.setColumnCount(2)
        self.add_language_dialog.all_language.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.add_language_dialog.all_language.setHeaderLabels(["语言名", "语言中文名称"])
        self.add_language_dialog.all_language.setColumnWidth(0, 90)

        self.add_language_dialog.language_to_add.setColumnCount(2)
        self.add_language_dialog.language_to_add.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.add_language_dialog.language_to_add.setHeaderLabels(["语言名", "语言中文名称"])
        self.add_language_dialog.language_to_add.setColumnWidth(0, 90)

        self.add_language_dialog.setWindowTitle(
            QCoreApplication.translate(
                u"Dialog",
                u"\u6dfb\u52a0\u8bed\u8a00",
                None
            )
        )
        self.add_language_dialog.add_language_to_add.setText(
            QCoreApplication.translate(
                u"Dialog",
                u"\u6dfb\u52a0\u8981\u6dfb\u52a0\u7684\u8bed\u8a00",
                None
            )
        )
        self.add_language_dialog.add_language.setText(
            QCoreApplication.translate(
                u"Dialog",
                u"\u6dfb\u52a0",
                None
            )
        )
        self.add_language_dialog.delete_language_to_add.setText(
            QCoreApplication.translate(
                u"Dialog",
                u"\u5220\u9664\u8bed\u8a00",
                None
            )
        )
        self.add_language_dialog.clean_all_language.setText(
            QCoreApplication.translate(
                u"Dialog",
                u"\u6e05\u9664",
                None
            )
        )
        self.add_language_dialog.first_prompt.setText(
            QCoreApplication.translate(
                u"Dialog",
                u"\u5168\u90e8\u8bed\u8a00",
                None
            )
        )
        self.add_language_dialog.second_prompt.setText(
            QCoreApplication.translate(
                u"Dialog",
                u"\u8981\u6dfb\u52a0\u7684\u8bed\u8a00",
                None
            )
        )
        for language in Constants.LANGUAGE_TRANSLATE:
            language_item = QTreeWidgetItem(self.add_language_dialog.all_language)
            language_item.setText(0, language)
            language_item.setIcon(0, QIcon("res/language.svg"))
            language_item.setText(1, Constants.LANGUAGE_TRANSLATE.get(language))
            language_item.setIcon(1, QIcon("res/language.svg"))

        self.add_language_dialog.add_language_to_add.clicked.connect(
            self.on_add_language_dialog_add_language_to_add_click
        )
        self.add_language_dialog.add_language.clicked.connect(
            self.on_add_language_dialog_add_language_click
        )
        self.add_language_dialog.clean_all_language.clicked.connect(
            self.on_add_language_dialog_clean_all_language_click
        )
        self.add_language_dialog.delete_language_to_add.clicked.connect(
            self.on_add_language_dialog_delete_language_to_add_click
        )

    @staticmethod
    def get_languages(tree_widget: QTreeWidget) -> list:
        languages = []
        item = QTreeWidgetItemIterator(tree_widget)
        for _ in range(tree_widget.topLevelItemCount()):
            languages.append(item.value().text(0))
            item.__iadd__(1)
        return languages

    @staticmethod
    def change_style(
            style_name: str
    ) -> None:
        styles = QStyleFactory.keys()
        if style_name not in styles:
            QApplication.setStyle(styles[0])
            raise NameError("没有此主题，使用默认主题")
        else:
            QApplication.setStyle(style_name)

    @staticmethod
    def get_qss(file_name) -> str:
        with open(f"Style/{file_name}", "r+") as qss_file:
            return qss_file.read()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.add_language_dialog.close()


if __name__ == '__main__':
    application = QApplication()
    main_window = MainWindow()
    main_window.show()
    application.exec_()
