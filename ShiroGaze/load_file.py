# -*- coding: utf-8 -*-
"""Функция чтения тектовых файлов и файлов данных."""

import pathlib

import json
import tomli


def load_file(file_path: pathlib.Path) -> str | dict:
    """
    Читает и возвращает текстовый файл (.txt) или файл данных (.json / .toml).

    Args:
        file_path (pathlib.Path): Путь к файлу.

    Returns:
        str: Данные .txt файла.
        dict: Данные .json / .toml файла.
    """
    file_path: str = str(file_path)

    if file_path.endswith(".toml"):
        with open(file_path, mode="rb") as fb:
            file_data: dict = tomli.load(fb)
        return file_data

    with open(file_path, mode="r", encoding="utf-8") as f:
        if file_path.endswith(".json"):
            file_data: dict = json.load(f)
        elif file_path.endswith(".txt"):
            file_data: str = f.read()

    return file_data
