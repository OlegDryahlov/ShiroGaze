# -*- coding: utf-8 -*-
"""ShiroGaze - Простой инструмент для OSINT."""

import config
from menu import Menu
from utils import text


def main() -> None:
    """If __name__ == '__main__'."""
    text.init(text_data=config.TEXT)
    menu_main: Menu = Menu()
    menu_main.show()


if __name__ == "__main__":
    main()
