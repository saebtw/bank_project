from src.masks import get_mask_card_number, get_mask_account

import pytest


def test_get_mask_card_number(card_num: str, card_num_less: str, card_num_more: str, card_num_nothing: str) -> None:
    assert get_mask_card_number(card_num) == "7000 79** **** 6361"

    assert get_mask_card_number(card_num_more) == "Номер карты длиннее 16 символов"

    assert get_mask_card_number(card_num_less) == "Номер карты короче 16 символов"

    assert get_mask_card_number(card_num_nothing) == "Номер карты не указан"


@pytest.mark.parametrize(
    "inp_num, ans",
    [
        ("73654108430135874305", "**4305"),
        ("7365410843013587430554", "Номер счета длиннее 20 символов"),
        ("736541084301358", "Номер счета короче 20 символов"),
        ("", "Номер счета не указан"),
    ],
)
def test_get_mask_account(inp_num: str, ans: str) -> None:
    assert get_mask_account(inp_num) == ans
