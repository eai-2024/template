import typing as tp
from statistics import median
from vkapi.friends import get_friends

def age_predict(user_id: int) -> tp.Optional[float]:
    """
    Прогноз возраста пользователя на основе возрастов его друзей.
    """
    friends = get_friends(user_id, fields=["bdate"]).items
    ages = []
    for friend in friends:
        try:
            bdate = friend.get("bdate")
            if bdate and bdate.count(".") == 2:
                year = int(bdate.split(".")[2])
                age = 2024 - year  # Замените на динамический год
                ages.append(age)
        except ValueError:
            continue
    return median(ages) if ages else None
