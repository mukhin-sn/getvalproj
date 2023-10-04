import pytest

from utils.dicts import get_val


def test_get_val():
    assert get_val({"key_1": "value_1", "key_2": "value_2"}, "key_3", "test") == "test"
    assert get_val({"key_1": "value_1", "key_2": "value_2"}, "key_1", "test") == "value_1"
    assert get_val({}, "key", "test") == "test"
