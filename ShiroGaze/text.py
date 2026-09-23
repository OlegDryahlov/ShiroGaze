# -*- coding: utf-8 -*-
"""Поиск по имени пользователя."""

import os

import config


_text: dict | None = None


def __clear() -> None:  # Заготовка на будущее
    print("\033[H\033[2J", end="")


def get_text(text_header: str) -> dict | str:
    """Возвращает текст по указанным заголовкам.

    Args:
        text (str): Заголовок текста в файле "data/text.toml"
            Например: menu.app.logo

    Returns:
        dict | str: Вернёт строку в случае, если указан полный путь к заголовку
            текста. Вернёт словарь в противном случае. Например, если указазать
            в качестве заголовка "menu.app" вернёт словарь, содержащий значения
            "logo" и "description" (см. файл "data/text.toml").

    """
    # Полный путь к запрашиваему тексту
    text_path: list[str] = text_header.split(".")

    # Входим в первый заголовок
    text_output: dict | str = _text[text_path[0]]

    # Проходим по всем указанным заголовкам, начиная со второго
    for header in text_path[1:]:
        text_output = text_output[header]

    return text_output


def init(text_data: dict) -> None:
    """Указывает приложению откуда брать текст для вывода.

    Args:
        text_data (dict): Словарь с текстом для приложения.
    """
    global _text
    _text = text_data
