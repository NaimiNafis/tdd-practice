# Exercise 05: analyze_array

## Task

Implement the function `analyze_array(numbers)` in [analyze_array.py](analyze_array.py).

## What it should do

Accept a list of numbers and return a **dictionary** with these keys:

| Key | Value |
|---|---|
| `"average"` | Mean of the list (float) |
| `"min"` | Smallest value |
| `"max"` | Largest value |
| `"length"` | Number of elements |

If the list is **empty**, raise a `ValueError`.

## Examples

```python
analyze_array([1, 8, 3, 4, 2, 6])
# → {"average": 4.0, "min": 1, "max": 8, "length": 6}

analyze_array([5])
# → {"average": 5.0, "min": 5, "max": 5, "length": 1}

analyze_array([])
# → raises ValueError
```

## Steps

1. Read `test_analyze_array.py`
2. Implement `analyze_array` in `analyze_array.py`
3. Run `pytest 05_analyze_array/`
4. Fix until all tests pass

## Hints

- Python builtins: `sum()`, `min()`, `max()`, `len()`
- Average: `sum(numbers) / len(numbers)`
- Return a dict: `{"average": ..., "min": ..., "max": ..., "length": ...}`
