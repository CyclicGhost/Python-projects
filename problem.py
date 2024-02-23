from math import sqrt
from typing import Union
from typing import Optional


def add_numbers(one: int, two: int) -> int:
    return one + two


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: Optional[float]) -> Optional[float]:
    if your_number <= 0:
        return

    else:
        root: float = calculate_square_root(your_number)
        return f"Мы вычислили квадратный корень из введённого числа: {root}"


one: Union[int, float] = 10
two: Union[int, float] = 5

print("Сумма чисел:", add_numbers(one, two))
print(calc(25.5))
