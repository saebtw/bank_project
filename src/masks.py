def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера банковской карты"""

    if card_number.isdigit() and len(card_number) >= 16:
        return f"{card_number[:5]} {card_number[5:7]}* ** {card_number[13:]}"
    else:
        return card_number


def get_mask_account(number_account: str) -> str:
    """Функция маскировки номера банковского счета"""

    if number_account.isdigit() and len(number_account) >= 20:

        return f"{'**'}{number_account[-4:]}"
    else:
        return number_account
