import pytest
from solution import problem1, problem2, problem3, problem4, problem5

def test_problem_1_basic():
    assert problem1(10) == 23, "La función debería retornar 23 para el límite 10"

def test_problem_2_basic():
    assert problem2(10) == 10, "La función debería retornar 10 como la suma de los primeros términos pares"

def test_problem_3_basic():
    assert problem3(13195) == 29, "La función debería retornar 29 como el mayor factor primo de 13195"

def test_problem_4_is_palindrome():
    result = problem4()
    assert str(result) == str(result)[::-1], "El resultado debería ser un palíndromo"

def test_problem_4_within_expected_range():
    result = problem4()
    assert 10000 <= result <= 998001, "El resultado debería estar dentro del rango de productos de dos números de 3 dígitos"


def test_problem_5_basic():
    assert problem5(10) == 2520, "La función debería retornar 2520 como el número divisible por todos los números del 1 al 10"