#TODO пустая строка возвращает 0

#TODO одно число возвращает это число
#TODO два числа через запятую возвращают сумму

from string_calculator.string_calculator import StringCalculator


def test_empty_return_zero():
    result = StringCalculator().add("")
    assert result == 0

def test_single_number_return_it_self():
    result = StringCalculator().add("1")
    assert result == 1

