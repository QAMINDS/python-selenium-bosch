import pytest

def do_something():
    print('Hola')

def test_hola_mundo():
    raise ValueError()

@pytest.mark.qaminds
def test_valido():
    do_something()
    True

