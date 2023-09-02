from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

    try:
        jar = Jar(-5)
    except ValueError as e:
        assert str(e) == "Capacity cannnot be less than 0!"

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()

    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

    try:
        jar.deposit(10)
    except ValueError as e:
        assert str(e) == "Cannot exceed jar's capacity!"

def test_withdraw():
    jar = Jar(15)
    jar.deposit(10)

    jar.withdraw(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

    try:
        jar.withdraw(7)
    except ValueError as e:
        assert str(e) == "Cannot withdraw less than cookies in jar!"

def test_capacity():
    jar = Jar(25)
    assert jar.capacity == 25

def test_size():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(8)
    assert jar.size == 8
