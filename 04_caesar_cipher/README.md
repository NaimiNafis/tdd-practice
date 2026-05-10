# Exercise 04: caesar_cipher

## Task

Implement the function `caesar_cipher(string, shift)` in [caesar_cipher.py](caesar_cipher.py).

## What it should do

Shift every **alphabetic character** in the string by `shift` positions in the alphabet. Everything else (spaces, punctuation, numbers) stays unchanged.

## Rules

- **Wrap around**: after `z` comes `a` again (and after `Z` comes `A`)
- **Preserve case**: uppercase stays uppercase, lowercase stays lowercase
- **Non-alpha unchanged**: spaces, punctuation, digits are not shifted

## Examples

```python
caesar_cipher("abc", 1)           # → "bcd"
caesar_cipher("xyz", 3)           # → "abc"   (wraps around)
caesar_cipher("Hello", 13)        # → "Uryyb"  (case preserved)
caesar_cipher("Hello, World!", 5) # → "Mjqqt, Btwqi!"  (punctuation unchanged)
caesar_cipher("abc", 0)           # → "abc"   (shift of 0)
```

## Steps

1. Read `test_caesar_cipher.py`
2. Implement `caesar_cipher` in `caesar_cipher.py`
3. Run `pytest 04_caesar_cipher/`
4. Fix until all tests pass

## Hints

- `ord('a')` gives the ASCII value of `'a'` (97). `chr(97)` gives `'a'` back.
- To shift with wrap-around for lowercase: `chr((ord(c) - ord('a') + shift) % 26 + ord('a'))`
- Use `str.isalpha()`, `str.isupper()`, `str.islower()` to check character type
