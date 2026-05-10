# Exercise 03: Calculator — TDD

## This time, you write the test first

Open [calculator.py](calculator.py) — the methods are all stubs (`pass`). Nothing works yet.

Open [test_calculator.py](test_calculator.py) — one test is already written. The rest is yours.

## The TDD loop

```
1. Write one test
2. Run pytest → it FAILS  (RED)
3. Implement just enough code to make it pass
4. Run pytest → it PASSES (GREEN)
5. Write the next test → repeat
```

## What Calculator should do

| Method | Behavior |
|---|---|
| `add(a, b)` | Returns `a + b` |
| `subtract(a, b)` | Returns `a - b` |
| `multiply(a, b)` | Returns `a * b` |
| `divide(a, b)` | Returns `a / b` — raises `ValueError` if `b` is 0 |

## Run your tests

```bash
pytest 03_calculator/ -v
```

## Hint: testing that an exception is raised

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator().divide(5, 0)
```
