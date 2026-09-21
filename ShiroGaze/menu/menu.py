import sys

import config
from .about import About
from .search_by_username import SearchByUsername


class Menu:

    def __init__(self):
        self._about = About()
        self._search_by_username = SearchByUsername()
        self._options: dict = {
            1: {
                "text": "Поиск по имени пользователя",
                "action": self._search_by_username.show
            },
            2: {
                "text": "О программе",
                "action": self._about.show
            },
            3: {
                "text": "Выход",
                "action": sys.exit
            }
        }

    def _input_user_choice(self) -> int:
        while True:
            try:
                user_input: int = int(input("\nВыберите действие: "))
                if 1 <= user_input <= len(self._options):
                    break
                raise Exception
            except Exception:
                print("\nНекорректный ввод!")
                print(f"Введите число от 1 до {len(self._options)}.")
        return user_input

    def show(self):
        print(f"\n{config.APP_LOGO}\n\n{config.APP_DESCRIPTION}")

        while True:
            print("\n")

            for key, option in self._options.items():
                print(f"[{key}] {option['text']}")
            
            option: int = self._input_user_choice()
            self._options[option]['action']()
