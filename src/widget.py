from src import masks
from datetime import datetime


def mask_account_card(account_card: str) -> str:
    """Функция для обработки ифнормации о картах и счетах"""

    name_card = ""
    num_card = ""
    list_card = account_card.split()

    for i in list_card:
        if i.isdigit():
            num_card += i
        elif i.isalpha():
            name_card += i + " "
    if len(num_card) == 16:
        return f"{name_card.strip()} {masks.get_mask_card_number(num_card)}"

    else:
        return f"{name_card.strip()} {masks.get_mask_account(num_card)}"


def get_data(data: str) -> str:
    """Функция для обработки даты"""

    try:
        date_obj = datetime.fromisoformat(data)
        formatted_date = date_obj.strftime("%d.%m.%Y")
    except ValueError:
        formatted_date = ""

    return formatted_date
