import pytest

def test_log(capsys):
    with pytest.raises(Exception):
        captured = capsys.readouterr()
        assert captured.out == f"my_function error: {e}. Inputs:{args}, {kwargs}\n"
