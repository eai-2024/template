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


class MutualFriends(tp.TypedDict):
    id: int
    common_friends: tp.List[int]
    common_count: int


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

    query_params: QueryParams = {
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

    return FriendsResponse(count=data["response"]["count"], items=data["response"]["items"])


def get_mutual(
    source_uid: Optional[int] = None,
    target_uid: Optional[int] = None,
    target_uids: Optional[List[int]] = None,
    count: Optional[int] = 100,
    offset: int = 0,
) -> Union[List[MutualFriends], List[int]]:
    """
    Получить список идентификаторов общих друзей между парой пользователей или группой пользователей.
    """
    if not target_uid and not target_uids:
        raise ValueError("Target user ID or target user IDs must be provided.")

    result: Union[List[MutualFriends], List[int]] = []

    if target_uids is not None and len(target_uids) > 100:
        # Handle cases where target_uids exceeds 100 by splitting into chunks
        for i in range(0, len(target_uids), 100):
            chunk = target_uids[i:i + 100]
            result.extend(
                get_mutual(
                    source_uid=source_uid, target_uids=chunk, count=count, offset=offset
                )
            )
            time.sleep(0.34)  # To avoid exceeding request rate limits
        return result

    query_params: QueryParams = {
        "access_token": config.VK_CONFIG["access_token"],
        "source_uid": source_uid or 0,  # Используйте значения по умолчанию, если None
        "target_uid": target_uid or 0,
        "target_uids": ",".join(map(str, target_uids)) if target_uids else None,
        "count": count,
        "offset": offset,
        "v": config.VK_CONFIG["version"],
    }

    response = requests.get(f"{config.VK_CONFIG['domain']}/friends.getMutual", params=query_params)
    if response.status_code != 200:
        raise APIError(f"Error during API request: {response.text}")

    data = response.json()

    if "error" in data:
        raise APIError(data["error"]["error_msg"])

    if target_uids is not None:
        if target_uid or len(target_uids) == 1:
            return data["response"]

        for item in data["response"]:
            result.append(
                {
                    "id": item["id"],
                    "common_friends": item.get("common_friends", []),
                    "common_count": item.get("common_count", 0),
                }
            )
        return result

    return data["response"]
