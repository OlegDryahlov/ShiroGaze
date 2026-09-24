# -*- coding: utf-8 -*-
"""Поиск по имени пользователя."""

import requests
from progress.bar import Bar
from rich import print
from rich.console import Console
from rich.table import Table

import config
from .options import option_confirm
from utils.text import get_text as t


class SearchByUsername:
    """Поиск по имени пользователя."""

    def __init__(self):
        """Инициализация класса."""
        self.__button_text: str = t("SBU.button")

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

    @property
    def button_text(self) -> str:
        """Текст кнопки (опции) в меню приложения."""
        return self.__button_text

    def _get_username(self) -> str:
        """Запрашивает у пользователя ввод имени пользователя.

        Returns:
            str: Имя пользователя.
        """
        while True:
            # Ввод имени пользователя
            print(t("SBU.input.message"), end="")
            username: str = input()

            # Имя пользователя не может быть пустым. Самая минимальная
            # проверка. Если имя пользователя не пустое - прерывает цикл
            if len(username.strip()) != 0:
                break

            # Сообщение о некорректом вводе
            print(t("SBU.input.error"))

        return username

    def _output_result(self) -> None:
        """Выводит результат поиска пользователю."""
        table: Table = Table(
            title=t("SBU.output.table.title").format(
                results_length=len(self._result["found"])
            )
        )
        table.add_column(t("SBU.output.column.site"))
        table.add_column(t("SBU.output.column.url"))
        for i in self._result["found"]:
            table.add_row(*i)

        console: Console = Console()
        console.print(table)

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

    def show(self) -> None:
        """
        Запуск модуля.

        Выполняет поиск по списку ресурсов по указанному имени пользователя.
        """
        # Выводит информацию о действии
        print(t("SBU.message"), end="\n\n")

        if not option_confirm():
            return

        # Запрашивает ввод имени пользователя
        username: str = self._get_username()

        # Выполняет поиск имени пользователя по ресурсам
        self._search_by_username(username=username)

        # Выводит результат поиска пользователю
        self._output_result()
