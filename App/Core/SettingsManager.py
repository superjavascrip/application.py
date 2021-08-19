# -*- coding: utf-8 -*-

"""
This module is a tool of the setttings.
You can set settings with this module.
"""

from typing import Union

import json


class SettingsManager(object):
    def __init__(self):
        self.SETTINGS_FILE = "Settings/Settings.json"

    def manage_setting(
            self,
            setting_name: str,
            value: Union[str, bool]
    ) -> None:
        with open(self.SETTINGS_FILE, "r+") as settings_file_read:
            settings_dict = json.loads(settings_file_read.read())
            if setting_name not in settings_dict["Settings"]:
                raise NameError("没有此设置")
            else:
                settings_dict["Settings"][setting_name] = value
            with open(self.SETTINGS_FILE, "w+") as settings_file_write:
                settings_file_write.write(
                    json.dumps(
                        settings_dict,
                        sort_keys=True,
                        indent=4, separators=(',', ': ')
                    )
                )

    def get_setting(
            self,
            setting_name: str
    ) -> str:
        with open(self.SETTINGS_FILE, "r+") as settings_file:
            settings_dict = json.loads(settings_file.read())
            if setting_name not in settings_dict["Settings"]:
                raise NameError("没有此设置")
            else:
                return settings_dict["Settings"][setting_name]

    def setup_settings(
            self,
            obj: object
    ) -> None:
        obj.google_translate_service_url = self.get_setting(
            "google_translate_service_url")
        obj.random_grass_no_english = self.get_setting(
            "random_grass_no_english")
        obj.application_style = self.get_setting("application_style")
        obj.config_file_name = self.get_setting("config_file_name")
        obj.application_qss = self.get_setting("application_qss")
