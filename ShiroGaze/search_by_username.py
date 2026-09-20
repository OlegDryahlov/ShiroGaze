# ...
"..."

import requests
from progress.bar import Bar

import config


def search_by_username(username: str) -> dict:
    """_summary_

    Args:
        username (str): _description_

    Returns:
        dict: _description_
    """
    # Шкала прогресса поиска по имени пользователя
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
    return result
