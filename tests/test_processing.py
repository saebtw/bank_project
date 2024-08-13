from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(my_filter_inp: list[dict[str, str]], my_filter_ans: list[dict[str, str]]) -> None:
    assert filter_by_state(my_filter_inp) == my_filter_ans


def test_sort_by_date(my_sort_ans: list[dict[str, str]], my_sort_inp: list[dict[str, str]]) -> None:
    assert sort_by_date(my_sort_inp) == my_sort_ans
