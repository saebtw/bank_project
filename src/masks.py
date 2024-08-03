def get_mask_card_number(card_number: str) -> None:
    """Функция для маскировки номера банковской карты"""

    if card_number.isdigit() and len(card_number) == 16:

        print(
            f"{card_number[:4]} {card_number[4:6]}{card_number[6:8].replace(card_number[6:8], '**')}"
            f" {card_number[8:12].replace(card_number[8:12], '****')} {card_number[12:]}"
        )
    else:
        return None


def get_mask_account(number_account: str) -> None:
    """Функция маскировки номера банковского счета"""

    if number_account.isdigit() and len(number_account) == 20:

        print(f"{'**'}{number_account[-4:]}")
    else:
        return None
