# -*- coding: utf-8 -*-
"""Обеспечивает закрытие приложения."""

import sys


class Exit:
    """Обеспечивает закрытие приложения."""

    def __init__(self):
        """Инициализация класса."""
        self.__button_text = "Выход"

    @property
    def button_text(self) -> str:
        """Текст кнопки (опции) в меню приложения."""
        return self.__button_text

    def show(self) -> None:
        """
        Запуск модуля.

        Выводит сообщение и завершает работу приложения.
        """
        print("\nЗавершение работы.")
        sys.exit()
