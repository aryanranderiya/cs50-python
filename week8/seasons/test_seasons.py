from datetime import date
from seasons import userinput, convert_to_minutes
import pytest

valid_input = "2000-01-01"
invalid_input = "01-01-2000"

def test_userinput_valid():
    result = userinput(valid_input)
    assert result == valid_input

def test_userinput_invalid():
    with pytest.raises(SystemExit):
        userinput(invalid_input)

def test_convert_to_minutes():
    result = convert_to_minutes("2000-01-01")
    assert result is None
