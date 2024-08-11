# def mask_account_card(account_card : str) -> None:
#     """Функция для обработки ифнормации о картах и счетах"""
#
#     if 'Счет' in account_card:
#         return get_mask_account(account_card)
#     else:
#         cards = get_mask_card_number(account_card[-16:])
#         new_cards = account_card.replace(account_card[-16:], cards)
#         return new_cards
#
# print(mask_account_card('Счет 73654108430135874305'))
# print(mask_account_card('Visa Platinum 7000792289606361'))
# print(mask_account_card('Maestro 7000792289606361'))
