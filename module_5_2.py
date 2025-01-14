import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'(?<!\S)(-?\d+\.\d+|-?\d+)(?!\S)'
    for match in re.finditer(pattern, text):
        yield float(match.group(0))  # цифра замінюється

def sum_profit(text: str, func: Callable):
    "  загальній прибуток"
    return sum(func(text))  # сумма чисел
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
