import masks


def mask_account_card(account_card: str) -> str:
    """Функция для обработки ифнормации о картах и счетах"""

    name_card = ""
    num_card = ""
    list_card = account_card.split()

    for i in list_card:
        if i.isdigit():
            num_card += i
        elif i.isalpha():
            name_card += i
    if len(num_card) == 16:
        return f"{name_card} {masks.get_mask_card_number(num_card)}"

    else:
        return f"{name_card} {masks.get_mask_account(num_card)}"


def get_data(data: str) -> str:
    """Функция для обработки даты"""

    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"
