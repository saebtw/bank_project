def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера банковской карты"""

    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    elif len(card_number) > 16:
        return "Номер карты длиннее 16 символов"
    elif len(card_number) > 0 and len(card_number) >= 0:
        return "Номер карты короче 16 символов"
    elif card_number == "":
        return "Номер карты не указан"
    else:
        return card_number


def get_mask_account(number_account: str) -> str:
    """Функция маскировки номера банковского счета"""

    if number_account.isdigit() and len(number_account) == 20:

        return f"{'**'}{number_account[-4:]}"
    elif len(number_account) > 20:
        return "Номер счета длиннее 20 символов"
    elif len(number_account) > 0 and len(number_account) >= 0:
        return "Номер счета короче 20 символов"
    elif number_account == "":
        return "Номер счета не указан"
    else:
        return number_account
