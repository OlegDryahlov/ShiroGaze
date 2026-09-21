import requests
from progress.bar import Bar

import config


class SearchByUsername:

    def __init__(self):
        ...

    def _get_username(self) -> str:
        while True:
            user_input: str = input("\nВведите имя пользователя: ")
            if len(user_input.strip()) != 0: break
            print("\nНекорректный ввод!")
            print("Имя пользователя не может быть пустым.")
        return user_input

    def _output_result(self, result):
        print(f"\n\nНайдено резульататов: {len(result['found'])}")
        max_len = len(max([i[0] for i in result["found"]], key=len))
        for i in result["found"]:
            site = i[0].ljust(max_len, " ")
            url = i[1]
            print(f"{site} | {url}")

    def _search_by_username(self, username):
        print()
        progress_bar: Bar = Bar(
            fill=config.PROGRESS_BAR_FILL,
            max=len(config.TARGET_URLS),
            message=config.PROGRESS_BAR_MESSAGE,
            width=config.PROGRESS_BAR_WIDTH
        )
        result: dict = {
            "found": [],
            "not found": []
        }
        for site, urls in config.TARGET_URLS.items():
            progress_bar.suffix = config.PROGRESS_BAR_SUFFIX_BASE.format(site=site)
            url: str = urls["url_user"].format(username)
            try:
                status_code: int = requests.get(url, timeout=5).status_code
                if status_code == 200:
                    result["found"].append([site, url])
                else:
                    result["not found"].append([url, "None"])
            except Exception as e:
                result["not found"].append([url, e])
            progress_bar.next()
        self._output_result(result=result)

    def show(self):
        print("\nПоиск по имени пользователя.")
        print("Выполняет поиск по 400+ сайтам по выбранному имени пользователя.")
        username: str = self._get_username()
        self._search_by_username(username=username)
