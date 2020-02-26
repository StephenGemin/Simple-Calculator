"""
Unit tests for calculator library
"""
import pytest

from calculator import calculator


class TestCalculator:

    def test_addition_yields_positive_value(self):
        assert 4 == calculator.add(2, 2)

    def test_add_yields_negative_value(self):
        assert -3 == calculator.add(-5, 2)

    def test_addition_equals_zero(self):
        assert 0 == calculator.add(2, -2)

    def test_subtract_yields_positive_value(self):
        assert 1 == calculator.subtract(6, 5)

    def test_subtract_yields_negative_value(self):
        assert -1 == calculator.subtract(5, 6)

    def test_subtraction_equals_zero(self):
        assert 0 == calculator.subtract(3, 3)

    def test_multiply_yields_positive_value(self):
        assert 4 == calculator.multiply(2, 2)

    def test_multiply_two_negatives_yields_positive_value(self):
        assert 4 == calculator.multiply(-2, -2)

    def test_multiply_yields_negative_value(self):
        assert -4 == calculator.multiply(-2, 2)

    def test_multiply_equals_zero(self):
        assert 4 == calculator.multiply(2, 2)

    def test_multiply_large_positive_values(self):
        assert 15241578750190521 == calculator.multiply(123456789, 123456789)

    def test_divide_yields_positive_value(self):
        assert 1 == calculator.divide(2, 2)

    def test_divide_two_negatives_yields_positive_value(self):
        assert 1 == calculator.divide(-2, -2)

    def test_divide_yields_negative_value(self):
        assert -1 == calculator.divide(-2, 2)

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            calculator.divide(2, 0)

    def test_divide_yields_fixed_decimal(self):
        assert 2.5 == calculator.divide(5, 2)

    def test_divide_not_yield_rounding_error(self):
        assert 1.7/5 == calculator.divide(1.7, 5)

    def test_divide_yields_repeating_decimal(self):
        assert 1.6/3 == calculator.divide(1.6, 3)
