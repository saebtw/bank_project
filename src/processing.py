def filter_by_state(data: list) -> list:
    """Функция фильтрации"""

    state = "EXECUTED"
    filtered_items = []

    for item in data:
        if item.get("state") == state:
            filtered_items.append(item)
    return filtered_items
