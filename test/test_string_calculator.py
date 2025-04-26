#TODO пустая строка возвращает 0
#TODO два числа через запятую возвращают сумму

#TODO одно число возвращает это число
import pytest

from string_calculator.string_calculator import StringCalculator


class TestStringCalculator:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.string_calculator = StringCalculator()

    def test_empty_return_zero(self):
        result = self.string_calculator.add("")
        assert result == 0

    def test_single_number_return_it_self(self):
        result = self.string_calculator.add("1")
        assert result == 1

    def test_two_numbers_returns_their_sum(self):
        result = self.string_calculator.add("1,2")
        assert result == 3
