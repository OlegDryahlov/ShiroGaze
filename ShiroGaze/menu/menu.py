# -*- coding: utf-8 -*-
"""Главный управляющий класс."""

import sys

import config
from .about import About
from .search_by_username import SearchByUsername


class Menu:
    """
    Главный управляющий класс.

    Запускается первым, из него вызываются все остальные действия.
    """

    def __init__(self):
        """Инициализация класса. """
        self._about: About = About()  # Действие "О приложении"

        self._run: bool = True  # Флаг работы приложения

        # Действие "Поиск по имени пользователя"
        self._search_by_username: SearchByUsername = SearchByUsername()

        # Словарь действий доступных пользователю, где:
        # ключ - текст с описанием действия, который будет выведен пользователю
        # значение - функция, которая будет выполнения действием
        self._options: dict = {
            "Поиск по имени пользователя": self._search_by_username.show,
            "О программе": self._about.show,
            "Выход": self._exit
        }

    def _exit(self) -> None:
        """Переключает флаг работы приложения на False."""
        self._run = False

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

        while self._run:
            print()  # Просто для более красивого вывода

            # Вывод списока доступных действий
            for i, option in enumerate(self._options.keys()):
                print(f"[{i + 1}] {option}")

            # Запрос у пользователя выбор действия
            option: int = self._input_user_choice()

            # Выполнение функции согласно выбора пользователя
            list(self._options.values())[option - 1]()

        # Выполняется, если пользователь выберет действие "Выход":
        # будет вызвана функция self._exit(), которая установит значение
        # self._run = False, что позволит выйти из цикла while
        print("\nЗавершение работы.")
        sys.exit()
