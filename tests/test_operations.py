from src.math_operations import add, sub, multiply

def test_add(a,b):
    assert add(2,3) == 5

    assert add(-1,1) == 0

def test_sub(a,b):
    assert sub(3,5) == -2
    assert sub(5,5) == 0
    assert sub(5,3) == 2

