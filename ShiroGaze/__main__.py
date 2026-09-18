# -*- coding: utf-8 -*-
"""ShiroGaze - Простой инструмент для OSINT."""

import json
import requests

import config
from utils import load_file


def main() -> None:
    """If __name__ == '__main__'."""
    print(config.APP_LOGO)
    print(config.APP_DESCRIPTION)
    username = str(input("Введите имя пользователя: "))
    for key, val in config.TARGET_URLS.items():
        print("Проверяю сайт:", key)
        url = val["url_user"].format(username)
        print("\t", url)
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print("\t !!! Успех!")
            else:
                print("\t xxx Пользователь не найден.")
        except:
            print("\t xxx Пользователь не найден.")


if __name__ == "__main__":
    main()
