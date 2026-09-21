# -*- coding: utf-8 -*-
"""ShiroGaze - Простой инструмент для OSINT."""

from menu import Menu


def main() -> None:
    """If __name__ == '__main__'."""
    menu_main: Menu = Menu()
    menu_main.show()


if __name__ == "__main__":
    main()
