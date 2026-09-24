# -*- coding: utf-8 -*-
"""
Модуль "Выход из приложения".

Обеспечивает закрытие приложения.
"""

import sys

from rich import print

from .options import option_continue
from utils.text import clear, get_text as t


class Exit:
    """
    Модуль "Выход из приложения".

    Обеспечивает закрытие приложения.
    """

    def __init__(self):
        """Инициализация модуля."""
        self.__button_text: str = t("exit.button")

    @property
    def button_text(self) -> str:
        """Текст кнопки (опции) в меню приложения."""
        return self.__button_text

    def show(self) -> None:
        """
        Запуск модуля.

        Выводит сообщение и завершает работу приложения.
        """
        # Выводит сообщение о завершении работы приложения
        print(t("exit.message"), end="\n\n")

        # Запрашивает ввод ENTER перед выходом
        option_continue()

        # Очищает вывод терминала и завершает работу
        clear()
        sys.exit()
