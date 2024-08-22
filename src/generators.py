def filter_by_currency(transactions_list, currency):
    """Функция фильтрации операций по валюте"""

    if len(transactions_list) > 0:
        filtered_transactions = filter(
            lambda transactions_list: transactions_list.get("operationAmount").get("currency").get("code") == currency,
            transactions_list,
        )
        return filtered_transactions
    else:
        return "Список пустой!"


def transaction_descriptions(transactions_list):
    """Функция вывода описания операций"""

    if len(transactions_list) > 0:
        for element in transactions_list:
            yield element.get("description")
    else:
        yield "Список пустой!"


def card_number_generator(start, stop):
    """Функция генерациии номера карт в заданном диапазоне"""

    while start <= stop:
        str_num = str(start)
        while len(str_num) < 16:
            str_num = "0" + str_num
        formatted_card_num = str_num[0:4] + " " + str_num[4:8] + " " + str_num[8:12] + " " + str_num[12:]
        yield formatted_card_num
        start += 1
