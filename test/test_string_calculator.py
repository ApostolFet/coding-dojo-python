# TODO пустая строка возвращает 0
# TODO два числа через запятую возвращают сумму
# TODO одно число возвращает это число

# TODO метод принимает \n в качестве разделителя
# TODO поддержка кастомных разделителей в формате "//<delimeter>\n<numbers>"

import pytest

from string_calculator.string_calculator import StringCalculator


@pytest.fixture
def string_calculator():
    return StringCalculator()


def test_add_empty_return_zero(string_calculator):
    result = string_calculator.add("")
    assert result == 0


def test_add_single_number_return_it_self(string_calculator):
    result = string_calculator.add("1")
    assert result == 1


@pytest.mark.parametrize(
    ("input_value", "expected_value"),
    [
        ("1,2", 3),
        ("1,2,3", 6),
    ],
)
def test_add_separate_by_comma(string_calculator, input_value: str, expected_value: int):
    result = string_calculator.add(input_value)
    assert result == expected_value


def test_add_separate_by_end_of_line(string_calculator):
    result = string_calculator.add("1,2\n3")
    assert result == 6

def test_add_separated_by_custom_delimeter(string_calculator):
    result = string_calculator.add("//x\n1x2x100")
    assert result == 103
