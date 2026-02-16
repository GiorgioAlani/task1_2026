import random

class CircleSquareCalculate:
    """Класс для оценки площади круга методом Монте-Карло."""
    
    def __init__(self, a, b, r, x0, y0, n):
        """Метод для инициализации параметров."""
        self.a = a
        self.b = b
        self.r = r
        self.x0 = x0
        self.y0 = y0
        self.n = n
        
    def is_point_in_circle(self, x, y):
        """Метод для проверки, находится ли точка (x, y) внутри круга."""
        return (x - self.x0)**2 + (y - self.y0)**2 <= self.r**2
    
    def number_of_points_calculate(self):
        """Метод для подсчета кол-ва точек, попавших в круг."""
        count = 0
        for i in range(self.n):
            a = random.uniform(0.0, self.a)
            b = random.uniform(0.0, self.b)
            if self.is_point_in_circle(a, b):
                count += 1
        return count
    
    def final_square(self):
        """Метод который вычисляет приблизительную площадь круга."""
        count = self.number_of_points_calculate()
        return count / self.n * self.a * self.b
    
    def calculate_statistics(self, trials=10):
        """Метод для определения мат. ожидания и дисперсии."""
        results = []
        for i in range(trials):
            results.append(self.final_square())
        expectation = sum(results) / trials
        expectation_of_squares = sum(x**2 for x in results) / trials
        variance = expectation_of_squares - expectation**2
        return expectation, variance