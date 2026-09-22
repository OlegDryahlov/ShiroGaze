# -*- coding: utf-8 -*-
"""Поиск по имени пользователя."""

import requests
from progress.bar import Bar

import config


class SearchByUsername:
    """Поиск по имени пользователя."""

    def __init__(self):
        """Инициализация класса."""
        # Шкала прогресса поиска по сайтам
        self._progress_bar: Bar = Bar(
            fill=config.PROGRESS_BAR_FILL,
            max=len(config.TARGET_URLS),
            message=config.PROGRESS_BAR_MESSAGE,
            width=config.PROGRESS_BAR_WIDTH
        )

        # Словарь с результатом поиска по сайтам
        self._result: dict = {
            "found": [],
            "not found": []
        }

        self._target_urls: dict = config.TARGET_URLS

    def _get_username(self) -> str:
        """Запрашивает у пользователя ввод имени пользователя.

        Returns:
            str: Имя пользователя.
        """
        while True:
            # Ввод имени пользователя
            username: str = input("\nВведите имя пользователя: ")

            # Имя пользователя не может быть пустым. Самая минимальная
            # проверка. Если имя пользователя не пустое - прерывает цикл
            if len(username.strip()) != 0:
                break

            # Сообщение о некорректом вводе
            print("\nНекорректный ввод!")
            print("Имя пользователя не может быть пустым.")

        return username

    def _output_result(self) -> None:
        """Выводит результат поиска пользователю."""
        print(f"\n\nНайдено резульататов: {len(self._result['found'])}")

        # Наибольшая длина названия сайта из списка
        # Используется для более красивого вывода
        max_len: int = len(max([i[0] for i in self._result["found"]], key=len))

        # Вывод результата поиска
        for i in self._result["found"]:
            site = i[0].ljust(max_len, " ")  # Название сайта
            url = i[1]  # Ссылка на профиль пользователя
            print(f"{site} | {url}")

    def _search_by_username(self, username: str) -> None:
        """Выполняет поиск по имени пользователя.

        Args:
            username (str): Имя пользователя.
        """
        print()  # Просто для более красивого вывода

        for site, urls in self._target_urls.items():

            # Показывает в шкале прогресса сайт к которому идёт запрос
            self._progress_bar.suffix = config.PROGRESS_BAR_SUFFIX_BASE.format(
                site=site
            )
            # Ссылка на профиль пользователя на сайте
            url: str = urls["url_user"].format(username)

            try:
                # Статус код запроса на профиль пользователя
                status_code: int = requests.get(url, timeout=5).status_code

                # Статус код "The HTTP 200 OK" зачастую указывает на наличие
                # профиля пользователя на сайте. Будет улучшено в дальнейшем
                if status_code == 200:
                    self._result["found"].append([site, url])
                else:
                    self._result["not found"].append([url, "None"])

            # Может быть ошибка при установке соединения. Например, если
            # доступ к сайту в регионе заблокирован. Будет улучшено
            except Exception as e:
                self._result["not found"].append([url, e])

            self._progress_bar.next()

    def show(self):
        # Выводит информацию о действии
        print("\n[Поиск по имени пользователя]")
        print("Выполняет поиск по 400+ сайтам по указанному имени "
              "пользователя.\nНаходится в разработке, будет улучшен "
              "в следующих обновлениях.")

        # Запрашивает ввод имени пользователя
        username: str = self._get_username()

        # Выполняет поиск имени пользователя по ресурсам
        self._search_by_username(username=username)

        # Выводит результат поиска пользователю
        self._output_result()
