# -*- coding: utf-8 -*-
"""Загружает конфигурацию приложения."""

from pathlib import Path

from load_file import load_file


# Путь к папке приложения
APP_PATH: Path = Path(__file__).parent.parent

# Загрузка конфигурации из файла "config.toml" в корне приложения
_config_file: str = "config.toml"
_config_path: Path = APP_PATH.joinpath(_config_file)
_config: dict = load_file(_config_path)
_config_progress_bar = _config["progress_bar"]

# Чтение и настройка путей к данным приложения
_app_description_path: Path = APP_PATH.joinpath(
    *_config["files"]["app_description"]
)
_app_logo_path: Path = APP_PATH.joinpath(*_config["files"]["app_logo"])
_target_urls_path: Path = APP_PATH.joinpath(*_config["files"]["target_urls"])

# Описание приложения
APP_DESCRIPTION: str = load_file(_app_description_path).format(
    github=_config["app"]["github"],
    version=_config["app"]["version"]
)

# Логотип приложения
APP_LOGO: str = load_file(_app_logo_path)

# Ссылки на Интернет-сайты по которым будет вестись поиск пользователя
TARGET_URLS: dict = load_file(_target_urls_path)

# Настройки шкалы прогресса
PROGRESS_BAR_FILL: str = _config_progress_bar["fill"]
PROGRESS_BAR_MESSAGE: str = _config_progress_bar["message"]
PROGRESS_BAR_SUFFIX_BASE: str = _config_progress_bar["suffix_base"]
PROGRESS_BAR_WIDTH: int = _config_progress_bar["width"]
