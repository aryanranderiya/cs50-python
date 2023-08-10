from fuel import convert, gauge
import pytest


def test_full():
    assert gauge(convert("100/100")) == "F"
    assert gauge(convert("99/100")) == "F"


def test_empty():
    assert gauge(convert("0/100")) == "E"
    assert gauge(convert("1/100")) == "E"


def test_percentages():
    for i in range(10, 90, 10):
        assert gauge(convert(f"{i}/100")) == f"{i}%"
        i += 10


def test_value_error():
    with pytest.raises(ValueError):
        gauge(convert("one/two"))


def test_div_zero_error():
    with pytest.raises(ZeroDivisionError):
        gauge(convert("10/0"))
