# filter_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
#
# state_dict = {'state': 'EXECUTED'}
#
# new_dict = {}
#
# for filt in filter_list:
#     if state_dict[] in filt['state']:

# def filter_by_state(data, state='EXECUTED'):
#     filtered_items = []
#     for item in data:
#         if item.get('state') == state:
#             filtered_items.append(item)
#     return filtered_items
# data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
# filtered_data = filter_by_state(data)
# print(filtered_data)

# def filter_by_state(data: list) -> list:
#     """Функция фильтрации"""
#
#     state = "EXECUTED"
#     filtered_items = []
#
#     for item in data:
#         if item.get("state") == state:
#             filtered_items.append(item)
#     return filtered_items
#
# data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
# filtered_data = filter_by_state(data)
# print(filtered_data)