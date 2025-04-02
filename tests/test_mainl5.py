from typing import Literal
from contextlib import nullcontext as does_not_raise
import pytest

from src.mainl5 import Calculator

# Имя обязательно с Test...!
class TestCalculator:
    @pytest.mark.parametrize(
            # Нету четких стандартов типа функции "с ошибками" и "без"
            # но можно использовать nullcontext и передавать expectation
            "x, y, res, expectation",
            [
                (1, 2, 0.5, does_not_raise()),
                (5, -1, -5, does_not_raise()),
                (5, "-1", -5, pytest.raises(TypeError)),
                (5, 0, 1, pytest.raises(ZeroDivisionError)),
            ]
    )
    def test_divide(self, x: int, y: int, res: float | int, expectation):
        # Отлавливаем ошибки
        # with pytest.raises(Имя ошибки):
        # with pytest.raises(TypeError):
        #     assert Calculator().divide(x,y) == res

        # то же самое, но отлавливаем ошибку в передаваемых параметрах
        with expectation:
            assert Calculator().divide(x,y) == res

    @pytest.mark.parametrize(
            "x, y, res, expectation",
            [
                (1, 2, 3, does_not_raise()),
                (5, -1, 4, does_not_raise()),
                (5, "-1", 4, pytest.raises(TypeError))
            ]
    )
    def test_add(self, x: int, y: int, res: int | float, expectation):
        with expectation:
            assert Calculator().add(x,y) == res