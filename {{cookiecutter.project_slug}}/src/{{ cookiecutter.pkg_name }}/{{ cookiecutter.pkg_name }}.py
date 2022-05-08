#!/usr/bin/env python3
# Core Library modules
from typing import Any


def fizzbuzz(number_range: int) -> list:
    result: list[Any] = []
    for num in range(1, number_range):
        if num % 15 == 0:
            result.append("FizzBuzz")
        elif num % 5 == 0:
            result.append("Buzz")
        elif num % 3 == 0:
            result.append("Fizz")
        else:
            result.append(num)
    return result


def fibonacci(number_range: int) -> list:
    result: list = []
    a, b = 1, 1
    while True:
        if a >= number_range:
            return result
        result.append(a)
        a, b = b, (a + b)
