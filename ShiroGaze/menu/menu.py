# -*- coding: utf-8 -*-
"""Главный управляющий класс."""

from rich import print

import config
from .modules import About, Exit, SearchByUsername
from .modules.options import option_continue
from utils.text import clear, get_text as t


class Menu:
    """
    Главный управляющий класс.

    Запускается первым, из него вызываются все остальные действия.
    """

    def __init__(self):
        """Инициализация класса. """
        # Список доступного пользователю функционала приложения
        self._options: list = [
            SearchByUsername,
            About,
            Exit
        ]

    def _input_user_choice(self) -> int:
        """Запрашивает у пользователя выбор действия.

        Returns:
            int: Номер действия, которое выбрал пользователь.
        """
        while True:

            try:
                # Ввод пользователя
                print(t("menu.input.message"), end="")
                user_input: int = int(input())

                # Число должно быть положительным и не превышать
                # количество доступных дейтсвий.
                if 1 <= user_input <= len(self._options):
                    break

                raise ValueError  # Ввод пользователя не удовлетворяет условие

            # Пользователь ввёл некорректный тип данных (не число)
            # или число не входит в множество доступных действий
            except ValueError:
                error_text: str = t("menu.input.error").format(
                    max_length=len(self._options)
                )
                print(error_text)

        return user_input

    def show(self) -> None:
        """Запуск работы приложения."""
        while True:
            clear()  # Очищает вывод в терминал

            # Выводит логотип и описание приложения
            logo: str = t("menu.app.logo")
            description: str = t("menu.app.description").format(
                github=config.GITHUB, version=config.VERSION
            )
            print("\n" + logo + "\n\n" + description, end="\n\n")

            # Вывод списка доступных действий
            for i, option in enumerate(self._options):
                print(f"[{i + 1}] {option().button_text}")
            print()

            # Запрос у пользователя выбора действия
            option: int = self._input_user_choice()

            clear()  # Очищает вывод в терминал и выводит логотип приложения
            print("\n" + logo, end="\n\n")

            # Выполнение модуля согласно выбора пользователя
            self._options[option - 1]().show()

            print()  # Запрашивает ввод ENTER перед продолжением выполнения
            option_continue()
