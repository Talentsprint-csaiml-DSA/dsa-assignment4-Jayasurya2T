import pytest
import main

def test_case_1():
    n = 3
    boy_preferences = [[1, 2, 3], [2, 1, 3], [1, 2, 3]]
    girl_preferences = [[2, 1, 3], [1, 3, 2], [3, 1, 2]]
    expected_output = [(2, 1), (1, 2), (3, 3)]
    
    assert main.stable_marriage(n, boy_preferences, girl_preferences) == expected_output


def test_case_2():
    n = 2
    boy_preferences = [[1, 2], [2, 1]]
    girl_preferences = [[2, 1], [1, 2]]
    expected_output = [(2, 1), (1, 2)]
    
    assert main.stable_marriage(n, boy_preferences, girl_preferences) == expected_output


def test_case_3():
    n = 4
    boy_preferences = [[1, 2, 3, 4], [3, 1, 4, 2], [2, 3, 1, 4], [4, 1, 2, 3]]
    girl_preferences = [[2, 1, 3, 4], [3, 4, 1, 2], [1, 3, 4, 2], [4, 3, 2, 1]]
    expected_output = [(2, 1), (3, 2), (1, 3), (4, 4)]
    
    assert main.stable_marriage(n, boy_preferences, girl_preferences) == expected_output

