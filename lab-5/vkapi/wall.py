import pandas as pd
from vkapi.session import Session
import typing as tp


def get_posts_2500(
    owner_id: str = "",
    domain: str = "",
    offset: int = 0,
    count: int = 10,
    max_count: int = 2500,
    filter: str = "owner",
    extended: int = 0,
    fields: tp.Optional[tp.List[str]] = None,
) -> tp.Dict[str, tp.Any]:
    pass

def get_wall_execute(
    domain: str, count: int = 10
) -> pd.DataFrame:
    session = Session(base_url="https://api.vk.com/method")
    
    # Используем POST вместо GET для метода execute
    response = session.post(
        "execute",
        data={"domain": domain, "count": count, "v": "5.126"},
    )
    
    data = response.json()
    if "error" in data:
        raise APIError(data["error"]["error_msg"])
    
    total_count = data["response"]["count"]
    print(f"Total records: {total_count}")
    
    # Теперь выполняем GET для получения данных с нужным total_count
    response = session.get(
        "wall.get", params={"domain": domain, "count": total_count, "v": "5.81"}
    )
    return pd.json_normalize(response.json()["response"]["items"])





