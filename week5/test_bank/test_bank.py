from bank import value

def test_twenty ():
    assert value("hi") == 20
    assert value("heyyyy") == 20
    assert value("heyHEYhey") == 20
    assert value("heyaryan") == 20
    assert value("heykhyati") == 20

def test_zero() :
    assert value("hellooooo") == 0
    assert value("Hellooooo") == 0
    assert value("hellooooo123") == 0

def test_hundred() :
    assert value("wassup") == 100
    assert value("wassupAryan") == 100
    assert value("wassupKhyati") == 100
