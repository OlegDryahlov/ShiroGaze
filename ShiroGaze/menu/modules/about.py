# -*- coding: utf-8 -*-
"""Выводит информацию о приложении."""

# В дальнейшем функционал будет расширен. Планируется добавить проверку на
# обновления и автообновление приложения.

import config
from text import get_text as t


class About:
    """Выводит информацию о приложении."""

    def __init__(self):
        """Инициализация класса."""
        self.__button_text: str = t("about.button")
        self._app_about: str = t("about.message").format(
            version=config.VERSION
        )

    @property
    def button_text(self) -> str:
        """Текст кнопки (опции) в меню приложения."""
        return self.__button_text

    def show(self) -> None:
        """
        Запуск модуля.

        Выводит информацию о приложении.
        """
        print(self._app_about)
