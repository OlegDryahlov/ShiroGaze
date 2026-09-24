# -*- coding: utf-8 -*-
"""
Модуль "Поиск по имени пользователя".

Выполняет поиск по имени пользователя с помощью библиотеки requests по
базе ресурсов из файла конфигурации.
"""

from concurrent.futures import as_completed, ThreadPoolExecutor

import requests
from progress.bar import Bar
from rich import console, print, table

import config
from .options import option_confirm
from utils.text import get_text as t


class SearchByUsername:
    """
    Модуль "Поиск по имени пользователя".

    Запрашивает у пользователя приложения имя пользователя для поиска и
    выполняет поиск по имеющейся базе ссылок.
    """

    def __init__(self):
        """Инициализация модуля."""
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
            print(t("SBU.input.message"), end="")
            username: str = input()

            # Имя пользователя не может быть пустым. Самая минимальная
            # проверка. Если имя пользователя не пустое - прерывает цикл
            if len(username.strip()) != 0:
                break

            print(t("SBU.input.error"))

        return username

    def _output_result(self) -> None:
        """Выводит результат поиска пользователю в виде таблицы."""
        result_table: table.Table = table.Table(
            title=t("SBU.output.table.title").format(
                results_length=len(self._result["found"])
            )
        )
        result_table.add_column(t("SBU.output.column.site"))
        result_table.add_column(t("SBU.output.column.url"))
        for i in self._result["found"]:
            result_table.add_row(*i)

        con: console.Console = console.Console()
        con.print(result_table)

    def _search_by_username(self, username: str) -> None:
        """Выполняет поиск по имени пользователя.

        Args:
            username (str): Имя пользователя.
        """
        print()  # Просто для более красивого вывода

        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_platform = {
                executor.submit(
                    self._send_request, url["url_user"], username
                ): site
                for site, url in self._target_urls.items()
            }
            for future in as_completed(future_to_platform):
                site: str = future_to_platform[future]
                self._progress_bar.suffix = \
                    config.PROGRESS_BAR_SUFFIX_BASE.format(site=site)
                try:
                    result = future.result()
                    if result:
                        self._result["found"].append([site, result])
                except Exception:
                    pass
                self._progress_bar.next()
            self._progress_bar.finish()


    def _send_request(self, url: str, username: str) -> str | None:
        url: str = url.format(username)
        try:
            status_code: int = requests.get(url, timeout=5).status_code
            if status_code == 200:
                return url
            return None
        except Exception:
            return None

    def show(self) -> None:
        """
        Запуск модуля.

        Выполняет поиск по списку ресурсов по указанному имени пользователя.
        """
        print(t("SBU.message"), end="\n\n")  # Выводит информацию о действии

        # Запрашивает подтверждение действия
        if not option_confirm():  # (защита от неправильного ввода)
            return

        username: str = self._get_username()  # Ввод имени пользователя

        # Выполняет поиск имени пользователя по ресурсам
        self._search_by_username(username=username)

        self._output_result()  # Выводит результат поиска пользователю
