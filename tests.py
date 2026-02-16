"""Тесты для класса CircleSquareCalculate."""

import unittest
import math
from circle_calculator import CircleSquareCalculate


class TestCircleSquareCalculate(unittest.TestCase):
    """Тесты для методов класса."""

    def setUp(self):
        """Инициализация параметров для теста."""
        self.calc = CircleSquareCalculate(a=10, b=10, r=1, x0=5, y0=5, n=1000)

    def test_point_in_circle_center(self):
        """Точка в центре круга должна возвращать True."""
        self.assertTrue(self.calc.is_point_in_circle(5, 5))

    def test_point_in_circle_edge(self):
        """Точки на границе круга (расстояние = радиусу) должны возвращать True."""
        self.assertTrue(self.calc.is_point_in_circle(6, 5)) 
        self.assertTrue(self.calc.is_point_in_circle(4, 5))  
        self.assertTrue(self.calc.is_point_in_circle(5, 6)) 
        self.assertTrue(self.calc.is_point_in_circle(5, 4))  

    def test_point_outside_circle(self):
        """Точка вне круга должна возвращать False."""
        self.assertFalse(self.calc.is_point_in_circle(0, 0))
        self.assertFalse(self.calc.is_point_in_circle(10, 10))

    def test_area_approximation(self):
        """Площадь круга должна быть близка к π*r². Допустимая погрешность для проверки - 20%."""
        expected_area = math.pi * self.calc.r ** 2 
        calculated_area = self.calc.final_square()
        self.assertAlmostEqual(calculated_area, expected_area, delta=expected_area * 0.2)


if __name__ == "__main__":
    unittest.main()