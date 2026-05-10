# Python Unit Testing 勉強会

A hands-on workshop for learning unit testing and test-driven development (TDD) with Python and pytest.

---

## Setup

### 1. Fork this repo

Click **Fork** at the top-right of this GitHub page. This creates your own copy.

### 2. Clone your fork

```bash
git clone https://github.com/<your-username>/tdd-practice.git
cd tdd-practice
```

### 3. Install pytest

```bash
pip install -r requirements.txt
```

---

## How to run tests

```bash
pytest 01_capitalize/ -v    # run one exercise
pytest -v                   # run everything
```

---

## Reading a test

```python
from capitalize import capitalize   # import the function

def test_capitalizes_first_letter():      # function name starts with test_
    assert capitalize("hello") == "Hello" # assert: expected value on the right
```

When a test **fails**, pytest shows you what value you got vs. what was expected.  
When it **passes**, you get a green dot.

---

## Workshop flow

### Part 1 — Write tests for existing code (exercises 01–02)

The functions are already implemented. **Your job: write tests for them.**

This teaches you how to read a function and think about what cases to verify.

| Exercise | Function |
|---|---|
| [01_capitalize/](01_capitalize/) | `capitalize(string)` |
| [02_reverse_string/](02_reverse_string/) | `reverse_string(string)` |

### Part 2 — TDD: write the test first (exercise 03)

The function is **not implemented** yet. You write a test first, watch it fail, then implement.

| Exercise | Function |
|---|---|
| [03_calculator/](03_calculator/) | `Calculator` class |

### Bonus — Extra exercises

Pre-written tests, stub implementations. Make them pass.

| Exercise | Function |
|---|---|
| [04_caesar_cipher/](04_caesar_cipher/) | `caesar_cipher(string, shift)` |
| [05_analyze_array/](05_analyze_array/) | `analyze_array(numbers)` |
