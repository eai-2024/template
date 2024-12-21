import pandas as pd
from vkapi.session import Session
import typing as tp
import time
import requests


class APIError(Exception):
    pass


def get_posts_2500(
    owner_id: str = "",
    domain: str = "",
    offset: int = 0,
    count: int = 10,
    max_count: int = 2500,
    filter: str = "owner",
    extended: int = 0,
    fields: tp.Optional[tp.List[str]] = None,
) -> tp.List[tp.Dict[str, tp.Any]]:
    """
    Функция для получения постов с использованием API ВКонтакте с учетом возможных ограничений.
    """
    session = Session(base_url="https://api.vk.com/method")
    params = {
        "owner_id": owner_id,
        "domain": domain,
        "offset": offset,
        "count": min(count, max_count),
        "filter": filter,
        "extended": extended,
        "fields": ",".join(fields) if fields else "",
        "v": "5.81",
    }

    response = session.get("wall.get", params=params)
    data = response.json()

    if "error" in data:
        raise APIError(data["error"]["error_msg"])

    return data.get("response", {}).get("items", [])


##def get_wall_execute(domain, count=1):
##    url = "https://api.vk.com/method/wall.get"
##    params = {
##        "domain": domain,
##        "count": count,
##        "v": "5.81"
##    }
##
##    response = requests.get(url, params=params)
##
##    # Проверяем успешность запроса
##    if response.status_code == 200:
##        data = response.json()
##        # Возвращаем нужные данные
##        return data['response']['items']
##    else:
##        # Если запрос не успешен
##        return f"Error: {response.status_code}"


def get_wall_execute(domain: str, count: int = 10) -> pd.DataFrame:
    """
    Получает посты со стены пользователя с использованием метода execute.
    """
    session = Session(base_url="https://api.vk.com/method")

    # Подготовка кода для метода execute
    execute_code = f"""
    return API.wall.get({{
        "domain": "{domain}",
        "count": {count},
        "v": "5.81"
    }});
    """

    # delay_per_request = max(2.0 / (count // 2500 + 1), 0.5)  # Задержка зависит от количества запросов
    time.sleep(2)  # стало быстро

    # Отправка POST-запроса
    response = session.post(
        "execute",
        data={"code": execute_code, "v": "5.81"},
    )
    data = response.json()

    if "error" in data:
        raise APIError(data["error"]["error_msg"])

    # Преобразование результата в DataFrame
    items = data["response"]["items"]
    return pd.json_normalize(items)
