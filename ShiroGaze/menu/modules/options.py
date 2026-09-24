# -*- coding: utf-8 -*-
"""Удобные опции, позволяющие улучшить пользовательский интерфейс."""

from rich import print

from utils.text import get_text as t


def option_confirm() -> bool:
    """Запрашивает у пользователя подтверждение на продолжение действия.

    Returns:
        bool: True, если пользователь ввёл "Y" или "y",
            в противном случае False.
    """
    message: str = t("options.confirm.message")
    print(message, end="")

    if input().lower() == "y":
        return True

    message_interrupted: str = t("options.confirm.interrupted")
    print("\n" + message_interrupted)
    return False


def option_continue() -> None:
    """Запрашивает у пользователя ввод ENTER для продолжения действия."""
    message: str = t("options.continue.message")
    print(message)
    input()
