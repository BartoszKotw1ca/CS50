from bank import value

def test1():
    assert value("hello") == 0
    assert value("Hello there") == 0
    assert value("  hello") == 0

def test2():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("howdy") == 20

def test3():
    assert value("greetings") == 100
    assert value("good morning") == 100
    assert value("  good night") == 100

if __name__ == "__main__":
    test1()
    test2()
    test3()
    print("All tests passed.")
