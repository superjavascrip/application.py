# -*- coding: utf-8 -*-
import json
import os
from typing import List


class ConfigManager(object):
    def __init__(
            self,
            config_file_name: str
    ):
        self.config_file = f"Config/{config_file_name}.json"

    def return_all_config(self) -> List[str]:
        with open(self.config_file, "r+") as config_file_read:
            config_dict = json.load(config_file_read)
        return list(config_dict.keys())

    def new_config(
            self,
            language_list: List[str],
            config_name: str
    ) -> None:
        with open(self.config_file, "r+") as config_file_read:
            config_dict = json.load(config_file_read)
            if config_name in config_dict:
                raise NameError("已经有此config，请检查输入是否正确。")
            else:
                config_dict[config_name] = language_list
            with open(self.config_file, "w+") as config_file_write:
                config_file_write.write(
                    json.dumps(
                        config_dict,
                        sort_keys=True,
                        indent=4,
                        separators=(',', ': ')
                    )
                )

    def remove_config(
            self,
            config_name: str
    ) -> None:
        with open(self.config_file, "r+") as config_file_read:
            config_dict = json.load(config_file_read)
            if config_name in config_dict:
                config_dict.pop(config_name)
                with open(self.config_file, "w+") as config_file_write:
                    config_file_write.write(
                        json.dumps(
                            config_dict,
                            sort_keys=True,
                            indent=4,
                            separators=(',', ': ')
                        )
                    )
            else:
                raise NameError("没有此config，请检查输入是否正确。")

    def return_config(
            self,
            config_name: str
    ) -> List[str]:
        with open(self.config_file, "r+") as config_file_read:
            config_dict = json.load(config_file_read)
        if config_name in config_dict:
            return config_dict[config_name]
        else:
            raise NameError("没有此config，请检查输入是否正确。")

    def import_config(
            self,
            config_file: str
    ) -> None:
        if os.path.exists(config_file) and os.path.isfile(config_file) and config_file.endswith(".json"):
            with open(config_file, "r+") as config_file_read:
                config_dict = json.load(config_file_read)
                for key in config_dict:
                    self.new_config(config_dict[key], key)
        else:
            raise FileNotFoundError("没有此json文件。")

    def add_language(
            self,
            language_list: List[str],
            config_name: str,
            add_index: int
    ) -> None:
        with open(self.config_file, "r+") as config_file_read:
            config_dict = json.load(config_file_read)
            for language_index in range(len(language_list)):
                config_dict[config_name].insert(
                    (add_index + 1 + language_index), language_list[language_index]
                )
            with open(self.config_file, "w+") as config_file_write:
                config_file_write.write(
                    json.dumps(
                        config_dict,
                        sort_keys=True,
                        indent=4,
                        separators=(',', ': ')
                    )
                )

    def remove_language(
            self,
            language_index: int,
            config_name: str
    ) -> None:
        with open(self.config_file, "r+") as config_file_read:
            config_dict = json.load(config_file_read)
            if config_name in config_dict:
                del config_dict[config_name][language_index]
                with open(self.config_file, "w+") as config_file_write:
                    config_file_write.write(
                        json.dumps(
                            config_dict,
                            sort_keys=True,
                            indent=4,
                            separators=(',', ': ')
                        )
                    )
            else:
                raise NameError("没有此config，请检查输入是否正确。")

    def export_config(
            self,
            config_name_list: List[str],
            export_config_file_path: str
    ) -> None:
        with open(self.config_file, "r+") as config_file_read:
            config_dict = json.load(config_file_read)
            with open(export_config_file_path, "w+") as export_config_file:
                export_config_dict = {}
                for v in config_name_list:
                    export_config_dict[v] = config_dict[v]
                export_config_file.write(
                    json.dumps(
                        export_config_dict,
                        sort_keys=True,
                        indent=4,
                        separators=(',', ': ')
                    )
                )
