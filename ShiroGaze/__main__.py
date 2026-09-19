# -*- coding: utf-8 -*-
"""ShiroGaze - Простой инструмент для OSINT."""

import json
import requests
from progress.bar import Bar

import config
from progress_bar import ProgressBar
from load_file import load_file


# Шкала прогресса поиска по имени пользователя
progress_bar: Bar = Bar(
    fill=config.PROGRESS_BAR_FILL,
    max=len(config.TARGET_URLS),
    message=config.PROGRESS_BAR_MESSAGE,
    width=config.PROGRESS_BAR_WIDTH
)

# Список найденных профилей по имени пользователя
success: list[list[str, str]] = []


def main() -> None:
    """If __name__ == '__main__'."""
    print(config.APP_LOGO)
    print(config.APP_DESCRIPTION)
    username = input("Введите имя пользователя: ")
    for key, val in config.TARGET_URLS.items():
        progress_bar.suffix = config.PROGRESS_BAR_SUFFIX_BASE.format(site=key)
        url: str = val["url_user"].format(username)
        try:
            status_code: int = requests.get(url, timeout=5).status_code
            if status_code == 200:
                success.append([key, url])
        except:
            pass
        progress_bar.next()
    print(f"\nНайдено результатов: {len(success)}")
    for i in success:
        print(f"{i[0]}: {i[1]}")


if __name__ == "__main__":
    main()
