import dataclasses
import typing as tp
from typing import Optional, List, Union
import requests
from vkapi import config
from vkapi.exceptions import APIError
import time

QueryParams = tp.Optional[tp.Dict[str, tp.Union[str, int]]]

@dataclasses.dataclass(frozen=True)
class FriendsResponse:
    count: int
    items: tp.Union[tp.List[int], tp.List[tp.Dict[str, tp.Any]]]

def get_friends(
    user_id: int, count: int = 5000, offset: int = 0, fields: tp.Optional[tp.List[str]] = None
) -> FriendsResponse:
    """
    Получить список идентификаторов друзей пользователя или расширенную информацию
    о друзьях пользователя (при использовании параметра fields).
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert fields is None or isinstance(fields, list), "fields must be list of strings or None"

    query_params = {
        "access_token": config.VK_CONFIG["access_token"],
        "user_id": user_id,
        "count": count,
        "offset": offset,
        "fields": ",".join(fields) if fields else "",
        "v": config.VK_CONFIG["version"],
    }

    response = requests.get(f"{config.VK_CONFIG['domain']}/friends.get", params=query_params)
    if response.status_code != 200:
        raise APIError(f"Error during API request: {response.text}")
    data = response.json()
    if "error" in data:
        raise APIError(data["error"]["error_msg"])
    return FriendsResponse(
        count=data["response"]["count"], items=data["response"]["items"]
    )

class MutualFriends(tp.TypedDict):
    id: int
    common_friends: tp.List[int]
    common_count: int

def get_mutual(
    source_uid: Optional[int] = None,
    target_uid: Optional[int] = None,
    target_uids: Optional[List[int]] = None,
    count: Optional[int] = 100,
    offset: int = 0
) -> Union[List[MutualFriends], List[int]]:
    """
    Получить список идентификаторов общих друзей между парой пользователей или группой пользователей.

    :param source_uid: Идентификатор исходного пользователя.
    :param target_uid: Идентификатор целевого пользователя.
    :param target_uids: Список идентификаторов целевых пользователей.
    :param count: Количество общих друзей для возврата.
    :param offset: Смещение для пагинации.
    :return: Список общих друзей с их полями (или список идентификаторов, если целевой список пуст).
    """
    
    # Проверка, что хотя бы один из идентификаторов целевых пользователей передан
    if not target_uid and not target_uids:
        raise ValueError("Target user ID or target user IDs must be provided.")

    # Параметры запроса к API
    query_params = {
        "access_token": config.VK_CONFIG["access_token"],
        "source_uid": source_uid,
        "target_uid": target_uid,
        "target_uids": ",".join(map(str, target_uids)) if target_uids else None,
        "count": count,
        "offset": offset,
        "v": config.VK_CONFIG["version"],  # Версия API
    }

    try:
        # Выполнение GET-запроса к API
        response = requests.get(f"{config.VK_CONFIG['domain']}/friends.getMutual", params=query_params)
        response.raise_for_status()  # Если статус не 200, выбрасываем исключение
    except requests.exceptions.RequestException as e:
        raise APIError(f"Error during API request: {e}")

    # Получаем данные из ответа
    data = response.json()

    # Проверяем наличие ошибок в ответе
    if "error" in data:
        raise APIError(data["error"]["error_msg"])

    mutual_friends: List[MutualFriends] = []

    # Процессируем полученные данные
    for item in data["response"]:
        if isinstance(item, dict):  # Убедимся, что это словарь
            mutual_friends.append({
                "id": item["id"],  # Добавляем id
                "common_friends": item.get("common_friends", []),  # Если данных нет, то пустой список
                "common_count": item.get("common_count", 0)  # Если данных нет, то 0
            })

    # Добавляем задержку между запросами, чтобы избежать превышения лимитов
    time.sleep(1)

    # Возвращаем список общих друзей
    return mutual_friends






