from calculator.calculator import Calculator
import pytest 

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        a = 380
        b = 200
        cal = Calculator()

        result = cal.subtract(a, b)

        expected = 180
        assert result == expected

    def test_multiply(self):
        a = 5
        b = 5
        cal = Calculator()

        result = cal.multiply(a, b)

        expected = 25
        assert result == expected

    def test_divide(self):
        a = 160
        b = 20
        cal = Calculator()

        result = cal.divide(a, b)

        expected = 8
        assert result == expected

    def test_divide_by_zero(self):
        a = 60
        b = 0 
        cal = Calculator()

        # act & assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a, b)
