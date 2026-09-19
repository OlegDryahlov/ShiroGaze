# -*- coding: utf-8 -*-
"""ShiroGaze - Простой инструмент для OSINT."""

import json
import requests

import config
from progress_bar import ProgressBar
from load_file import load_file


def main() -> None:
    """If __name__ == '__main__'."""
    print(config.APP_LOGO)
    print(config.APP_DESCRIPTION)
    username = str(input("Введите имя пользователя: "))
    bar = ProgressBar(ProgressBar.message, max=len(config.TARGET_URLS))
    success = []
    for key, val in config.TARGET_URLS.items():
        bar.suffix = bar.suffix_base.format(site=key)
        url = val["url_user"].format(username)
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                success.append([key, url])
        except:
            pass
        bar.next()
    print(f"\nНайдено результатов: {len(success)}")
    for i in success:
        print(f"{i[0]}: {i[1]}")


if __name__ == "__main__":
    main()
