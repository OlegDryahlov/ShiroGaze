# -*- coding: utf-8 -*-
"""ShiroGaze - Простой инструмент для OSINT."""

import json
import requests


def load_url():
    """Загружает файл со списком url-адресов."""
    with open("./data/url.json", mode="r") as f:
        data_url = json.load(f)
    return data_url


def main() -> None:
    """If __name__ == '__main__'."""
    with open("./data/logo.txt", mode="r") as f:
        data_logo = f.read()
    with open("./data/description.txt", mode="r") as f:
        data_desc = f.read()
    print(data_logo)
    print(data_desc)
    username = str(input("Введите имя пользователя: "))
    for key, val in list(load_url().items()):
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
