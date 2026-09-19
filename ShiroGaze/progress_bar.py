# -*- coding: utf-8 -*-
"""Классы шкал прогресса приложения."""

from progress.bar import Bar


class ProgressBar(Bar):
    """Шкала прогресса при поиске пользователя."""
    fill: str = "#"
    message: str = "Поиск по имени пользователя"
    suffix: str = "(%(index)d / %(max)d)"
    suffix_base: str = "(%(index)d / %(max)d) | {site}"
    width: int = 24

    def __init__(self, **args):
        super().__init__(self, **args)
        self.message = ProgressBar.message
