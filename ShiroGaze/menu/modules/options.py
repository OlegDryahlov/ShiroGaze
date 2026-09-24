# -*- coding: utf-8 -*-
"""Опции, позволяющие улучшить пользовательский интерфейс."""

from rich import print

from utils.text import get_text as t


def option_confirm() -> bool:
    """Запрашивает у пользователя подтверждение на продолжение действия.

    Returns:
        bool: True, если пользователь ввёл "Y" или "y",
            в противном случае False.
    """
    print(t("options.confirm.message"), end="")

    if input().lower() == "y":
        return True

    print(t("options.confirm.interrupted"))
    return False


def option_continue() -> None:
    """Запрашивает у пользователя ввод ENTER для продолжения действия."""
    print(t("options.continue.message"))
    input()
