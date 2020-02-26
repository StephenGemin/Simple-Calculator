"""
Unit tests for calculator library
"""

import calculator


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
