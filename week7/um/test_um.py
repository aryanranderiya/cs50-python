from um import count

def test() :
    assert count("yummy") == 0
    assert count("hi um hi") == 1
    assert count("UM.... HI") == 1