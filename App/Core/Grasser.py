# -*- coding: utf-8 -*-
import random
from typing import List, Union

import langid


class GrassResult(object):
    def __init__(
            self,
            text: str,
            language_list: Union[List[str], None]
    ):
        self.text = text
        self.language_list = language_list


class GoogleGrasser(object):
    def __init__(
            self,
            config_file_name: str = "Config",
            service_url: str = "translate.google.cn",
            no_english: bool = True
    ):
        from googletrans import Translator
        from ConfigManager import ConfigManager
        from Constants import LANGUAGES
        self.LANGUAGES = LANGUAGES
        if no_english and "en" in self.LANGUAGES:
            self.LANGUAGES.remove("en")
        self.translator = Translator(
            service_urls=[
                service_url
            ]
        )
        self.language_number = (len(self.LANGUAGES) - 1)
        self.config_manager = ConfigManager(config_file_name)

    def get_random_grass(
            self,
            original_text: str,
            grass_frequency: int = 20
    ) -> GrassResult:
        text = original_text
        language_list = []
        for i in range(grass_frequency + 1):
            if i != 0:
                random_language = random.choice(self.LANGUAGES)
                language_list.append(random_language)
                text = self.translator.translate(
                    text,
                    dest=random_language,
                    src=langid.classify(text)[0]
                ).text
            else:
                language_list.append("zh-cn")
                random_language = random.choice(self.LANGUAGES)
                text = self.translator.translate(
                    text,
                    dest=random_language,
                    src="zh-cn"
                ).text
        language_list.pop(0)
        return GrassResult(
            self.translator.translate(
                text,
                src=langid.classify(text)[0],
                dest="zh-cn"
            ).text,
            language_list
        )

    def output_random_grass_txt(
            self,
            input_txt: str,
            output_txt: str,
            grass_frequency: int = 20
    ) -> None:
        with open(input_txt, "r", encoding="utf-8") as input_txt:
            input_text = input_txt.read()
            random_grass = self.get_random_grass(input_text, grass_frequency)
            with open(output_txt, "w+", encoding="utf-8") as output_txt:
                output_txt.write(random_grass.text)

    def get_config_grass(
            self,
            original_text: str,
            config_name: str,
            grass_grass_frequency: int = 20
    ) -> GrassResult:
        config = self.config_manager.return_config(config_name)
        text = original_text
        for _ in range(grass_grass_frequency):
            for config_index in range(len(config)):
                if config_index != 0:
                    text = self.translator.translate(
                        text,
                        dest=config[config_index],
                        src=config[config_index - 1]
                    ).text
                else:
                    text = self.translator.translate(
                        text,
                        dest=config[config_index],
                        src="zh-cn"
                    ).text
        if langid.classify(text)[0] != "zh":
            text = self.translator.translate(
                text,
                dest="zh-cn",
                src=config[len(config) - 1]
            ).text
        return GrassResult(text, None)

    def output_config_grass(
            self,
            input_txt: str,
            output_txt: str,
            config_name: str,
            grass_frequency: int = 20,
    ) -> None:
        with open(input_txt, "r", encoding="utf-8") as input_txt:
            input_text = input_txt.read()
            config_grass = self.get_config_grass(
                input_text,
                config_name,
                grass_frequency
            )
            with open(output_txt, "w+", encoding="utf-8") as output_txt:
                output_txt.write(config_grass.text)
