# -*- coding: utf-8 -*-
"""ShiroGaze - Простой инструмент для OSINT."""

import config
from search_by_username import search_by_username


def main() -> None:
    """If __name__ == '__main__'."""
    print(config.APP_LOGO)
    print(config.APP_DESCRIPTION)
    username = input("Введите имя пользователя: ")
    result: dict = search_by_username(username=username)
    print("\n\nНайдено результатов:", len(result["found"]))
    for i in result["found"]:
        print(i[0], i[1])


if __name__ == "__main__":
    main()
