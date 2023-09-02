from numb3rs import validate

def test() :
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.999.999.999") == False
    assert validate("512.512.512.512") == False