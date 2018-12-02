import pytest

from src.day2.day2 import ID


@pytest.mark.parametrize("test_input,expected", [
    (("abaac", 3), True),
    (("abbc", 2), True),
    (("abbc", 3), False),
    (("abbcba", 2), True),
    (("abbcba", 3), True),
])
def test_id_char_counter(test_input, expected):
    id_char_counter = ID(test_input[0])
    result = id_char_counter.repeated(test_input[1])
    assert result == expected

