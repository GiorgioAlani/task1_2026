"""Точка входа в программу."""

from circle_calculator import CircleSquareCalculate


if __name__ == "__main__":
    # Параметры прямоугольной области
    A = B = 10
    
    # Параметры круга
    R = 1
    X0 = Y0 = 5
    
    # Количество испытаний для статистики
    N = 10000
    
    calc = CircleSquareCalculate(A, B, R, X0, Y0, N)
    mean, var = calc.calculate_statistics(trials=10)
    
    print(f"Математическое ожидание: {mean:.6f}")
    print(f"Дисперсия: {var:.6f}")
    print(f"Ответ: {mean:.6f} (𝜋)")