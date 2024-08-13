from src.widget import mask_account_card, get_data

import pytest


@pytest.mark.parametrize(
    "inp, ans",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(inp: str, ans: str) -> None:
    assert mask_account_card(inp) == ans


@pytest.mark.parametrize(
    "inp, ans",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("0001-01-01T00:00:00.000000", "01.01.0001"),
        ("9999-12-31T23:59:59.999999", "31.12.9999"),
        ("", ""),
    ],
)
def test_get_data(inp: str, ans: str) -> None:
    assert get_data(inp) == ans
