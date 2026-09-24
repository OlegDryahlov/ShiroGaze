# -*- coding: utf-8 -*-
"""Обеспечивает закрытие приложения."""

import sys

from rich import print

from .options import option_continue
from utils.text import clear, get_text as t


class Exit:
    """Обеспечивает закрытие приложения."""

    def __init__(self):
        """Инициализация класса."""
        self.__button_text: str = t("exit.button")
        self.__message: str = t("exit.message")

    @property
    def button_text(self) -> str:
        """Текст кнопки (опции) в меню приложения."""
        return self.__button_text

    def show(self) -> None:
        """
        Запуск модуля.

        Выводит сообщение и завершает работу приложения.
        """
        print(self.__message + "\n")
        option_continue()
        clear()
        sys.exit()
