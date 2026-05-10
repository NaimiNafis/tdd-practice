import pytest
from analyze_array import analyze_array


def test_returns_correct_average():
    result = analyze_array([1, 8, 3, 4, 2, 6])
    assert result["average"] == 4.0


def test_returns_correct_min():
    result = analyze_array([1, 8, 3, 4, 2, 6])
    assert result["min"] == 1


def test_returns_correct_max():
    result = analyze_array([1, 8, 3, 4, 2, 6])
    assert result["max"] == 8


def test_returns_correct_length():
    result = analyze_array([1, 8, 3, 4, 2, 6])
    assert result["length"] == 6


def test_single_element():
    result = analyze_array([5])
    assert result == {"average": 5.0, "min": 5, "max": 5, "length": 1}


def test_negative_numbers():
    result = analyze_array([-3, -1, -2])
    assert result["min"] == -3
    assert result["max"] == -1
    assert result["average"] == -2.0


def test_empty_list_raises():
    with pytest.raises(ValueError):
        analyze_array([])
