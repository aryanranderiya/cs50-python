from plates import is_valid

def test_valid() :
    assert is_valid("CS50") == True
    assert is_valid("aryan") == True
    assert is_valid("khyati") == True
    assert is_valid("AR78") == True


def test_invalid() :
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("123") == False
    assert is_valid("50CS") == False

