# GoogleGrasser

[![Programing Language](https://img.shields.io/badge/Programing%20Language-Python-brightgreen)](https://www.python.org/)

[![github](https://img.shields.io/badge/github-superjavascrip-brightgreen.svg)](https://github.com/superjavascrip)

[![license](https://img.shields.io/github/license/superjavascrip/GoogleGrasser?color=greeb)](https://www.gnu.org/licenses/gpl-3.0.html)

这是一个python脚本，它使用Python googletrans库发送多个翻译请求，使文本变得生草。


本Readme包含:

* [安装依赖包](#安装依赖包)

* [运行脚本](#运行脚本)
* [项目文件目录](#项目文件目录)
* [将要添加的功能](#将要添加的功能)

## 安装依赖包

```shell
pip install -r requiments.txt
```

## 运行脚本

你可以在命令行里输入这些命令来运行脚本

```shell
cd App/Core/
python Application.py
```

## 项目文件目录

* App(代码存放目录)
    - Core(程序主目录)
        + \_\_Cache__(缓存文件目录)
        + Config(存放配置文件目录)
        + Export(导出的配置文件存放目录)
        + Output(导出的mp3音频文件存放目录)
        + res(资源目录)
          * application_icon.png(程序图标)
          * config.png(配置图标)
          * language.png(语言图标)
        + Settings.py(设置文件存放目录)
        + Application.py(应用程序主代码文件)
        + ConfigManager.py(配置管理器代码文件)
        + Constants.py(程序常量存放文件)
        + GoogleVoice.py(谷歌语音爬虫代码文件)
        + Grasser.py(生草器主代码文件)
        + SettingsManager.py(设置管理器代码文件)
        + UI_GoogleGrasser.py(程序主UI代码文件，由PySide6-uic 用 UI文件夹里的UI_GoogleGrasser.ui文件自动生成)
        + Style(程序美化文件目录)
    - UI(UI文件目录，由PySide6-uic 用 UI文件夹里的AddLanguageDialog.ui文件自动生成)
        + UI_GoogleGrasser.ui(PySide6UI文件，使用QtDesign编辑)
* LICENSE(开源协议)
* Readme.md(本文)
* requiments.txt(依赖包文件)

## 将要添加的功能

* 将配置界面功能实装
* 增加代理设置

##### 鸣谢

[Github项目QSS](https://github.com/GTRONICK/QSS)