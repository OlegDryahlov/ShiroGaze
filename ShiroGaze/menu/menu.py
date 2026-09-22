# -*- coding: utf-8 -*-
"""Главный управляющий класс."""

import config
from .modules import About, Exit, SearchByUsername


class Menu:
    """
    Главный управляющий класс.

    Запускается первым, из него вызываются все остальные действия.
    """

    def __init__(self):
        """Инициализация класса. """
        self._about: About = About()  # Выводит информацию о приложении

        self._exit: Exit = Exit()  # Выход из приложения

        # Выполняет поиск по имени пользователя
        self._search_by_username: SearchByUsername = SearchByUsername()

        # Список доступного пользователю функционала приложения
        self._options: list = [
            self._search_by_username,
            self._about,
            self._exit
        ]

    def _input_user_choice(self) -> int:
        """Запрашивает у пользователя выбор действия.

        Returns:
            int: Номер действия, которое выбрал пользователь.
        """
        # Бесконечный цикл, пока пользователь не введёт корректное значение
        while True:

            try:
                # Ввод пользователя
                user_input: int = int(input("\nВыберите действие: "))

                # Число должно быть положительным и не превышать
                # количество доступных дейтсвий.
                if 1 <= user_input <= len(self._options):
                    break

                raise ValueError  # Ввод пользователя не удовлетворяет условие

            # Пользователь ввёл некорректный тип данных (не число)
            # или число не входит в множество доступных действий
            except ValueError:
                print("\nНекорректный ввод!")
                print(f"Введите число от 1 до {len(self._options)}.")

        return user_input

    def show(self) -> None:
        """Запуск работы приложения."""
        # Вывод логотипа и описания приложения
        # Выводится один раз при запуске приложения
        print(f"\n{config.APP_LOGO}\n\n{config.APP_DESCRIPTION}")

        while True:
            print()  # Просто для более красивого вывода

            # Вывод списока доступных действий
            for i, option in enumerate(self._options):
                print(f"[{i + 1}] {option.button_text}")

            # Запрос у пользователя выбора действия
            option: int = self._input_user_choice()

            # Выполнение модуля согласно выбора пользователя
            self._options[option - 1].show()
