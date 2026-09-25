# -*- coding: utf-8 -*-
"""Загружает конфигурацию приложения."""

from pathlib import Path

from utils.load_file import load_file


# Путь к папке приложения
APP_PATH: Path = Path(__file__).parent.parent

# Загрузка конфигурации из файла "config.toml" в корне приложения
_config_file: str = "config.toml"
_config_path: Path = APP_PATH.joinpath(_config_file)
_config: dict = load_file(_config_path)
_config_filters: dict = _config["filters"]
_config_progress_bar: dict = _config["progress_bar"]

# Чтение и настройка путей к данным приложения
_target_urls_path: Path = APP_PATH.joinpath(*_config["files"]["target_urls"])
_text_path: Path = APP_PATH.joinpath(*_config["files"]["text"])

# Фильтры для поиска по имени пользователя
F_RESPONSE_BODY: bool = _config_filters["response_body"]
F_RESPONSE_BODY_NOT_NULL: bool = _config_filters["response_body_not_null"]
F_KEYWORDS: bool = _config_filters["keywords"]
F_KEYWORDS_LIST: list = _config_filters["keywords_list"]

# Ссылка на GitHub проекта
GITHUB: str = _config["app"]["github"]

# Настройки шкалы прогресса
PROGRESS_BAR_FILL: str = _config_progress_bar["fill"]
PROGRESS_BAR_MESSAGE: str = _config_progress_bar["message"]
PROGRESS_BAR_SUFFIX_BASE: str = _config_progress_bar["suffix_base"]
PROGRESS_BAR_WIDTH: int = _config_progress_bar["width"]

# Ссылки на Интернет-сайты по которым будет вестись поиск пользователя
TARGET_URLS: dict = load_file(_target_urls_path)

# Весь текст, который выводит приложение
TEXT: dict = load_file(_text_path)

# Версия приложения
VERSION: str = _config["app"]["version"]
