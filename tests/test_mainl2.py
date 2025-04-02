# Такие импорты нужно явно указывать в конфигурационном файле
from src.mainl2 import A

def test_main():
    # убеждаемся, что-то равно чему-то
    assert A.x == 1

def test_2():
    assert 2 == 2

