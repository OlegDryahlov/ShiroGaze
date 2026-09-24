# -*- coding: utf-8 -*-
"""
Модуль "О приложении".

Выводит описание приложения, его версию, разработчика и т.д.
В дальнейшем функционал модуля будент расширен.
"""

from rich import print

import config
from utils.text import get_text as t


class About:
    """
    Модуль "О приложении".

    Выводит информацию о приложении.
    """

    def __init__(self):
        """Инициализация модуля."""
        self.__button_text: str = t("about.button")

    @property
    def button_text(self) -> str:
        """Текст кнопки (опции) в меню приложения."""
        return self.__button_text

    def show(self) -> None:
        """
        Запуск модуля.

        Выводит информацию о приложении.
        """
        message: str = t("about.message").format(version=config.VERSION)
        print(message)
