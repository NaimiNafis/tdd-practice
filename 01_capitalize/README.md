# Exercise 01: capitalize

## The function is already implemented

Open [capitalize.py](capitalize.py) and read it. This is the code you are testing.

```python
capitalize("hello")   # → "Hello"
capitalize("HELLO")   # → "HELLO"  (only first char is changed)
capitalize("a")       # → "A"
capitalize("")        # → ""
```

## Your job: write tests

Open [test_capitalize.py](test_capitalize.py). One example test is already there.

Write more tests — try to break the function. Think about:
- What if the first character is already uppercase?
- What if the string is empty?
- What if there's only one character?

## Run your tests

```bash
pytest 01_capitalize/ -v
```

If all your tests pass, the function handles those cases correctly.
If a test fails, either the function has a bug — or your test expectation is wrong. Both are useful!
