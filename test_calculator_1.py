from Calculator_1 import add
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 2) == 0
    assert add(0 , 0) == 0

def test_raises_integer_plus_string():
    with pytest.raises(TypeError):
        add(3,"c")                              